from django.db import models
from django.utils import timezone
from users.models import Profile
from medications.models import Prescription
from pharmacy.models import Pharmacy


class Order(models.Model):
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]

    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="orders")
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name="orders")
    prescriptions = models.ManyToManyField(Prescription, related_name="orders", blank=True)
    order_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tracking_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer.user.username} ({self.status})"
    
class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item in Order {self.order.id} - {self.prescription}"