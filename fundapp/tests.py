from django.test import TestCase
from .models import Fund
from decimal import Decimal
from datetime import date
import uuid
# Create your tests here.

class FundTestCase(TestCase):
    test_fund = Fund
    def setUp(self):
        self.test_fund = Fund.objects.create(name="Pension Fund for test",
                                            manager_name="Alice Chee",
                                            description="Pension fund created for unit test",
                                            nav=190000,
                                            performance=5.55,
                                            created_at='2025-02-01')
    """UNIT TESTS FOR MODELS"""    
    def test_fund_creation(self):
        fund = Fund.objects.get(name="Pension Fund for test")
        self.assertIsNotNone(fund)
    
    def test_fund_field_values(self):
        fund = Fund.objects.get(name="Pension Fund for test")
        self.assertEqual(fund.manager_name, "Alice Chee")
        self.assertEqual(fund.description, "Pension fund created for unit test")
        self.assertEqual(fund.nav, 190000)
        self.assertEqual(fund.performance, Decimal("{:.2f}".format(5.55)))
        self.assertEqual(fund.created_at, date.today())

    def test_fund_str_representation(self):
        fund = Fund.objects.get(name="Pension Fund for test")
        self.assertEqual(str(fund), "Pension Fund for test") 
    """UNIT TESTS FOR VIEWS/API"""  
    def test_view_list(self):
        response = self.client.get('/all/')
        # asserting the response status code to 200.
        self.assertEqual(response.status_code, 200) 

    def test_view_retrieve(self):
        response = self.client.get(f'/fund/{str(self.test_fund.id)}/')
        # asserting the response status code to 200.
        self.assertEqual(response.status_code, 200) 
        # asserting self test fund's name to response's name
        self.assertEqual(response.json()['name'], self.test_fund.name)

    def test_view_put(self):
        # updating description by concatenating 1 at the back, performance has to be in 2 decimal places
        # in models.py I set this to have a default 2 decimal places
        performance_2d = "%.2f" % 10.50
        updated_data = {
            'performance':performance_2d,
        }
        response = self.client.put(f'/update_performance/{str(self.test_fund.id)}/',
                                   updated_data,
                                   content_type='application/json'
                                   )
        # asserting the response status code to 200.
        self.assertEqual(response.status_code, 200) 
        # asserting self test fund's name to response's name
        self.assertEqual(response.json()['performance'], str(updated_data['performance']))

    def test_view_delete(self):
        response = self.client.delete(f'/delete/{str(self.test_fund.id)}/')
        # asserting the response status code to 200.
        self.assertEqual(response.status_code, 200) 