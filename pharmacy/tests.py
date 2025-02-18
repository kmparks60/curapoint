from django.test import TestCase
from pharmacy.models import Pharmacy


class PharmacyTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        cls.pharmacy = Pharmacy.objects.create(
            name = "Test Pharmacy",
            location = "Bethlehem, PA",
            contact_info = "test@testpharmacy.com",
            license_number = "123ABC"
        )

    def test_pharmacy_creation(self):
        self.assertEqual(self.pharmacy.name, "Test Pharmacy")
        self.assertEqual(self.pharmacy.location, "Bethlehem, PA")
        self.assertEqual(self.pharmacy.contact_info, "test@testpharmacy.com")
        self.assertEqual(self.pharmacy.license_number, "123ABC")