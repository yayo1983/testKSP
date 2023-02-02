from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('employees/', views.list_employees, name='list-employees'),
    path('employee/create', views.create_employee, name='create-employee'),
    path('employees/employee_detail/<int:pk>', views.detail_beneficiaries, name='detail-employees'),
    path('employees/update/<int:pk>', views.update_employee, name='update-employee'),
    path('employees/deactivate/<int:pk>', views.deactivate_employee, name='delete-employee'),
    path('list_employees/employee_detail/create', views.create_beneficiary, name='create-beneficiary'),
    path('list_employees/employee_detail/update/<int:pk>', views.update_beneficiary, name='update-beneficiary'),
    path('list_employees/employee_detail/delete/<int:pk>', views.delete_beneficiary, name='delete-beneficiary'),
]
