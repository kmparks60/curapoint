from django.test import TestCase
from medications.models import Prescription
from users.models import CustomUser
from django.utils import timezone



class PrescriptionTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.customer = CustomUser.objects.create_user(
            username = "Test User",
            email = "test@pharmacy.com",
            password = "password"
        )

        cls.prescription = Prescription.objects.create(
            medication_name = "Aspirin",
            dosage = "500mg",
            start_date = timezone.now(),
            end_date = timezone.now() + timezone.timedelta(days=30),
            quantity = 30,
            refills_allowed = 2,
            customer = cls.customer
        )

    def test_prescription_creation(self):
        self.assertEqual(self.prescription.customer, self.customer)
        self.assertEqual(self.prescription.medication_name, "Aspirin")
        self.assertEqual(self.prescription.dosage, "500mg")
        self.assertEqual(self.prescription.quantity, 30)
        self.assertTrue(self.prescription.start_date < self.prescription.end_date)
        self.assertEqual(self.prescription.refills_allowed, 2)