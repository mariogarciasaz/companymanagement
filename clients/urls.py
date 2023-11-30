from django.urls import path, include
from clients.views import ClientListView, AddClient, UpdateClient, DeleteClient

urlpatterns = [
    path('', ClientListView.as_view(), name='clients'),
    path('add_client/', AddClient.as_view(), name='add_client'),
    path('update_client/<int:pk>/', UpdateClient.as_view(), name='update_client'),
    path('delete_client/<int:pk>/', DeleteClient.as_view(), name='delete_client'),
]