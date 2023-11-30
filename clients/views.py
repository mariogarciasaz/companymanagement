from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from clients.models import Client
from clients.forms import ClientForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin




class ClientListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Client
    template_name = 'clients_list.html'
    context_object_name = 'clients'
    login_url = 'website:login'
    permission_required = 'clients.view_client'


    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(ci__icontains=search_query) |
                Q(rif__icontains=search_query) |
                Q(address__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(email__icontains=search_query)
            )
        return queryset





#This class creates a client in the database
class AddClient(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'add_client.html'
    success_url = reverse_lazy('clients:clients')
    login_url = 'website:login'
    permission_required = 'clients.add_client'

    def form_valid(self, form):
        form.instance.full_name = form.instance.name + ' ' + form.instance.last_name
        return super().form_valid(form)



#This class update a client in the database
class UpdateClient(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'edit_client.html'
    success_url = reverse_lazy('clients:clients')
    login_url = 'website:login'
    permission_required = 'clients.change_client'

    def form_valid(self, form):
        form.instance.full_name = form.instance.name + ' ' + form.instance.last_name
        return super().form_valid(form)


#This class delete a client in the database
class DeleteClient(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('clients:clients')
    login_url = 'website:login'
    permission_required = 'clients.delete_client'