from rest_framework import serializers
from .models import Employee, Beneficiary


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    # def validate_full_name(self, value):
    #     if len(value) == 0:
    #         raise serializers.ValidationError('Error in the field full name value')
    #
    # def validate_job(self, value):
    #     if len(value) == 0 or len(value) > 50:
    #         raise serializers.ValidationError('Error in the field photo value')
    #
    # def validate_photo(self, value):
    #     if len(value) == 0 or len(value) > 50:
    #         raise serializers.ValidationError('Error in the field photo value')
    #
    # def validate_salary(self, value):
    #     if len(value) < 10 or len(value) > 50:
    #         raise serializers.ValidationError('Error in the field salary value')
    #
    # def validate_status(self, value):
    #     try:
    #         int(value)
    #         if value < 0:
    #             raise serializers.ValidationError('Error in the field status value')
    #     except ValueError:
    #         raise serializers.ValidationError('Error in the field status value')


class BeneficiarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = '__all__'

    # def validate_full_name(self, value):
    #     if len(value) == 0:
    #         raise serializers.ValidationError('Error in the field full name value')
    #
    # def validate_relationship(self, value):
    #     if len(value) == 0:
    #         raise serializers.ValidationError('Error in the field relationship value')
    #
    # def validate_sex(self, value):
    #     if len(value) == 0:
    #         raise serializers.ValidationError('Error in the field sex value')
    #
    # def validate_birthday(self, value):
    #     if len(value) == 0:
    #         raise serializers.ValidationError('Error in the field birthday value')