from django.db import models
from clients.models import Client
from management.models import Employee

# Create your models here.


class Job(models.Model):
    client = models.ForeignKey(Client, to_field='full_name', blank=False, null=True, on_delete=models.SET_NULL, verbose_name='Client')
    car = models.CharField(max_length=100, blank=False, null=True, verbose_name='Car')
    car_model = models.CharField(max_length=100, blank=False, null=True, verbose_name='Car Model')
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Employee')
    description = models.TextField(blank=False, null=True, verbose_name='Description')
    start_date = models.DateField(blank=False, null=True,  verbose_name='Start Date')
    finished = models.BooleanField(default=False, blank=True, verbose_name='Finished')
    end_date = models.DateField(blank=True, null=True, verbose_name='End Date')
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name='State')

    def __str__(self):
        return self.client
    

    class Meta:
        db_table = 'jobs'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-id']