from django.db import models
from orders.models import Order
from users.models import Profile


class Insurance(models.Model):
    
    customer = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="insurance")
    provider_name = models.CharField(max_length=255)
    policy_number = models.CharField(max_length=255)
    coverage_details = models.TextField(blank=True, null=True)
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer.user.username} - {self.provider_name}"
    
class Payment(models.Model):
    
    PAYMENT_METHODS = [
        ('credit card', 'Credit Card'),
        ('debit card', 'Debit Card'),
        ('insurance', 'Insurance'),
        ('cash', 'Cash')
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="payments")
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Order {self.order.id} - {self.payment_status}"