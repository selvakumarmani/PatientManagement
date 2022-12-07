from rest_framework import serializers
from patient.models import PatientDetails

class PatientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields = '__all__'