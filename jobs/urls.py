from django.urls import path, include
from jobs.views import JobListView, AddJob, UpdateJob, DeleteJob


urlpatterns = [
    path('', JobListView.as_view(), name='jobs'),
    path('add_job/', AddJob.as_view(), name='add_job'),
    path('update_job/<int:pk>/', UpdateJob.as_view(), name='update_job'),
    path('delete_job/<int:pk>/', DeleteJob.as_view(), name='delete_job'),
    path('report/', JobListView.generate_excel_report, name='generate_report'),
]

