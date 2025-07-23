from django.contrib import admin
from .models import Employee, Attendance, FinancialTransaction, PesticideSchedule

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(FinancialTransaction)
admin.site.register(PesticideSchedule)
