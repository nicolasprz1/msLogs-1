from django.urls import path
from .views import (
    LoginLogView,
    PasswordChangeLogView,
    AccountBlockLogView,
    ReportLogView,
)

urlpatterns = [
    path('login/', LoginLogView.as_view(), name='login-logs'),
    path('password-change/', PasswordChangeLogView.as_view(), name='password-change-logs'),
    path('account-block/', AccountBlockLogView.as_view(), name='account-block-logs'),
    path('reports/', ReportLogView.as_view(), name='report-logs'),
]
