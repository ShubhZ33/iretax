class RebateCalculator:

    REBATES = {
        'SP': 1775,  # Single Person
        'MP': 3550,  # Married Person or Civil Partner
        'WPD': 1775,  # Widowed Person or Surviving Civil Partner with dependent child(ren)
        'WPN': 2315,  # Widowed Person or Surviving Civil Partner without dependent child(ren)
        'WPBY': 3550,  # Widowed Person or Surviving Civil Partner - bereavement year
        'WP1Y': 3600,  # Widowed Parent 1st year after death
        'WP2Y': 3150,  # Widowed Parent 2nd year after death of spouse or civil partner
        'WP3Y': 2700,  # Widowed Parent 3rd year after death of spouse or civil partner
        'WP4Y': 2250,  # Widowed Parent 4th year after death of spouse or civil partner
        'WP5Y': 1800,  # Widowed Parent 5th year after death of spouse or civil partner
        'SPCC': 1650,  # Single Person Child Carer Credit
        'ATCS': 245,  # Age Tax Credit if single, widowed or surviving civil partner
        'ATCM': 490,  # Age Tax Credit if married or in a civil partnership
        'HCTC': 1700,  # Home Carer's Tax Credit (max.)
        'EPCI': 75000,  # Employed Person taking care of an incapacitated individual (max.)
        'EPTC': 1775,  # Employee PAYE Tax Credit
        'EITC': 1775,  # Earned Income Tax Credit (max.)
        'ICTC': 3300,  # Incapacitated Child Tax Credit
        'DR': 245,  # Dependent Relative
        'DRL': 16156,  # Dependent Relative Income Limit
        'BTCSP': 1650,  # Blind Tax Credit - single person
        'BTCOPB': 1650,  # Blind Tax Credit - one spouse or civil partner blind
        'BTCBPB': 3300,  # Blind Tax Credit - both spouses or civil partners blind
        'GDA': 825,  # Guide Dog - allowance
        'RTCS': 500,  # Rent Tax Credit - single person (max)
        'RTCJ': 1000,  # Rent Tax Credit - jointly assessed married couple or civil partners (max)
        'TRSF': 25,  # Tax Rate: Schedule F (WH = Withholding Tax) 25% WH
        'TRSSA': 33,  # Tax Rate: Special Savings Account (SSA) 33%
        'MLDI': 33  # Max. liability on deposit interest 33%
    }

    EXCLUSIVE_CODES = {
        'single': ['SP', 'ATCS', 'RTCS', 'BTCSP'],
        'married': ['MP', 'ATCM', 'RTCJ', 'BTCOPB', 'BTCBPB']
    }

    def __init__(self, rebate_codes):
        self.rebate_codes = rebate_codes

    def _check_exclusive_codes(self):
        single_codes = set(self.rebate_codes) & set(self.EXCLUSIVE_CODES['single'])
        married_codes = set(self.rebate_codes) & set(self.EXCLUSIVE_CODES['married'])
        if single_codes and married_codes:
            raise ValueError('Cannot qualify for both single and married rebate codes.')

    def calculate_rebate(self):
        self._check_exclusive_codes()
        total_rebate = 0
        for code in self.rebate_codes:
            total_rebate += self.REBATES.get(code, 0)
        return total_rebate