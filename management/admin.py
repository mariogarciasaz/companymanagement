from django.contrib import admin
from management.models import Employee, Invoice, Product

# Register your models here.


admin.site.register(Employee)
admin.site.register(Invoice)
admin.site.register(Product)