# iretax
iretax

iretax is a Python-based library designed specifically for the Ireland tax system. It serves as a comprehensive tool for individuals, tax professionals, and software developers in Ireland seeking a reliable, easy-to-use solution for tax-related computations for the 2023 tax year.

The iretax library provides a simplified approach to calculating taxes and rebates in Ireland. It features two main components: TaxCalculator and RebateCalculator. The TaxCalculator class offers functionality to calculate taxes based on factors such as income and marital status, aligning with the 2023 tax brackets and rates. The RebateCalculator class aids users in determining the applicable tax rebates, encompassing various eligibility codes specific to the Ireland tax system.

The advantage of using iretax is that it converts complex tax calculations into a few straightforward function calls. This accessibility makes tax calculations comprehensible to everyone, while ensuring accuracy and adherence to the current Irish tax codes, thereby minimizing potential errors in manual calculations.



## Installation

The iretax package can be easily installed from TestPyPI by running the following command:

```shell
pip install iretax
```

Usage
=====

Tax Calculator
--------------

The `TaxCalculator` class forms the core of the iretax package. It is responsible for calculating the tax based on an individual's income and marital status. 

The `TaxCalculator` class is specifically designed to handle various tax scenarios for different types of taxpayers in Ireland. It is informed by the specific tax bands applicable in Ireland for the year 2023 and is well equipped to handle a wide array of scenarios such as being a single parent, both partners earning, and so on.

While the class does not calculate PRSI, given its dependence on other factors such as type of employment and PRSI class, it does a stellar job in calculating PAYE and Universal Social Charge (USC) based on the income slabs.

Here's a quick overview of how to use the `TaxCalculator` class:
Example 1: Single Individual without children

In this scenario, let's consider an individual who is single without children and earns €70,000 per annum.

```python
from iretax import TaxCalculator

# Creating a tax calculator for a single individual earning €70,000 annually
calculator_single = TaxCalculator(70000, 'single')

# Calculating the tax for the single individual
tax_deducted_single = calculator_single.calculate_tax()
print(f'Total tax deducted for the single individual: {tax_deducted_single}')

# Calculating the net annual and monthly income for the single individual
net_annual_income_single, net_monthly_income_single = calculator_single.calculate_net_income()
print(f'Net annual income for the single individual: {net_annual_income_single}')
print(f'Net monthly income for the single individual: {net_monthly_income_single}')
```
Example 2: Married Couple both earning

In this scenario, let's consider a married couple where both partners are earning. The primary earner makes €80,000 annually, and the secondary earner makes €25,000 annually.

```python
from iretax import TaxCalculator

# Creating a tax calculator for the primary earner in a married couple where both are earning
calculator_married_primary = TaxCalculator(80000, 'married', both_earning=True)

# Calculating the tax for the primary earner
tax_deducted_married_primary = calculator_married_primary.calculate_tax()
print(f'Total tax deducted for the primary earner: {tax_deducted_married_primary}')

# Calculating the net annual and monthly income for the primary earner
net_annual_income_married_primary, net_monthly_income_married_primary = calculator_married_primary.calculate_net_income()
print(f'Net annual income for the primary earner: {net_annual_income_married_primary}')
print(f'Net monthly income for the primary earner: {net_monthly_income_married_primary}')

# Creating a tax calculator for the secondary earner in a married couple where both are earning
calculator_married_secondary = TaxCalculator(25000, 'married', both_earning=True)

# Calculating the tax for the secondary earner
tax_deducted_married_secondary = calculator_married_secondary.calculate_tax()
print(f'Total tax deducted for the secondary earner: {tax_deducted_married_secondary}')

# Calculating the net annual and monthly income for the secondary earner
net_annual_income_married_secondary, net_monthly_income_married_secondary = calculator_married_secondary.calculate_net_income()
print(f'Net annual income for the secondary earner: {net_annual_income_married_secondary}')
print(f'Net monthly income for the secondary earner: {net_monthly_income_married_secondary}')

```

Let's delve deeper into the TaxCalculator class:

Upon initialization, the TaxCalculator class takes in the income, marital status, and optional parameters indicating if both partners are earning and if the taxpayer is a single parent.

The calculate_tax() method is used to compute the PAYE based on the individual's income and marital status. Different tax bands are used depending on the marital status and other factors. For instance, a single person without children will be taxed at 20% up to €40,000 and 40% for income exceeding this amount.

The calculate_usc() method calculates the Universal Social Charge. The USC is a tax on income that is charged on a staggered basis. The exact computation depends on the income slab that the individual falls into.

Finally, the calculate_net_income() method computes the net income (annual and monthly) after tax deductions.

By offering an easy-to-use and intuitive interface for tax calculations, the TaxCalculator class simplifies the process of estimating tax deductions and net income for individuals in Ireland.

Sources: Revenue.ie, Citizens Information

