# Names: Megan Clarke, Colin Eade, Noelle Dacayo
# Date: April 07, 2023
# File Name: testsuite.py
# Description: This is the app that provides a selection menu for each of the test modules.

from os import system
import unittest
from test_m1_new_customer import TestNewCustomer
from test_m2_edit_customer import TestEditCustomer
from test_m3_delete_customer import TestDeleteCustomer
from test_m4_new_account import TestNewAccount
from test_m5_edit_account import TestEditAccount
from test_m6_delete_account import TestDeleteAccount
from test_m7_balance_enquiry import TestBalanceEnquiry
from test_m8_mini_statement import TestMiniStatement
from test_m9_customized_statement import TestCustomizedStatement

# Constants
MAIN_MENU = """
==========
TEST SUITE
==========

Select an option:

1. New Customer
2. Edit Customer
3. Delete Customer
4. New Account
5. Edit Account
6. Delete Account
7. Balance Enquiry
8. Mini Statement
9. Customized Statement

Or press [Enter] to quit
"""

valid = False
# App loop
while not valid:

    # Clr the terminal and print the menu options
    system("cls")
    print(MAIN_MENU)

    selection = input(">")

    # New Customer tests selected
    if selection == "1":
        system("cls")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestNewCustomer)
        unittest.TextTestRunner(verbosity=2).run(suite)
        input("Press [Enter] to continue: ")

    # Edit Customer tests selected
    elif selection == "2":
        system("cls")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestEditCustomer)
        unittest.TextTestRunner(verbosity=2).run(suite)
        input("Press [Enter] to continue: ")

    # Delete Customer tests selected
    elif selection == "3":
        system("cls")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestDeleteCustomer)
        unittest.TextTestRunner(verbosity=2).run(suite)
        input("Press [Enter] to continue: ")

    # New Account tests selected
    elif selection == "4":
        system("cls")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestNewAccount)
        unittest.TextTestRunner(verbosity=2).run(suite)
        input("Press [Enter] to continue: ")

    # Edit Account tests selected
    elif selection == "5":
        system("cls")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestEditAccount)
        unittest.TextTestRunner(verbosity=2).run(suite)
        input("Press [Enter] to continue: ")

    # Delete Account tests selected
    elif selection == "6":
        system("cls")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestDeleteAccount)
        unittest.TextTestRunner(verbosity=2).run(suite)
        input("Press [Enter] to continue: ")

    # Balance Enquiry tests selected
    elif selection == "7":
        system("cls")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestBalanceEnquiry)
        unittest.TextTestRunner(verbosity=2).run(suite)
        input("Press [Enter] to continue: ")

    # Mini Satement tests selected
    elif selection == "8":
        system("cls")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestMiniStatement)
        unittest.TextTestRunner(verbosity=2).run(suite)
        input("Press [Enter] to continue: ")

    # Customized Statement tests selected
    elif selection == "9":
        system("cls")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestCustomizedStatement)
        unittest.TextTestRunner(verbosity=2).run(suite)
        input("Press [Enter] to continue: ")

    else:
        valid = True


