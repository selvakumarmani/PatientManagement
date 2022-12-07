from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from patient.serializer import PatientDetailsSerializer
from rest_framework.exceptions import ValidationError
from .models import BulkUpload
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .task import upload_file
from django.shortcuts import redirect
from django.conf import settings
# Create your views here.
import logging
celery_logger = logging.getLogger("celery")

class BulkUploadAPI(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self,request):
        return render(request, "bulk_upload.html")

    def post(self,request):
        try:
            file_extension = request.FILES['file'].content_type
            if file_extension == 'text/csv':
                df = pd.read_csv(request.FILES['file'])
                patient_data = df.to_dict(orient="records")
                upload_file.delay(patient_data)
                return redirect('patient_list')
            else:
                return redirect('error_page')
        except Exception as e:
            celery_logger.error(e)

# Create your views here.
def bulk_upload_list(request):
    bulk_upload_data = BulkUpload.objects.all()
    bulk_upload_incompleted = [i for i in bulk_upload_data if i.status != 'completed']
    incompleted_task_count = len(bulk_upload_incompleted)
    context = {
        'data': bulk_upload_data,
        'incompleted_task_count':incompleted_task_count
    }
    return render(request, "bulk_upload_list.html",context)

# Create your views here.
def error_page(request):
    return render(request, "error_page.html")
