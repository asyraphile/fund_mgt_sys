from django.test import TestCase
from .models import Fund
import uuid
# Create your tests here.

class FundTestCase(TestCase):
    def set_up(self):
        Fund.objects.create(id=uuid.uuid4,
                            name="Pension Fund for test",
                            manager_name="Alice Chee",
                            description="Pension fund created for unit test",
                            nav=190000,
                            performance=5.55,
                            created_at='2025-02-01')
        
    def test_fund_creation(self):
        fund = Fund.objects.get(name="Pension Fund for test")
        self.assertIsNotNone(fund)
    
    def test_fund_field_values(self):
        fund = Fund.objects.get(name="Pension Fund for test")
        self.assertEqual(fund.manager_name, "Alice Chee")
        self.assertEqual(fund.description, "Pension fund created for unit test")
        self.assertEqual(fund.nav, 190000)
        self.assertEqual(fund.performance, 5.55)
        self.assertEqual(str(fund.created_at), '2025-02-01')

    def test_fund_str_representation(self):
        fund = Fund.objects.get(name="Pension Fund for test")
        self.assertEqual(str(fund), "Pension Fund for test")    
