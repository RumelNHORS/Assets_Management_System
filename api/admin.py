from django.contrib import admin
from . models import AssetsModel, CheckIn, CheckOut, CheckOutAndReturn, DeviceLog, Company

#Admin for All Models

@admin.register(AssetsModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_name', 'date', 'asset', 'brand', 'quantity']
    search_fields = ('employee_name', 'asset')

@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_name', 'email', 'asset', 'checkin_date']
    search_fields = ('employee_name', 'phone')
    
@admin.register(CheckOut)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_name', 'email', 'asset', 'checkout_date']
    search_fields = ('employee_name', 'phone')

@admin.register(CheckOutAndReturn)
class CheckOutAndReturnAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_name', 'email', 'phone', 'asset']
    search_fields = ('employee_name', 'phone')

@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'devcice', 'Company_name', 'employee_name', 'hand_out_condition', 'return_condition']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email', 'phone']
