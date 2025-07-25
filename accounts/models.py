from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name_sinhala = models.CharField(max_length=100, blank=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=100)  # ✅ This should be here
    daily_wage = models.DecimalField(max_digits=10, decimal_places=2)  # ✅ This too

    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.user.username} - {self.date} - {'Present' if self.present else 'Absent'}"
class FinancialTransaction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
class PesticideSchedule(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
# accounts/models.py

class DailySalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_half_day = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.amount}"
