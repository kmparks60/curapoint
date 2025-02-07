from django.db import models


class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    license_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name