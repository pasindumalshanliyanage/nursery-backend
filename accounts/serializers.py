from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Employee, Attendance, FinancialTransaction, PesticideSchedule , DailySalary

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class FinancialTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialTransaction
        fields = '__all__'

class PesticideScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PesticideSchedule
        fields = '__all__'

class DailySalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySalary
        fields = '__all__'


    def create(self, validated_data):
        is_half_day = validated_data.get('is_half_day', False)
        amount = validated_data.get('amount')

        if is_half_day:
            validated_data['amount'] = round(float(amount) / 2, 2)

        return super().create(validated_data)

    def update(self, instance, validated_data):
        is_half_day = validated_data.get('is_half_day', instance.is_half_day)
        amount = validated_data.get('amount', instance.amount)

        if is_half_day:
            validated_data['amount'] = round(float(amount) / 2, 2)

        return super().update(instance, validated_data)