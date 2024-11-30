from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Employee, Asset, Assignment

# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard_view")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "admin_dashboard/login.html")

# Dashboard View
@login_required
def dashboard_view(request):
    return render(request, "admin_dashboard/dashboard.html")

# Logout View
def logout_view(request):
    logout(request)
    return redirect("login_view")

# Employee Management
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "admin_dashboard/employee_list.html", {"employees": employees})

# Asset Management
@login_required
def asset_list(request):
    assets = Asset.objects.all()
    return render(request, "admin_dashboard/asset_list.html", {"assets": assets})

# Assign Assets
@login_required
def assign_asset(request):
    if request.method == "POST":
        employee_id = request.POST["employee"]
        asset_id = request.POST["asset"]
        employee = get_object_or_404(Employee, id=employee_id)
        asset = get_object_or_404(Asset, id=asset_id)
        Assignment.objects.create(employee=employee, asset=asset)
        messages.success(request, "Asset assigned successfully.")
        return redirect("assign_asset")
    employees = Employee.objects.all()
    assets = Asset.objects.all()
    return render(request, "admin_dashboard/assign_asset.html", {"employees": employees, "assets": assets})
