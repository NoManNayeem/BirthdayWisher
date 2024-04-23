from django.contrib import admin
from .models import Customer

import csv
from django.http import HttpResponse
from django.contrib import admin

def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="customers.csv"'
    writer = csv.writer(response)
    # Write header row
    writer.writerow(['Name', 'Email', 'Birthday'])
    # Write data rows
    for customer in queryset:
        writer.writerow([customer.name, customer.email, customer.birthday])
    return response

export_as_csv.short_description = 'Export as CSV'

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'birthday')
    actions = [export_as_csv]

