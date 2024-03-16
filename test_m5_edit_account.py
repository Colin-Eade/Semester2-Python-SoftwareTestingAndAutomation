# Names: Megan Clarke, Colin Eade, Noelle Dacayo
# Date: April 07, 2023
# File Name: test_m5_edit_account.py
# Description: All tests for the Edit Account Module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest

# set up main class
class TestEditAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.get("https://demo.guru99.com/V4/index.php")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr491421")
        self.driver.find_element(By.NAME, "password").send_keys("mYdAqyj")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.get("https://demo.guru99.com/V4/manager/editAccount.php")

    def teardown(self):
        self.driver.quit()

    # test account number field
    def test_ea01(self):
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Account Number must not be empty"
        except AssertionError:
            print("Test EA01 failed: Error text is not 'Account Number must not be empty'\n")
            raise
        else:
            print("Test EA01 passed: Error text is 'Account Number must not be empty'\n")

    def test_ea02_1(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test EA02.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test EA02.1 passed: Error text is 'Characters are not allowed'\n")

    def test_ea02_2(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test EA02.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test EA02.2 passed: Error text is 'Characters are not allowed'\n")

    def test_ea03_1(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EA03.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EA03.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_ea03_2(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("!@#")
        assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EA03.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EA03.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_ea04(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test EA04 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test EA04 passed: Error text is 'Characters are not allowed'\n")

    def test_ea05(self):
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.SPACE)
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message2").text == "First character cannot have space"
        except AssertionError:
            print("Test EA05 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test EA05 passed: Error text is 'First character cannot have space'\n")

    # test submit button
    def test_ea06(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("120998")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        try:
            assert self.driver.find_element(By.CSS_SELECTOR, ".heading3").text == "Edit Account"

        except AssertionError:
            print("Test EA06 failed: Page does not redirect to an 'Edit Account' page\n")
            raise
        else:
            print("Test EA06 passed: Page redirects to an 'Edit Account' page\n")

    def test_ea07(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("12345")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        try:
            assert self.driver.switch_to.alert.text == "Account does not exist"
        except AssertionError:
            print("Test EA07 failed: Alert text is not 'Account does not exist'\n")
            raise
        else:
            print("Test EA07 passed: Alert text is 'Account does not exist'\n")

    # test reset button
    def test_ea08_1(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("qwer")
        self.driver.find_element(By.NAME, "res").click()
        try:
            assert self.driver.find_element(By.NAME, "accountno").text == ""
        except AssertionError:
            print("Test EA08.1 failed: Reset button does not empty Account Number field\n")
            raise
        else:
            print("Test EA08.1 passed: Reset button empties Account Number field\n")

    def test_ea08_2(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("123456")
        self.driver.find_element(By.NAME, "res").click()
        try:
            assert self.driver.find_element(By.NAME, "accountno").text == ""
        except AssertionError:
            print("Test EA08.2 failed: Reset button does not empty Account Number field\n")
            raise
        else:
            print("Test EA08.2 passed: Reset button empties Account Number field\n")
