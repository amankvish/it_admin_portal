from django.urls import path
from .views import login_view, dashboard_view, logout_view, employee_list, asset_list, assign_asset

urlpatterns = [
    path("login/", login_view, name="login_view"),
    path("dashboard/", dashboard_view, name="dashboard_view"),
    path("logout/", logout_view, name="logout_view"),
    path("employees/", employee_list, name="employee_list"),
    path("assets/", asset_list, name="asset_list"),
    path("assign-asset/", assign_asset, name="assign_asset"),
]
