# Names: Megan Clarke, Colin Eade, Noelle Dacayo
# Date: April 07, 2023
# File Name: test_m3_delete_customer.py
# Description: All tests for the Delete Customer Module

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep

# set up the main class
class TestDeleteCustomer(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.maxDiff = None
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.get("https://demo.guru99.com/V4/index.php")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr491421")
        self.driver.find_element(By.NAME, "password").send_keys("mYdAqyj")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.get("https://demo.guru99.com/V4/manager/DeleteCustomerInput.php")

    def teardown(self):
        self.driver.quit()

    # test customer ID field
    def test_dc01(self):
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Customer ID cannot be blank"
        except AssertionError:
            print("Test DC01 failed: Error text is not 'Customer ID cannot be blank'\n")
            raise
        else:
            print("Test DC01 passed: Error text is 'Customer ID cannot be blank'\n")

    def test_dc02_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Characters are not allowed"
        except AssertionError:
            print("Test DC02.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test DC02.1 passed: Error text is 'Characters are not allowed'\n")

    def test_dc02_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Characters are not allowed"
        except AssertionError:
            print("Test DC02.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test DC02.2 passed: Error text is 'Characters are not allowed'\n")

    def test_dc03_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Special characters are not allowed"
        except AssertionError:
            print("Test DC03.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test DC03.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_dc03_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Special characters are not allowed"
        except AssertionError:
            print("Test DC03.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test DC03.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_dc04(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Characters are not allowed"
        except AssertionError:
            print("Test DC04 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test DC04 passed: Error text is 'Characters are not allowed'\n")

    def test_dc05(self):
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.SPACE, "12345")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "First character cannot have space"
        except AssertionError:
            print("Test DC05 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test DC05 passed: Error text is 'First character cannot have space'\n")

    # test submit button
    def test_dc06(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.switch_to.alert.accept()
        try:
            assert self.driver.switch_to.alert.text == "Customer does not exist!!"
        except AssertionError:
            print("Test DC06 failed: Alert text is not 'Customer does not exist!!'\n")
            raise
        else:
            print("Test DC06 passed: Alert text is 'Customer does not exist!!'\n")

    def test_dc07(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.switch_to.alert.accept()
        try:
            assert self.driver.switch_to.alert.text == "Customer could not be deleted!!. First delete all accounts of " \
                                                       "this customer then delete the customer"
        except AssertionError:
            print("Test DC07 failed: Alert text is not 'Customer could not be deleted!!. First delete all accounts of "
                  "this customer then delete the customer'\n")
            raise
        else:
            print("Test DC07 passed: Alert text is 'Customer could not be deleted!!. First delete all accounts of "
                  "this customer then delete the customer'\n")

    # test reset button
    def test_dc08_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("qwer")
        self.driver.find_element(By.NAME, "res").click()
        try:
            assert self.driver.find_element(By.NAME, "cusid").text == ""
        except AssertionError:
            print("Test DC08.1 failed: Reset button does not empty customer ID field\n")
            raise
        else:
            print("Test DC08.1 passed: Reset button empties customer ID field\n")

    def test_dc08_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        self.driver.find_element(By.NAME, "res").click()
        try:
            assert self.driver.find_element(By.NAME, "cusid").text == ""
        except AssertionError:
            print("Test DC08.2 failed: Reset button does not empty customer ID field\n")
            raise
        else:
            print("Test DC08.2 passed: Reset button empties customer ID field\n")

