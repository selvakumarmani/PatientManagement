from celery import shared_task
from patient.serializer import PatientDetailsSerializer
from rest_framework.exceptions import ValidationError
from file_upload.models import BulkUpload
import pandas as pd
from datetime import datetime
from django.conf import settings
import logging,time
celery_logger = logging.getLogger("celery")

@shared_task
def upload_file(file):
    try:
        celery_logger.debug("upload file 1...........")
        error_list = []
        if file:
            bulk_upload_object = BulkUpload.objects.create(status='initiated',total_records=len(file),total_errors=0,total_created=0,created_date=datetime.now())
            time.sleep(15)
            bulk_upload_object.status = 'processing'
            bulk_upload_object.save()
            time.sleep(20)
            celery_logger.debug("upload file 1.2..........")
            for i in file:
                error_data = {}
                try:
                    serializer_instance = PatientDetailsSerializer(data=i)
                    serializer_instance.is_valid(raise_exception=True)
                    serializer_instance.save()
                except ValidationError as e:
                    error_data = i
                    error_data['reason'] = e
                    error_list.append(error_data)
            # bulk_upload_instance = BulkUpload.objects.get(id=bulk_upload_object.id)
            if error_list:
                file_name = str(bulk_upload_object.id)+'error_file.csv'
                df = pd.DataFrame(error_list) 
                df.to_csv(settings.MEDIA_ROOT + '/'+ file_name,index=False)
                bulk_upload_object.file_name = file_name
            bulk_upload_object.total_errors = len(error_list)
            bulk_upload_object.status = 'completed'
            bulk_upload_object.total_created = len(file) - len(error_list)
            bulk_upload_object.save()
    except Exception as e:
        celery_logger.error("upload file 1...........")