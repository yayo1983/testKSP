from django import forms
from .models import Employee, Beneficiary, Status, Sex, Relationship


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

    def choices(em):
        return [(e.name, e.value) for e in em]

    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=4, max_length=250, label='Nombre completo')
    job = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=1, max_length=50, label='Puesto de trabajo')
    salary = forms.CharField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}), label='Salario')
    status = forms.ChoiceField(
        label = 'Estatus',
        choices = choices(Status),
        widget = forms.Select(attrs={'class': 'form-control'}),
    )
    hiring_date = forms.CharField(required=True, widget=forms.SelectDateWidget(attrs={'class': 'form-control'}), min_length=4, max_length=250, label='Fecha de contratación')
    photo = forms.FileField(label='Foto', required=False)


class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = "__all__"

        def choices(em):
            return [(e.name, e.value) for e in em]

        full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=4, max_length=250, label='Nombre completo')
        relationship = forms.ChoiceField(
            label = 'Parentesco',
            choices=choices(Relationship),
            widget=forms.Select(attrs={'class': 'form-control'}),
        )
        sex = forms.ChoiceField(
            label = 'Sexo',
            choices=choices(Sex),
            widget=forms.Select(attrs={'class': 'form-control'}),
        )
        birthday = forms.CharField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}), min_length=1, max_length=5, label='Fecha de nacimiento')