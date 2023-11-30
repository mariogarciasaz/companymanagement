from django import forms
from management.models import Employee, Invoice, Product, Category




class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = '__all__'
        widgets = {
            'invoice_date': forms.DateInput(attrs={'type': 'date'}),
            'invoice_due_date': forms.DateInput(attrs={'type': 'date'}),
            
        }




class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'



