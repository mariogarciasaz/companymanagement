from django.db import models


#This model is for clients datas
class Client(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name='Name')
    last_name = models.CharField(max_length=100, blank=False, null=True, verbose_name='Last Name')
    full_name = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name='Full Name')
    ci = models.CharField(max_length=100, blank=False, null=True, verbose_name='Cedula de Identidad')
    rif = models.CharField(max_length=100, blank=True, null=True, verbose_name='Registro unico de Informacion Fiscal')
    address = models.CharField(max_length=100, blank=False, null=True, verbose_name='Address')
    phone = models.CharField(max_length=100, blank=False, null=True, verbose_name='Phone')
    email = models.EmailField(max_length=100, blank=False, null=True, verbose_name='Email')
    others_datas = models.CharField(max_length=100, blank=True, null=True, verbose_name='Others Datas')


    #This function return name and last name
    def __str__(self):
        return self.name + ' ' + self.last_name
    

    #This class creates the model in the database
    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['-id']


