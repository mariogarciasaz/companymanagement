import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from management.models import *
from jobs.models import *
from collections import Counter, defaultdict
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages




class Login(LoginView):
    template_name = 'login.html'
    fields = ['username', 'password']
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('website:index')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)


class Index(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'
    login_url = 'website:login'
    context_object_name = 'index'

    def state_jobs(self):
        pending_jobs = []
        finished_jobs = []
        year = datetime.datetime.now().year
        list_jobs = Job.objects.all()

        for job in list_jobs:
            if job.state == 'En Curso' and job.start_date.year == year :
                pending_jobs.append(job)
            elif job.state == 'Finalizado' and job.start_date.year == year :
                finished_jobs.append(job)
        
        total_pending_jobs = len(pending_jobs)
        total_finished_jobs = len(finished_jobs)

        return total_pending_jobs, total_finished_jobs


    
    def sales_per_month(self):
        january = []
        february = []
        march = []
        april = []
        may = []
        june = []
        july = []
        august = []
        september = []
        october = []
        november = []
        december = []

        year = datetime.datetime.now().year
        list_invoices = Invoice.objects.all()

        for invoice in list_invoices:
            if invoice.invoice_date.month == 1 and invoice.invoice_date.year == year and invoice.paid == True:
                january.append(invoice.total)
            elif invoice.invoice_date.month == 2 and invoice.invoice_date.year == year and invoice.paid == True:
                february.append(invoice.total)
            elif invoice.invoice_date.month == 3 and invoice.invoice_date.year == year and invoice.paid == True:
                march.append(invoice.total)
            elif invoice.invoice_date.month == 4 and invoice.invoice_date.year == year and invoice.paid == True:
                april.append(invoice.total)
            elif invoice.invoice_date.month == 5 and invoice.invoice_date.year == year and invoice.paid == True:
                may.append(invoice.total)
            elif invoice.invoice_date.month == 6 and invoice.invoice_date.year == year and invoice.paid == True:
                june.append(invoice.total)
            elif invoice.invoice_date.month == 7 and invoice.invoice_date.year == year and invoice.paid == True:
                july.append(invoice.total)
            elif invoice.invoice_date.month == 8 and invoice.invoice_date.year == year and invoice.paid == True:
                august.append(invoice.total)
            elif invoice.invoice_date.month == 9 and invoice.invoice_date.year == year and invoice.paid == True:
                september.append(invoice.total)
            elif invoice.invoice_date.month == 10 and invoice.invoice_date.year == year and invoice.paid == True:
                october.append(invoice.total)
            elif invoice.invoice_date.month == 11 and invoice.invoice_date.year == year and invoice.paid == True:
                november.append(invoice.total)
            elif invoice.invoice_date.month == 12 and invoice.invoice_date.year == year and invoice.paid == True:
                december.append(invoice.total)

        total_january = sum(january)
        total_february = sum(february)
        total_march = sum(march)
        total_april = sum(april)
        total_may = sum(may)
        total_june = sum(june)
        total_july = sum(july)
        total_august = sum(august)
        total_september = sum(september)
        total_october = sum(october)
        total_november = sum(november)
        total_december = sum(december)

        return total_january, total_february, total_march, total_april, total_may, total_june, total_july, total_august, total_september, total_october, total_november, total_december

    def last_jobs(self):

        list_jobs = Job.objects.order_by('-id')[:6]
        pending_jobs = []

        for job in list_jobs:
            if job.finished == False:
                pending_jobs.append(job)

        return pending_jobs
    


    def products_without_stock(self):

        list_products = Product.objects.all()
        products_without_stock = []

        for product in list_products:
            if product.quantity <= 10:
                products_without_stock.append(product)

        return products_without_stock[:5]


    def total_charged(self):
        current_year = datetime.datetime.now().year
        list_invoices = Invoice.objects.all()
        total_charged = []

        for invoice in list_invoices:
            if invoice.invoice_date.year == current_year:
                total_charged.append(invoice.total)

        total_invoices_charged_abs = sum(total_charged)

        return total_invoices_charged_abs
    

    def top_cars(self):
        all_cars = Job.objects.all()

        dict_cars = {}

        for car in all_cars:
            if car.car not in dict_cars:
                dict_cars[car.car] = 0
            dict_cars[car.car] += 1
            
        sorted_cars = dict(sorted(dict_cars.items(), key=lambda item:item[1], reverse=True))

        top_5_cars = list(sorted_cars.items())[:5]


        return top_5_cars
        
        


    def last_invoices(self):
        list_invoices = list(Invoice.objects.order_by('-id')[0:5])
        return list_invoices


    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context = {
            'total_pending_jobs' : self.state_jobs()[0],
            'total_finished_jobs' : self.state_jobs()[1],
            'total_january' : self.sales_per_month()[0],
            'total_february' : self.sales_per_month()[1],
            'total_march' : self.sales_per_month()[2],
            'total_april' : self.sales_per_month()[3],
            'total_may' : self.sales_per_month()[4],
            'total_june' : self.sales_per_month()[5],
            'total_july' : self.sales_per_month()[6],
            'total_august' : self.sales_per_month()[7],
            'total_september' : self.sales_per_month()[8],
            'total_october' : self.sales_per_month()[9],
            'total_november' : self.sales_per_month()[10],
            'total_december' : self.sales_per_month()[11],
            'pending_jobs' : self.last_jobs(),
            'products_without_stock' : self.products_without_stock(),
            'total_charged_abs' : self.total_charged(),
            'top_5_cars' : self.top_cars(),
            'list_invoices' : self.last_invoices(),
        }
        return context
    
