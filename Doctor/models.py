from django.db import models

class Doctor(models.Model):
    DESIGNATION_CHOICES = [
        ('MO', 'Medical Officer'),
        ('C', 'Consultant'),
        ('SC', 'Sr. Consultant'),
    ]
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=2, choices=DESIGNATION_CHOICES)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    visit_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
