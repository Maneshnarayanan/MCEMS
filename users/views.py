from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from employees.models import Employee,Attendance

from employees.forms import EmployeeForm2

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee-profile')  
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request):
    # Fetch the employee object for the logged-in user
    employee = get_object_or_404(Employee, user=request.user)

    active_attendance = Attendance.objects.filter(employee=employee, clock_out__isnull=True).first()

    context = {
        'employee': employee,
        'active_attendance': active_attendance  # Pass the active attendance record (if exists)
    }
    # Render the template with the employee's profile data
    return render(request, 'users/profile.html', context)

def home(request):
    return render(request, 'index.html')


@login_required
def edit_profile_view(request):
    # Fetch the employee object for the logged-in user
    employee = get_object_or_404(Employee, user=request.user)

    if request.method == 'POST':
        form = EmployeeForm2(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('employee-profile')  # Redirect to the profile view after saving
    else:
        form = EmployeeForm2(instance=employee)

    context = {
        'form': form
    }

    return render(request, 'users/edit_profile.html', context)


