from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    pharmacy_name = models.CharField(max_length=255, blank=True, null=True)
    pharmacy_location = models.CharField(max_length=255, blank=True, null=True)
    pharmacy_contact = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')

    # Customer-specific fields
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True)
    # Pharmacy-specific fields
    license_number = models.CharField(max_length=50, blank=True, null=True)
    pharmacy_role = models.CharField(max_length=50, blank=True, null=True)
    # Medical info for customers
    medical_history = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    prescriptions = models.ManyToManyField('medications.Prescription', related_name='patients', blank=True)
    # Tracking for customer orders, prescriptions, etc.
    active_prescriptions_count = models.IntegerField(default=0)
    last_filled_date = models.DateField(null=True, blank=True)
    # Business info for admins and pharmacists
    pharmacy_id = models.ForeignKey('pharmacy.Pharmacy', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"