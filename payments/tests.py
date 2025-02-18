from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from users.models import Profile
from orders.models import Order
from pharmacy.models import Pharmacy
from payments.models import Insurance, Payment


class PaymentTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        cls.user = get_user_model().objects.create_user(
            username = "Test User",
            email = "test@pharmacy.com",
            password = "password"
        )

        cls.profile = Profile.objects.create(
            user = cls.user
        )

        cls.pharmacy = Pharmacy.objects.create(
            name = "Test Pharmacy"
        )

        cls.insurance = Insurance.objects.create(
            customer = cls.profile,
            provider_name = "Aetna",
            policy_number = "ABC123"
        )

        cls.order = Order.objects.create(
            customer = cls.profile,
            pharmacy = cls.pharmacy,
            order_date = timezone.now(),
            status = "Completed",
            total_price = 1000.00,
            tracking_number = "ABC123Track"
        )

        cls.payment = Payment.objects.create(
            order = cls.order,
            customer = cls.profile,
            payment_method = "Cash",
            amount_paid = 37.12,
            payment_status = "Completed",
            payment_date = timezone.now()
        )


    def test_insurance_creation(self):
        self.assertEqual(self.insurance.customer, self.profile)
        self.assertEqual(self.insurance.provider_name, "Aetna")
        self.assertEqual(self.insurance.policy_number, "ABC123")

    def test_payment_creation(self):
        self.assertEqual(self.payment.order, self.order)
        self.assertEqual(self.payment.customer, self.profile)
        self.assertEqual(self.payment.payment_method, "Cash")
        self.assertEqual(self.payment.amount_paid, 37.12)
        self.assertEqual(self.payment.payment_status, "Completed")
        self.assertIsNotNone(self.payment.payment_date)