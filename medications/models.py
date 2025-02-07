from django.db import models
from users.models import CustomUser
from django.utils import timezone


class Prescription(models.Model):
    customer = models.ForeignKey(CustomUser, related_name='prescriptions', on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    quantity = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    refills_allowed = models.IntegerField()
    prescription_date = models.DateField(default=timezone.now)