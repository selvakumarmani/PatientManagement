from django.urls import path
from .views import BulkUploadAPI,bulk_upload_list,error_page

urlpatterns = [
    path('bulk_upload/',BulkUploadAPI.as_view(),name='bulk_upload'),
    path('bulk_upload_list/',bulk_upload_list,name='bulk_upload_list'),
    path('404_page/',error_page,name='error_page'),
]
