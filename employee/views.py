from django.shortcuts import render, redirect
from .models import Employee, Beneficiary
from .forms import EmployeeForm, BeneficiaryForm
from .serializers import EmployeeSerializers, BeneficiarySerializers
from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
import xlwt
from django.http import HttpResponse
import os

def index(request):
    return render(request, 'index.html')


def list_employees(request):
    try:
        employees = Employee.objects.filter(active=1)
        serializer = EmployeeSerializers(employees, many=True)
        return render(request, 'list_employees.html', {'employees': serializer.data})
    except:
        return render(request, 'list_employees.html', {'employees': []})


def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('list-employees')
            except:
                return redirect('list-employees')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})


def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(request.POST, instance=employee)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list-employees')
    context = {
        'form': form,
        'employee': employee
    }
    return render(request, 'update_employee.html', context)


def deactivate_employee(request, pk):
    if request.method == 'POST':
        Employee.objects.filter(pk=pk).update(active=0)
        return redirect('list-employees')

    employee = Employee.objects.filter(pk=pk).first()
    context = {
        'employee': employee
    }
    return render(request, 'deactivate_employee.html', context)


def detail_beneficiaries(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        beneficiaries = Beneficiary.objects.filter(employee=employee)
        serializer_beneficiaries = BeneficiarySerializers(beneficiaries, many=True)
        return render(request, 'list_beneficiaries.html',
                      {'employee': employee, 'beneficiaries': serializer_beneficiaries.data})
    except Beneficiary.DoesNotExist:
        return render(request, 'list_beneficiaries.html', {'employees': employee, 'beneficiary': []})


def create_beneficiary(request):
    if request.method == "POST":
        form = BeneficiaryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('list-employees')
            except:
                pass
    form = BeneficiaryForm()
    return render(request, 'beneficiary_form.html', {'form': form})


def update_beneficiary(request, pk):
    beneficiary = Beneficiary.objects.get(id=pk)
    form = BeneficiaryForm(instance=beneficiary)
    if request.method == 'POST':
        form = BeneficiaryForm(request.POST, instance=beneficiary)
        if form.is_valid():
            form.save()
            return redirect('detail-employees', pk=beneficiary.employee.id)

    context = {
        'beneficiary': beneficiary,
        'form': form,
    }
    return render(request, 'update_beneficiary.html', context)


def delete_beneficiary(request, pk):
    beneficiary = Beneficiary.objects.get(id=pk)
    if request.method == 'POST':
        beneficiary.delete()
        return redirect('detail-employees', pk=beneficiary.employee.id)

    context = {
        'beneficiary': beneficiary,
    }
    return render(request, 'delete_beneficiary.html', context)


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="lista_empleados.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nombre completo', 'Puesto de trabajo', 'Salario', 'Estatus', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Employee.objects.all().values_list('full_name', 'job', 'salary', 'status')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
