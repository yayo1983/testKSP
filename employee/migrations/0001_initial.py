# Generated by Django 4.1.5 on 2023-02-01 18:20

from django.db import migrations, models
import django.db.models.deletion
import employee.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=250)),
                ('job', models.CharField(blank=True, max_length=50)),
                ('photo', models.FileField(upload_to='')),
                ('salary', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(choices=[(employee.models.Status['S'], 'Soltero'), (employee.models.Status['C'], 'Casado'), (employee.models.Status['P'], 'Separado'), (employee.models.Status['D'], 'Divorciado'), (employee.models.Status['V'], 'Viudo')], max_length=10)),
                ('hiring_date', models.DateTimeField(auto_now_add=True, verbose_name='hiring_date')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=250)),
                ('relationship', models.CharField(choices=[(employee.models.Relationship['P'], 'Padre'), (employee.models.Relationship['M'], 'Madre'), (employee.models.Relationship['E'], 'Esposa'), (employee.models.Relationship['H'], 'Hijo'), (employee.models.Relationship['A'], 'Amigo')], max_length=10)),
                ('sex', models.CharField(choices=[(employee.models.Sex['M'], 'Masculino'), (employee.models.Sex['F'], 'Femenino')], max_length=10)),
                ('birthday', models.DateTimeField(auto_now_add=True, verbose_name='hiring_date')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='employee.employee')),
            ],
            options={
                'db_table': 'beneficiary',
            },
        ),
    ]
