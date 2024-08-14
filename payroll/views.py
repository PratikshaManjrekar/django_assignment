from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def dashboard(request):
    emp_nos = Attendance.objects.values_list('emp_no', flat=True).distinct()
    months  = Attendance.objects.values_list('month',flat=True).distinct()
    context = {
        'emp_nos': emp_nos,
        'months' : months,
    }
    return render(request, 'payroll/dashboard.html', context)


def calculate_pay(request):
    emp_no     = request.GET.get('emp_no')
    month      = request.GET.get('month')

    attendance = Attendance.objects.filter(emp_no=emp_no, month=month).first()
    basic_pay  = BasicPay.objects.filter(emp_no=emp_no).first()
    income_tax = IncomeTax.objects.filter(emp_no=emp_no).first()

    if attendance and basic_pay and income_tax:
        gross_pay = basic_pay.basic_pay_amount
        net_pay   = gross_pay * (1 - income_tax.income_tax_percentage / 100)
        data      = {
            'gross_pay'  : gross_pay,
            'net_pay'    : net_pay,
        }
    else:
        data = {
            'gross_pay'  : 0,
            'net_pay'    : 0,
        }
    
    return JsonResponse(data)