## Rebate Calculator
The RebateCalculator class forms a core part of the iretax package. It is responsible for calculating potential tax rebates based on the tax codes applicable to an individual's situation. These tax codes are defined by the specific circumstances of an individual, such as their marital status, the presence of dependents, the age of the taxpayer, and several other factors.

The RebateCalculator class is designed to handle a variety of tax scenarios relevant to individuals in Ireland. It works by matching the applicable rebate codes to their corresponding monetary values, and then adding these up to provide a total rebate amount.

This calculator can handle a wide array of scenarios such as being a single parent, having both partners earning, being a widowed person, and many more, offering a comprehensive and accessible way for individuals to estimate their potential tax rebates.

Here's a quick overview of how to use the RebateCalculator class:

Example 1: Single Individual with Employee PAYE Tax Credit (EPTC) and Age Tax Credit (ATCS)

In this scenario, let's consider an individual who is single, eligible for the Employee PAYE Tax Credit, and the Age Tax Credit.

```python
from iretax import RebateCalculator

# Creating a rebate calculator for a single individual with 'SP', 'EPTC', 'ATCS' rebates
rebate_calculator_single = RebateCalculator(['SP', 'EPTC', 'ATCS'])

# Calculating the total rebates for the single individual
total_rebate_single = rebate_calculator_single.calculate_rebate()
print(f'Total rebate for the single individual: {total_rebate_single}')
```

Example 2: Married Couple with Age Tax Credit (ATCM), Home Carer's Tax Credit (HCTC), and Blind Tax Credit for one partner (BTCOPB)

In this scenario, let's consider a married couple where both partners are eligible for the Age Tax Credit, Home Carer's Tax Credit, and one of the partners is eligible for the Blind Tax Credit.

```python
from iretax import RebateCalculator

# Creating a rebate calculator for a married couple with 'MP', 'ATCM', 'HCTC', 'BTCOPB' rebates
rebate_calculator_married = RebateCalculator(['MP', 'ATCM', 'HCTC', 'BTCOPB'])

# Calculating the total rebates for the married couple
total_rebate_married = rebate_calculator_married.calculate_rebate()
print(f'Total rebate for the married couple: {total_rebate_married}')
```
Exclusiveness
The RebateCalculator class uses the following exclusive codes:

```python
EXCLUSIVE_CODES = {
    'single': ['SP', 'ATCS', 'RTCS', 'BTCSP'],
    'married': ['MP', 'ATCM', 'RTCJ', 'BTCOPB', 'BTCBPB']
}
```
These codes ensure that certain tax rebates, which are mutually exclusive, are not claimed simultaneously. For example, a person cannot claim both the Single Person ('SP') rebate and the Married Person ('MP') rebate also  Rent Tax Credit - single person (max)(RTCS)  Rent Tax Credit - jointly assessed married couple or civil partners (max)(RTCJ).

The exclusivity is checked in the _check_exclusive_codes() method. This function compares the provided rebate codes against the exclusive codes. If it finds any overlap between the 'single' and 'married' sets of codes, it raises a ValueError, indicating that one cannot qualify for both single and married rebate codes.

This design makes the RebateCalculator class an effective and reliable tool for individuals seeking to estimate their potential tax rebates while respecting the exclusive nature of certain tax rebate codes.


## Key Features:
1) A specialized tool designed specifically for the Ireland tax system for the 2023 tax year.
2) Simplifies tax and rebate calculations, supporting a wide range of tax scenarios.
3) Regular updates ensure alignment with the latest Ireland tax codes.
4) Highly customizable and easy to integrate into other software applications.
5) User-friendly interface with well-documented functions for easy usage.
6) iretax is more than just a tool for simplifying tax calculations. It's an invaluable asset for those seeking to better understand and control their tax computations in Ireland. Simplify your tax computation process with iretax today!

## Contributing
We welcome contributions to the iretax package! Here's how you can contribute:

Bug Reports: If you encounter any bugs or issues, please open a new issue on our GitHub page detailing the problem you've experienced.
Feature Requests: If you have ideas for new features or improvements, don't hesitate to open a new issue for discussion.
Pull Requests: If you've implemented a bugfix or feature yourself, please submit a pull request so we can review your contribution and merge it into the project.
When you submit a pull request, please ensure your code adheres to our coding standards and that all tests pass.

## License
iretax is licensed under the MIT license, a permissive license that's commonly used in open-source software. We encourage the use, modification, and distribution of our code, in the spirit of collaboration and the advancement of knowledge.

In keeping with the terms of the MIT license, you're free to use iretax in your own projects, whether they're personal, commercial, or otherwise. The only requirement is to include the same MIT license in your project and give appropriate credit.

However, while the license does not place much restriction on how you can use the software, it's important to remember that iretax comes with no warranty. It's provided "as is," and any express or implied warranties, including the implied warranties of merchantability and fitness for a particular purpose, are disclaimed.

For the full terms, please see the LICENSE file included in our GitHub repository. Enjoy using iretax and we can't wait to see what you build with it!



