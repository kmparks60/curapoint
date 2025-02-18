import datetime
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from medications.models import Prescription
from orders.models import Order, OrderItem
from pharmacy.models import Pharmacy
from users.models import Profile


class OrderTest(TestCase):

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

        cls.order = Order.objects.create(
            customer = cls.profile,
            pharmacy = cls.pharmacy,
            order_date = timezone.now(),
            status = "Completed",
            total_price = 1000.00,
            tracking_number = "ABC123Track"
        )

        cls.prescription = Prescription.objects.create(
            customer=cls.user,
            medication_name="Amoxicillin",
            dosage="500mg",
            quantity=30,
            start_date=datetime.date(2025, 3, 1),
            end_date=datetime.date(2025, 6, 1),
            refills_allowed=2
        )

        cls.order.prescriptions.add(cls.prescription)

        cls.order_item = OrderItem.objects.create(
            order = cls.order,
            prescription = cls.prescription,
            quantity = 20,
            price = 1000.00
        )

    def test_order_creation(self):
        self.assertEqual(self.order.customer, self.profile)
        self.assertEqual(self.order.pharmacy, self.pharmacy)
        self.assertIn(self.prescription, self.order.prescriptions.all())
        self.assertIsNotNone(self.order.order_date)
        self.assertEqual(self.order.status, "Completed")
        self.assertAlmostEqual(self.order.total_price, 1000.00, places=2)
        self.assertEqual(self.order.tracking_number, "ABC123Track")

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.prescription, self.prescription)
        self.assertEqual(self.order_item.quantity, 20)
        self.assertAlmostEqual(self.order_item.price, 1000.00, places=2)