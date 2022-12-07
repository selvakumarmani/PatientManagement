from django.db import models

# Create your models here.

class BulkUpload(models.Model):
    # iterable
    # STATUS_CHOICES =(
    #     ("initiated", "initiated"),
    #     ("processing", "processing"),
    #     ("completed", "completed")
    # )
    status = models.CharField(max_length=15)
    created_date = models.DateTimeField()
    file_name = models.CharField(max_length=30,blank=True,null=True)
    total_records = models.IntegerField()
    total_created = models.IntegerField(blank=True,null=True)
    total_errors = models.IntegerField(blank=True,null=True)

    class Mata:
        db_table = 'bulk_upload'