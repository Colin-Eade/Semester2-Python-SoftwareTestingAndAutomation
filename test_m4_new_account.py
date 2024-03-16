# Names: Megan Clarke, Colin Eade, Noelle Dacayo
# Date: April 07, 2023
# File Name: test_m4_new_account.py
# Description: All tests for the Add Account Module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import unittest

# Set up main class
class TestNewAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.get("https://demo.guru99.com/V4/index.php")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr491421")
        self.driver.find_element(By.NAME, "password").send_keys("mYdAqyj")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.get("https://demo.guru99.com/V4/manager/addAccount.php")

    def tearDown(self):
        self.driver.quit()

    # test Customer ID field
    def test_na01(self):
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Customer ID is required"
        except AssertionError:
            print("Test NA01 failed: Error text is not 'Customer ID is required'\n")
            raise
        else:
            print("Test NA01 passed: Error text is 'Customer ID is required'\n")

    def test_na02_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Characters are not allowed"
        except AssertionError:
            print("Test NA02.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test NA02.1 passed: Error text is 'Characters are not allowed'\n")

    def test_na02_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Characters are not allowed"
        except AssertionError:
            print("Test NA02.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test NA02.2 passed: Error text is 'Characters are not allowed'\n")

    def test_na03_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NA03.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NA03.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_na03_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NA03.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NA03.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_na04(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Characters are not allowed"
        except AssertionError:
            print("Test NA04 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test NA04 passed: Error text is 'Characters are not allowed'\n")

    def test_na05(self):
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.SPACE)
        try:
            assert self.driver.find_element(By.ID, "message14").text == "First character cannot have space"
        except AssertionError:
            print("Test NA05 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test NA05 passed: Error text is 'First character cannot have space'\n")

    # test initial deposit field
    def test_na06(self):
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message19").text == "Initial Deposit must not be blank"
        except AssertionError:
            print("Test NA06 failed: Error text is not 'Initial Deposit must not be blank'\n")
            raise
        else:
            print("Test NA06 passed: Error text is 'Initial Deposit must not be blank'\n")

    def test_na07_1(self):
        self.driver.find_element(By.NAME, "inideposit").send_keys("1234Acc")
        try:
            assert self.driver.find_element(By.ID, "message19").text == "Characters are not allowed"
        except AssertionError:
            print("Test NA07.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test NA07.1 passed: Error text is 'Characters are not allowed'\n")

    def test_na07_2(self):
        self.driver.find_element(By.NAME, "inideposit").send_keys("Acc123")
        try:
            assert self.driver.find_element(By.ID, "message19").text == "Characters are not allowed"
        except AssertionError:
            print("Test NA07.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test NA07.2 passed: Error text is 'Characters are not allowed'\n")

    def test_na08_1(self):
        self.driver.find_element(By.NAME, "inideposit").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message19").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NA08.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NA08.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_na08_2(self):
        self.driver.find_element(By.NAME, "inideposit").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message19").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NA08.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NA08.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_na09(self):
        self.driver.find_element(By.NAME, "inideposit").send_keys("123 12")
        try:
            assert self.driver.find_element(By.ID, "message19").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NA09 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NA09 passed: Error text is 'Special characters are not allowed'\n")

    def test_na10(self):
        self.driver.find_element(By.NAME, "inideposit").send_keys(Keys.SPACE)
        self.driver.find_element(By.NAME, "inideposit").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message19").text == "First character cannot have space"
        except AssertionError:
            print("Test NA10 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test NA10 passed: Error text is 'First character cannot have space'\n")

    # test account type dropdown
    def test_na11(self):
        dropdown = self.driver.find_element(By.NAME, "selaccount")
        Select(dropdown).select_by_visible_text("Savings")
        selected_option = Select(dropdown).first_selected_option
        assert selected_option.text == "Savings"
        try:
            assert selected_option.text == "Savings"
        except AssertionError:
            print("Test NA11 failed: Account selected is not 'Savings'\n")
            raise
        else:
            print("Test NA11 passed: Account selected is 'Savings'\n")

    def test_na12(self):
        dropdown = self.driver.find_element(By.NAME, "selaccount")
        Select(dropdown).select_by_visible_text("Current")
        selected_option = Select(dropdown).first_selected_option
        try:
            assert selected_option.text == "Current"
        except AssertionError:
            print("Test NA12 failed: Account selected is not 'Current'\n")
            raise
        else:
            print("Test NA12 passed: Account selected is 'Current'\n")

    # test reset button
    def test_na13_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("qwer")
        self.driver.find_element(By.NAME, "reset").click()
        try:
            assert self.driver.find_element(By.NAME, "cusid").text == ""
        except AssertionError:
            print("Test NA13.1 failed: Reset button does not empty customer ID field\n")
            raise
        else:
            print("Test NA13.1 passed: Reset button empties customer ID field\n")

    def test_na13_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        self.driver.find_element(By.NAME, "reset").click()
        try:
            assert self.driver.find_element(By.NAME, "cusid").text == ""
        except AssertionError:
            print("Test NA13.2 failed: Reset button does not empty customer ID field\n")
            raise
        else:
            print("Test NA13.2 passed: Reset button empties customer ID field\n")

    # test submit button
    def test_na14(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        self.driver.find_element(By.NAME, "selaccount").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123456")
        self.driver.find_element(By.NAME, "button2").click()
        try:
            assert self.driver.switch_to.alert.text == "Customer does not exist!!"
        except AssertionError:
            print("Test NA14 failed: Alert text is not 'Customer does not exist!!'\n")
            raise
        else:
            print("Test NA14 passed: Alert text is 'Customer does not exist!!'\n")

    def test_na15(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "selaccount").click()
        self.driver.find_element(By.NAME, "inideposit").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("5000")
        self.driver.find_element(By.NAME, "button2").click()
        try:
            assert self.driver.find_element(By.CSS_SELECTOR, ".heading3").text == "Account Generated Successfully!!!"
        except AssertionError:
            print("Test NA15 failed: No heading present with test 'Account Generated Successfully!!!'\n")
            raise
        else:
            print("Test NA15 passed: Heading present with text 'Account Generated Successfully!!!'\n")

    # test hyperlink to manager homepage after successful account creation
    def test_na16(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "selaccount").click()
        self.driver.find_element(By.NAME, "inideposit").send_keys("5000")
        self.driver.find_element(By.NAME, "button2").click()
        self.driver.find_element(By.LINK_TEXT, "Continue").click()
        try:
            assert self.driver.find_element(By.CSS_SELECTOR, ".heading3 > td").text == "Manger Id : mngr491421"
        except AssertionError:
            print("Test EA04 failed: Page does not redirect back to the Manager page\n")
            raise
        else:
            print("Test EA04 passed: Page redirects back to the Manager page\n")
