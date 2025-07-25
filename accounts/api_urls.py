from rest_framework.routers import DefaultRouter
from .views import (
    EmployeeViewSet,
    AttendanceViewSet,
    FinancialTransactionViewSet,
    PesticideScheduleViewSet
)

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'financial-transactions', FinancialTransactionViewSet)
router.register(r'pesticide-schedules', PesticideScheduleViewSet)

urlpatterns = router.urls
