import unittest
from iretax.tax_calculator import TaxCalculator  # assuming the class is in tax_calculator.py

class TestTaxCalculator(unittest.TestCase):

    def test_calculate_tax_single(self):
        calculator = TaxCalculator(43200, 'single')
        tax_deducted = calculator.calculate_tax()
        self.assertEqual(tax_deducted, 9280)  # (40000*0.20) + (3200*0.40)

    def test_calculate_usc_single(self):
        calculator = TaxCalculator(43200, 'single')
        usc_deducted = calculator.calculate_usc()
        self.assertEqual(usc_deducted, 1190.8200000000002)  # Calculated based on the USC bands

    def test_calculate_net_income_single(self):
        calculator = TaxCalculator(43200, 'single')
        net_annual_income, net_monthly_income = calculator.calculate_net_income()
        self.assertEqual(net_annual_income, 32729)  # 43200 - 9280(tax) - 1341(usc), rounded to nearest whole number
        self.assertEqual(net_monthly_income, 2727)  # 32679 / 12, rounded to nearest whole number

if __name__ == '__main__':
    unittest.main()
