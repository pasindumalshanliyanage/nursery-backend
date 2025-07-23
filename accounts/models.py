from django.db import models

from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name_sinhala = models.CharField(max_length=100, blank=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    ddress = models.TextField(blank=True, null=True)
    # Add any other fields you want, e.g.:
    # position = models.CharField(max_length=100)
    # date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    # other fields...

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
    class Meta:
        unique_together = ('employee', 'date')  # Prevent duplicate attendance for same day

    def __str__(self):
        status = "Present" if self.present else "Absent"
        return f"{self.employee.user.username} - {self.date} - {status}"

class FinancialTransaction(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

class PesticideSchedule(models.Model):
    pesticide_name = models.CharField(max_length=100)
    application_date = models.DateField()
    next_application_date = models.DateField()