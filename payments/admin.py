from django.contrib import admin
from .models import Payment, Insurance

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_method', 'amount_paid', 'payment_status', 'payment_date')
    list_filter = ('payment_status', 'payment_method', 'payment_date')
    search_fields = ('order__id', 'customer__user__username', 'transaction_id')

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Insurance)