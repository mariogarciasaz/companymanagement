from django.db import models
from clients.models import Client
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name='Name')
    last_name = models.CharField(max_length=100, blank=False, null=True, verbose_name='Last Name')
    category = models.CharField(max_length=100, blank=False, null=True, verbose_name='Category')

    def __str__(self):
        return f"{self.name + ' ' + self.last_name}"
    

    class Meta:
        db_table = 'employees'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['-id']




class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, unique=True, verbose_name='Name')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']



class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, unique=True, verbose_name='Name')
    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.SET_NULL, verbose_name= 'Category')
    price = models.DecimalField(max_digits=50, decimal_places=2, blank=False, null=True, unique=False, verbose_name='Price')
    quantity = models.IntegerField(blank=False, null=True, verbose_name='Quantity')
    description = models.TextField(max_length=100, blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['category']


class Invoice(models.Model):

    #Client datas
    client = models.ForeignKey(Client, to_field='id', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Client')
    client_address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Client Address')
    client_email = models.EmailField(max_length=100, blank=True, null=True, verbose_name='Client Email')
    client_phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='Client Phone')
    client_car = models.CharField(max_length=100, blank=True, null=True, verbose_name='Car')
    client_car_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='Car Model')

    #Invoice datas
    invoice_number = models.CharField(max_length=100, blank=True, null=True, verbose_name='Invoice Number')
    invoice_date = models.DateField(blank=False, null=True,  verbose_name='Invoice Date')
    invoice_due_date = models.DateField(blank=False, null=True, verbose_name='Invoice Due Date')
    paid = models.BooleanField(blank=True, null=False, default=False, verbose_name='Paid')
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name='State')

    #Job datas

    #Line 1
    line_one = models.ForeignKey(Product, blank= True, null=True, on_delete=models.SET_NULL, default='', verbose_name='Line 1', related_name='line_one')
    line_one_quantity = models.IntegerField('Quantity', blank= True, null= True, default=0)
    line_one_unit_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    line_one_total_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)

    #Line 2
    line_two = models.ForeignKey(Product,blank= True, null=True, on_delete=models.SET_NULL, default='', verbose_name='Line 2', related_name='line_two')
    line_two_quantity = models.IntegerField('Quantity', blank= True, null= True, default=0)
    line_two_unit_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    line_two_total_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    
    #Line 3
    line_three = models.ForeignKey(Product,blank= True, null=True, on_delete=models.SET_NULL, default='', verbose_name='Line 3', related_name='line_three')
    line_three_quantity = models.IntegerField('Quantity', blank= True, null= True, default=0)
    line_three_unit_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    line_three_total_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)

    #Line 4
    line_four = models.ForeignKey(Product, blank= True, null=True, on_delete=models.SET_NULL, default='', verbose_name='Line 4', related_name='line_four')
    line_four_quantity = models.IntegerField('Quantity', blank= True, null= True, default=0)
    line_four_unit_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    line_four_total_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)

    #Line 5
    line_five = models.ForeignKey(Product, blank= True, null=True, on_delete=models.SET_NULL, default='', verbose_name='Line 5', related_name='line_five')
    line_five_quantity = models.IntegerField('Quantity', blank= True, null= True, default=0)
    line_five_unit_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    line_five_total_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)

    #Line 6
    line_six = models.ForeignKey(Product, blank= True, null=True, on_delete=models.SET_NULL, default='', verbose_name='Line 6', related_name='line_six')
    line_six_quantity = models.IntegerField('Quantity', blank= True, null= True, default=0)
    line_six_unit_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    line_six_total_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)

    #Line 7
    line_seven = models.ForeignKey(Product, blank= True, null=True, on_delete=models.SET_NULL, default='', verbose_name='Line 7', related_name='line_seven')
    line_seven_quantity = models.IntegerField('Quantity', blank= True, null= True, default=0)
    line_seven_unit_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    line_seven_total_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)

    #Line 8
    line_eight = models.ForeignKey(Product, blank= True, null=True, on_delete=models.SET_NULL, default='', verbose_name='Line 8', related_name='line_eight')
    line_eight_quantity = models.IntegerField('Quantity', blank= True, null= True, default=0)
    line_eight_unit_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    line_eight_total_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)

    #Line 9
    line_nine = models.ForeignKey(Product, blank= True, null=True, on_delete=models.SET_NULL, default='', verbose_name='Line 9', related_name='line_nine')
    line_nine_quantity = models.IntegerField('Quantity', blank= True, null= True, default=0)
    line_nine_unit_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    line_nine_total_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)

    #Line 10
    line_ten = models.ForeignKey(Product, blank= True, null=True, on_delete=models.SET_NULL, default='', verbose_name='Line 10', related_name='line_ten')
    line_ten_quantity = models.IntegerField('Quantity', blank= True, null= True, default=0)
    line_ten_unit_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)
    line_ten_total_price = models.DecimalField(max_digits=50, decimal_places=2, blank= True, null= True, default=0)

    #Invoice Totals

    subtotal = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True, verbose_name='Subtotal')
    discount = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True, verbose_name='Discount')
    vat = models.IntegerField(blank=True, null=True, verbose_name='VAT')
    total = models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True, verbose_name='Total')


    def __str__(self):
        return f"{self.invoice_number + '-' + self.client + '-' + self.invoice_date}"
    

    class Meta:
        db_table = 'invoices'
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        ordering = ['-invoice_number']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.line_one_id:
            product1 = Product.objects.get(id=self.line_one_id)
            self.line_one_unit_price = product1.price
        elif self.line_two_id:
            product2 = Product.objects.get(id=self.line_two_id)
            self.line_two_unit_price = product2.price
        elif self.line_three_id:
            product3 = Product.objects.get(id=self.line_three_id)
            self.line_three_unit_price = product3.price
        elif self.line_four_id:
            product4 = Product.objects.get(id=self.line_four_id)
            self.line_four_unit_price = product4.price
        elif self.line_five_id:
            product5 = Product.objects.get(id=self.line_five_id)
            self.line_five_unit_price = product5.price
        elif self.line_six_id:
            product6 = Product.objects.get(id=self.line_six_id)
            self.line_six_unit_price = product6.price
        elif self.line_seven_id:
            product7 = Product.objects.get(id=self.line_seven_id)
            self.line_seven_unit_price = product7.price
        elif self.line_eight_id:
            product8 = Product.objects.get(id=self.line_eight_id)
            self.line_eight_unit_price = product8.price
        elif self.line_nine_id:
            product9 = Product.objects.get(id=self.line_nine_id)
            self.line_nine_unit_price = product9.price
        elif self.line_ten_id:
            product10 = Product.objects.get(id=self.line_ten_id)
            self.line_ten_unit_price = product10.price

        super().save(*args, **kwargs)
    



def update_unit_price(sender, instance, **kwargs):
    product_attributes = [
        'line_one', 'line_two', 'line_three', 'line_four', 'line_five',
        'line_six', 'line_seven', 'line_eight', 'line_nine', 'line_ten'
    ]
    
    for attr in product_attributes:
        product = getattr(instance, attr)
        if product is not None and hasattr(product, 'price'):
            setattr(instance, f'{attr}_unit_price', product.price)


