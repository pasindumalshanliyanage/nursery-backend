from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Employee, Attendance, FinancialTransaction, PesticideSchedule, DailySalary
from django.contrib.auth.models import User
from .serializers import (RegisterSerializer,
                          EmployeeSerializer,
                          AttendanceSerializer,
                          FinancialTransactionSerializer,
                          PesticideScheduleSerializer,
                          DailySalarySerializer
)
                          

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer 

# Create your views here.
class AttendanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class FinancialTransactionViewSet(viewsets.ModelViewSet):
    queryset = FinancialTransaction.objects.all()
    serializer_class = FinancialTransactionSerializer

class PesticideScheduleViewSet(viewsets.ModelViewSet):
    queryset = PesticideSchedule.objects.all()
    serializer_class = PesticideScheduleSerializer

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class FinancialTransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = FinancialTransaction.objects.all()
    serializer_class = FinancialTransactionSerializer

class PesticideScheduleListCreateAPIView(generics.ListCreateAPIView):
    queryset = PesticideSchedule.objects.all()
    serializer_class = PesticideScheduleSerializer

class DailySalaryViewSet(viewsets.ModelViewSet):
    queryset = DailySalary.objects.all()
    serializer_class = DailySalarySerializer
    permission_classes = [IsAuthenticated]