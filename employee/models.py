from django.db import models
from enum import Enum


class Sex(Enum):
    M = "Masculino"
    F = "Femenino"

    def __str__(self):
        return self.name


class Relationship(Enum):
    P = 'Padre'
    M = 'Madre'
    E = 'Esposa'
    H = 'Hijo'
    A = 'Amigo'

    def __str__(self):
        return self.name


class Status(Enum):
    S = "Soltero"
    C = "Casado"
    P = "Separado"
    D = "Divorciado"
    V = "Viudo"


    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=250, null=False, blank=True)
    job = models.CharField(max_length=50, null=False, blank=True)
    photo = models.FileField(null=True, blank=True, upload_to='images')
    salary = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Status])
    hiring_date = models.DateTimeField(auto_now_add=True, verbose_name="hiring_date")
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.full_name


class Beneficiary(models.Model):
    full_name = models.CharField(max_length=250, null=False, blank=True)
    relationship = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Relationship])
    sex = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Sex])
    birthday = models.DateField(verbose_name="Birthday", null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employee", null=True)

    class Meta:
        db_table = "beneficiary"

    def __str__(self):
        return self.full_name