# Names: Megan Clarke, Colin Eade, Noelle Dacayo
# Date: April 07, 2023
# File Name: test_m6_delete_account.py
# Description: All tests for the Edit Account Module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest

# set up main class
class TestDeleteAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.get("https://demo.guru99.com/V4/index.php")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr491421")
        self.driver.find_element(By.NAME, "password").send_keys("mYdAqyj")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.get("https://demo.guru99.com/V4/manager/deleteAccountInput.php")

    def teardown(self):
        self.driver.quit()

    # test account number field
    def test_da01(self):
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.SPACE)
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Account Number must not be blank"
        except AssertionError:
            print("Test DA01 failed: Error text is not 'Account Number must not be blank'\n")
            raise
        else:
            print("Test DA01 passed: Error text is 'Account Number must not be blank'\n")

    def test_da02_1(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test DA02.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test DA02.1 passed: Error text is 'Characters are not allowed'\n")

    def test_da02_2(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test DA02.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test DA02.2 passed: Error text is 'Characters are not allowed'\n")

    def test_da03_1(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        except AssertionError:
            print("Test DA03.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test DA03.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_da03_2(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        except AssertionError:
            print("Test DA03.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test DA03.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_da04(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test DA04 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test DA04 passed: Error text is 'Characters are not allowed'\n")

    def test_da05(self):
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.SPACE)
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message2").text == "First character cannot have space"
        except AssertionError:
            print("Test DA05 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test DA05 passed: Error text is 'First character cannot have space'\n")

    # test submit button
    def test_da06(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("120998")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.switch_to.alert.accept()
        try:
            assert self.driver.switch_to.alert.text == "Account deleted successfully"
        except AssertionError:
            print("Test DA06 failed: Alert text is not 'Account deleted successfully'\n")
            raise
        else:
            print("Test DA06 passed: Alert text is 'Account deleted successfully'\n")

    def test_da07(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("12345")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        self.driver.switch_to.alert.accept()
        try:
            assert self.driver.switch_to.alert.text == "Account does not exist"
        except AssertionError:
            print("Test DA06 failed: Alert text is not 'Account does not exist'\n")
            raise
        else:
            print("Test DA06 passed: Alert text is 'Account does not exist'\n")

    # test reset button
    def test_da08_1(self):
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer")
        self.driver.find_element(By.NAME, "res").click()
        try:
            assert self.driver.find_element(By.NAME, "accountno").text == ""
        except AssertionError:
            print("Test DA08.1 failed: Reset button does not empty Account Number field\n")
            raise
        else:
            print("Test DA08.1 passed: Reset button empties Account Number field\n")

    def test_da08_2(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("123456")
        self.driver.find_element(By.NAME, "res").click()
        try:
            assert self.driver.find_element(By.NAME, "accountno").text == ""
        except AssertionError:
            print("Test DA08.2 failed: Reset button does not empty Account Number field\n")
            raise
        else:
            print("Test DA08.2 passed: Reset button empties Account Number field\n")
