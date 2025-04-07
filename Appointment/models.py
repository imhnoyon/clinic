from django.db import models
from django.db import models
from Doctor.models import Doctor

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name
