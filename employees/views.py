from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee, Attendance, LeaveRequest
from .forms import EmployeeForm
from django.utils import timezone

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee/employee_detail.html', {'employee': employee})

@login_required
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form})

@login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_form.html', {'form': form})

@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})


@login_required
def record_attendance(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        employee = get_object_or_404(Employee, employee_id=employee_id)

        # Check if there is already an open attendance record (clock_out is None)
        attendance_record = Attendance.objects.filter(employee=employee, clock_out__isnull=True).first()

        if attendance_record:
            # If the employee already clocked in, update the clock_out time
            attendance_record.clock_out = timezone.now()
            attendance_record.save()
        else:
            # If there is no open attendance record, create a new one with clock_in
            Attendance.objects.create(employee=employee, clock_in=timezone.now())

        return redirect('employee-profile')  # Redirect to employee profile after clocking in/out
    else:
        # Return a form or redirect in case of a GET request
        return render(request, 'employee/attendance_form.html')

@login_required
def clock_out_attendance(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if attendance.clock_out is None:
        attendance.clock_out = timezone.now()
        attendance.save()
    return redirect('employee-profile')

@login_required
def leave_request(request):
    if request.method == 'POST':
        employee_id = request.POST['employee_id']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        reason = request.POST['reason']
        employee = get_object_or_404(Employee, employee_id=employee_id)
        LeaveRequest.objects.create(employee=employee, start_date=start_date, end_date=end_date, reason=reason)
        return redirect('employee_detail', pk=employee.pk)
