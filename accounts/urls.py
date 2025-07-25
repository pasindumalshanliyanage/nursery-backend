
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import DailySalaryViewSet 
from . import views

router = DefaultRouter()
router.register(r'daily-salaries', DailySalaryViewSet)

urlpatterns = [
    path('employees/', views.EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
    path('attendances/', views.AttendanceListCreateAPIView.as_view(), name='attendance-list-create'),
    path('financial-transactions/', views.FinancialTransactionListCreateAPIView.as_view(), name='financial-transaction-list-create'),
    path('pesticide-schedules/', views.PesticideScheduleListCreateAPIView.as_view(), name='pesticide-schedule-list-create'),
    path('pesticide-schedules/', views.PesticideScheduleListCreateAPIView.as_view(), name='pesticide-schedule-list-create'),
    path('', include(router.urls)),
]
