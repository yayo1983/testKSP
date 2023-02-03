from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('employees/', views.list_employees, name='list-employees'),
    path('employee/create', views.create_employee, name='create-employee'),
    path('employee/employee_detail/<int:pk>', views.detail_beneficiaries, name='detail-employees'),
    path('employee/update/<int:pk>', views.update_employee, name='update-employee'),
    path('employee/deactivate/<int:pk>', views.deactivate_employee, name='delete-employee'),
    path('beneficiary/create', views.create_beneficiary, name='create-beneficiary'),
    path('beneficiary/update/<int:pk>', views.update_beneficiary, name='update-beneficiary'),
    path('beneficiary/delete/<int:pk>', views.delete_beneficiary, name='delete-beneficiary'),
    path('export_excel/', views.export_users_xls, name='export_excel'),
]
