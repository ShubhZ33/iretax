import unittest
from iretax.rebate_calculator import RebateCalculator

class TestRebateCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator_single = RebateCalculator(['SP', 'ATCS', 'RTCS', 'BTCSP'])
        self.calculator_married = RebateCalculator(['MP', 'ATCM', 'RTCJ', 'BTCOPB'])

    def test_calculate_rebate_single(self):
        expected_rebate = 1775 + 245 + 500 + 1650  # Sum of the rebates for single codes
        actual_rebate = self.calculator_single.calculate_rebate()
        self.assertEqual(expected_rebate, actual_rebate)

    def test_calculate_rebate_married(self):
        expected_rebate = 3550 + 490 + 1000 + 1650  # Sum of the rebates for married codes
        actual_rebate = self.calculator_married.calculate_rebate()
        self.assertEqual(expected_rebate, actual_rebate)

    def test_check_exclusive_codes_error(self):
        with self.assertRaises(ValueError):
            RebateCalculator(['SP', 'ATCS', 'RTCS', 'BTCSP', 'MP', 'ATCM', 'RTCJ', 'BTCOPB']).calculate_rebate()

if __name__ == '__main__':
    unittest.main()

