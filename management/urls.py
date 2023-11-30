from django.urls import path, include
from management.views import *

urlpatterns = [
    path('invoices/', InvoiceListView.as_view(), name='invoices'),
    path('invoices/add/', AddInvoice.as_view(), name='add_invoice'),
    path('invoices/update/<int:pk>/', UpdateInvoice.as_view(), name='update_invoice'),
    path('invoices/delete/<int:pk>/', DeleteInvoice.as_view(), name='delete_invoice'),
    path('invoices/view/<int:pk>/', ViewInvoice.as_view(), name='view_invoice'),
    path('invoices/pdf/', InvoiceListView.print_pdf, name='pdf_invoice'),
    path('invoices/report/', InvoiceListView.generate_excel_report, name='generate_report'),
    path('get_product_price/<int:product_id>/', get_product_price, name='get_product_price'),
    path('get_client_data/<int:client_id>/', get_client_datas, name='get_client_datas'),
    path('employees/', EmployeeListView.as_view(), name='employees'),
    path('employees/add/', AddEmployee.as_view(), name='add_employee'),
    path('employees/update/<int:pk>/', UpdateEmployee.as_view(), name='update_employee'),
    path('employees/delete/<int:pk>/', DeleteEmployee.as_view(), name='delete_employee'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/add/', AddProduct.as_view(), name='add_product'),
    path('products/update/<int:pk>/', UpdateProduct.as_view(), name='update_product'),
    path('products/delete/<int:pk>/', DeleteProduct.as_view(), name='delete_product'),
    path('category/', CategoryListView.as_view(), name='categories'),
    path('category/add/', AddCategory.as_view(), name='add_category'),
    path('category/update/<int:pk>/', UpdateCategory.as_view(), name='update_category'),
    path('category/delete/<int:pk>/', DeleteCategory.as_view(), name='delete_category'),
]