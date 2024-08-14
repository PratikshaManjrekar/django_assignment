from django.db import models

# Create your models here.
class Attendance(models.Model):
    emp_no       = models.CharField(max_length=10)
    month        = models.CharField(max_length=20)
    present_days = models.IntegerField()

    def __str__(self):
        return f"Attendance of {self.emp_no} for {self.month}"
    
class BasicPay(models.Model):
    emp_no           = models.CharField(max_length=10)
    basic_pay_amount = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"Basic Pay of {self.emp_no} is {self.basic_pay_amount}"
    
class IncomeTax(models.Model):
    emp_no                = models.CharField(max_length=10)
    income_tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Income Tax of {self.emp_no} is {self.income_tax_percentage}"
