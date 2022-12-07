from django.db import models

# Create your models here.
class PatientDetails(models.Model):
    # iterable
    ELIGIBILITY_CHOICES =(
        ("yes", "Yes"),
        ("no", "No")
    )
    patient_id = models.CharField(max_length = 20)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    insurance_eligibility = models.CharField(choices = ELIGIBILITY_CHOICES,max_length=3)
    created_date = models.DateTimeField()

    class Mata:
        db_table = 'patent_details'
