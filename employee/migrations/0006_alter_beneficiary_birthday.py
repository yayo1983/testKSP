# Generated by Django 4.1.5 on 2023-02-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_beneficiary_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='birthday',
            field=models.DateField(help_text="Beneficiary's birthdate"),
        ),
    ]
