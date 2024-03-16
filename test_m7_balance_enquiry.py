# Names: Megan Clarke, Colin Eade, Noelle Dacayo
# Date: April 07, 2023
# File Name: test_m7_balance_enquiry.py
# Description: All tests for the Balance Enquiry Module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest


# Set up main class
class TestBalanceEnquiry(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.get("https://demo.guru99.com/V4/index.php")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr491421")
        self.driver.find_element(By.NAME, "password").send_keys("mYdAqyj")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.get("https://demo.guru99.com/V4/manager/BalEnqInput.php")

    def tearDown(self):
        self.driver.quit()

    # test account number
    def test_be01(self):
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Account Number must not be blank"
        except AssertionError:
            print("Test BE01 failed: Error text is not 'Account Number must not be blank'\n")
            raise
        else:
            print("Test BE01 passed: Error text is 'Account Number must not be blank'\n")

    def test_be02_1(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test BE02.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test BE02.1 passed: Error text is 'Characters are not allowed'\n")

    def test_be02_2(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("Acc1234")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test BE02.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test BE02.2 passed: Error text is 'Characters are not allowed'\n")

    def test_be03_1(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        except AssertionError:
            print("Test BE03.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test BE03.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_be03_2(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        except AssertionError:
            print("Test BE03.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test BE03.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_be04(self):
        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message2").text == "First character cannot have space"
        except AssertionError:
            print("Test BE04 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test BE04 passed: Error text is 'First character cannot have space'\n")

    # test submit button
    def test_be05(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("120802")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        tables = self.driver.find_elements(By.TAG_NAME, "table")
        try:
            assert len(tables) > 0
        except AssertionError:
            print("Test BE05 failed: No table found\n")
            raise
        else:
            print("Test BE05 passed: Table found\n")

    def test_be06(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("12345")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        try:
            assert self.driver.switch_to.alert.text == "Account does not exist"
        except AssertionError:
            print("Test BE06 failed: Alert text is not 'Account does not exist'\n")
            raise
        else:
            print("Test BE06 passed: Alert text is 'Account does not exist'\n")

    # test reset button
    def test_be07_1(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer")
        self.driver.find_element(By.NAME, "res").click()
        try:
            assert self.driver.find_element(By.NAME, "accountno").text == ""
        except AssertionError:
            print("Test BE07.1 failed: Reset button does not empty Account Number field\n")
            raise
        else:
            print("Test BE07.1 passed: Reset button empties Account Number field\n")

    def test_be07_2(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("123456")
        self.driver.find_element(By.NAME, "res").click()
        try:
            assert self.driver.find_element(By.NAME, "accountno").text == ""
        except AssertionError:
            print("Test BE07.2 failed: Reset button does not empty Account Number field\n")
            raise
        else:
            print("Test BE07.2 passed: Reset button empties Account Number field\n")
