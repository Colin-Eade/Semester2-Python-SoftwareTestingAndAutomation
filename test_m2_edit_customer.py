# Names: Megan Clarke, Colin Eade, Noelle Dacayo
# Date: April 07, 2023
# File Name: test_m2_edit_customer.py
# Description: All tests for the Edit Customer Module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep

# set up main class
class TestEditCustomer(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.maxDiff = None
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.get("https://demo.guru99.com/V4/index.php")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr491421")
        self.driver.find_element(By.NAME, "password").send_keys("mYdAqyj")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.get("https://demo.guru99.com/V4/manager/EditCustomer.php")

    def tearDown(self):
        self.driver.quit()

    # test customer ID field
    def test_ec01(self):
        self.driver.find_element(By.NAME, "cusid").click()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Customer ID is required"
        except AssertionError:
            print("Test EC01 failed: Error text is not 'Customer ID is required'\n")
            raise
        else:
            print("Test EC01 passed: Error text is 'Customer ID is required'\n")

    def test_ec02_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Characters are not allowed"
        except AssertionError:
            print("Test EC02.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test EC02.1 passed: Error text is 'Characters are not allowed'\n")

    def test_ec02_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Characters are not allowed"
        except AssertionError:
            print("Test EC02.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test EC02.2 passed: Error text is 'Characters are not allowed'\n")

    def test_ec03_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC03.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC03.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_ec03_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message14").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC03.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC03.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_ec04(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        try:
            assert self.driver.find_element(By.CSS_SELECTOR, ".heading3").text == "Edit Customer"
        except AssertionError:
            print("Test EC04 failed: Heading text is not 'Edit Customer'\n")
            raise
        else:
            print("Test EC04 passed: Heading text is 'Edit Customer'\n")

    # test address field
    def test_ec05(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        address = self.driver.find_element(By.NAME, "addr")
        address.clear()
        sleep(1)
        self.driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message3").text == "Address Field must not be blank"
        except AssertionError:
            print("Test EC05 failed: Error text is not 'Address Field must not be blank'\n")
            raise
        else:
            print("Test EC05 passed: Error text is 'Address Field must not be blank'\n")

    # test city field
    def test_ec06(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        city = self.driver.find_element(By.NAME, "city")
        city.clear()
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message4").text == "City Field must not be blank"
        except AssertionError:
            print("Test EC06 failed: Error text is not 'City Field must not be blank'\n")
            raise
        else:
            print("Test EC06 passed: Error text is 'City Field must not be blank'\n")

    def test_ec07_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        city = self.driver.find_element(By.NAME, "city")
        city.clear()
        self.driver.find_element(By.NAME, "city").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message4").text == "Numbers are not allowed"
        except AssertionError:
            print("Test EC07.1 failed: Error text is not 'Numbers are not allowed'\n")
            raise
        else:
            print("Test EC07.1 passed: Error text is 'Numbers are not allowed'\n")

    def test_ec07_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        city = self.driver.find_element(By.NAME, "city")
        city.clear()
        self.driver.find_element(By.NAME, "city").send_keys("city123")
        try:
            assert self.driver.find_element(By.ID, "message4").text == "Numbers are not allowed"
        except AssertionError:
            print("Test EC07.2 failed: Error text is not 'Numbers are not allowed'\n")
            raise
        else:
            print("Test EC07.2 passed: Error text is 'Numbers are not allowed'\n")

    def test_ec08_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        city = self.driver.find_element(By.NAME, "city")
        city.clear()
        self.driver.find_element(By.NAME, "city").send_keys("City!@#")
        try:
            assert self.driver.find_element(By.ID, "message4").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC08.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC08.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_ec08_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        city = self.driver.find_element(By.NAME, "city")
        city.clear()
        self.driver.find_element(By.NAME, "city").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message4").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC08.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC08.1 passed: Error text is 'Special characters are not allowed'\n")

    # test state field
    def test_ec09(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        state = self.driver.find_element(By.NAME, "state")
        state.clear()
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message5").text == "State must not be blank"
        except AssertionError:
            print("Test EC09 failed: Error text is not 'State must not be blank'\n")
            raise
        else:
            print("Test EC09 passed: Error text is 'State must not be blank'\n")

    def test_ec10_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        state = self.driver.find_element(By.NAME, "state")
        state.clear()
        self.driver.find_element(By.NAME, "state").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message5").text == "Numbers are not allowed"
        except AssertionError:
            print("Test EC10.1 failed: Error text is not 'Numbers are not allowed'\n")
            raise
        else:
            print("Test EC10.1 passed: Error text is 'Numbers are not allowed'\n")

    def test_ec10_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        state = self.driver.find_element(By.NAME, "state")
        state.clear()
        self.driver.find_element(By.NAME, "state").send_keys("State123")
        try:
            assert self.driver.find_element(By.ID, "message5").text == "Numbers are not allowed"
        except AssertionError:
            print("Test EC10.2 failed: Error text is not 'Numbers are not allowed'\n")
            raise
        else:
            print("Test EC10.2 passed: Error text is 'Numbers are not allowed'\n")

    def test_ec11_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        state = self.driver.find_element(By.NAME, "state")
        state.clear()
        self.driver.find_element(By.NAME, "state").send_keys("State!@#")
        try:
            assert self.driver.find_element(By.ID, "message5").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC11.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC11.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_ec11_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        state = self.driver.find_element(By.NAME, "state")
        state.clear()
        self.driver.find_element(By.NAME, "state").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message5").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC11.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC11.2 passed: Error text is 'Special characters are not allowed'\n")

    # test PIN field
    def test_ec12_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        pin_code = self.driver.find_element(By.NAME, "pinno")
        pin_code.clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "Characters are not allowed"
        except AssertionError:
            print("Test EC12.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test EC12.1 passed: Error text is 'Characters are not allowed'\n")

    def test_ec12_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        pin_code = self.driver.find_element(By.NAME, "pinno")
        pin_code.clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234PIN")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "Characters are not allowed"
        except AssertionError:
            print("Test EC12.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test EC12.2 passed: Error text is 'Characters are not allowed'\n")

    def test_ec13(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        pin_code = self.driver.find_element(By.NAME, "pinno")
        pin_code.clear()
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message6").text == "PIN Code must not be blank"
        except AssertionError:
            print("Test EC13 failed: Error text is not 'PIN Code must not be blank'\n")
            raise
        else:
            print("Test EC13 passed: Error text is 'PIN Code must not be blank'\n")

    def test_ec14_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        pin_code = self.driver.find_element(By.NAME, "pinno")
        pin_code.clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("1234567")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "PIN Code must have 6 Digits"
        except AssertionError:
            print("Test EC14.1 failed: Error text is not 'PIN Code must have 6 Digits'\n")
            raise
        else:
            print("Test EC14.1 passed: Error text is 'PIN Code must have 6 Digits'\n")

    def test_ec14_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        pin_code = self.driver.find_element(By.NAME, "pinno")
        pin_code.clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("123")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "PIN Code must have 6 Digits"
        except AssertionError:
            print("Test EC14.2 failed: Error text is not 'PIN Code must have 6 Digits'\n")
            raise
        else:
            print("Test EC14.2 passed: Error text is 'PIN Code must have 6 Digits'\n")

    def test_ec15_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        pin_code = self.driver.find_element(By.NAME, "pinno")
        pin_code.clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC15.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC15.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_ec15_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        pin_code = self.driver.find_element(By.NAME, "pinno")
        pin_code.clear()
        self.driver.find_element(By.NAME, "pinno").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC15.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC15.2 passed: Error text is 'Special characters are not allowed'\n")

    # test mobile number field
    def test_ec16(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        phone_number = self.driver.find_element(By.NAME, "telephoneno")
        phone_number.clear()
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message7").text == "Telephone no must not be blank"
        except AssertionError:
            print("Test EC16 failed: Error text is not 'Telephone no must not be blank'\n")
            raise
        else:
            print("Test EC16 passed: Error text is 'Telephone no must not be blank'\n")

    def test_ec17_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        phone_number = self.driver.find_element(By.NAME, "telephoneno")
        phone_number.clear()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("886636!@12")
        try:
            assert self.driver.find_element(By.ID, "message7").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC17.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC17.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_ec17_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        phone_number = self.driver.find_element(By.NAME, "telephoneno")
        phone_number.clear()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("!@88662682")
        try:
            assert self.driver.find_element(By.ID, "message7").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC17.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC17.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_ec17_3(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        phone_number = self.driver.find_element(By.NAME, "telephoneno")
        phone_number.clear()
        self.driver.find_element(By.NAME, "telephoneno").send_keys("88663682!@")
        try:
            assert self.driver.find_element(By.ID, "message7").text == "Special characters are not allowed"
        except AssertionError:
            print("Test EC17.3 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test EC17.3 passed: Error text is 'Special characters are not allowed'\n")

    # test email field
    def test_ec18(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        email = self.driver.find_element(By.NAME, "emailid")
        email.clear()
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID must not be blank"
        except AssertionError:
            print("Test EC18 failed: Error text is not 'Email-ID must not be blank'\n")
            raise
        else:
            print("Test EC18 passed: Error text is 'Email-ID must not be blank'\n")

    def test_ec19_1(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        email = self.driver.find_element(By.NAME, "emailid")
        email.clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail")
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID is not valid"
        except AssertionError:
            print("Test EC19.1 failed: Error text is not 'Email-ID is not valid'\n")
            raise
        else:
            print("Test EC19.1 passed: Error text is 'Email-ID is not valid'\n")

    def test_ec19_2(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        email = self.driver.find_element(By.NAME, "emailid")
        email.clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99")
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID is not valid"
        except AssertionError:
            print("Test EC19.2 failed: Error text is not 'Email-ID is not valid'\n")
            raise
        else:
            print("Test EC19.2 passed: Error text is 'Email-ID is not valid'\n")

    def test_ec19_3(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        email = self.driver.find_element(By.NAME, "emailid")
        email.clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("Guru99@")
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID is not valid"
        except AssertionError:
            print("Test EC19.3 failed: Error text is not 'Email-ID is not valid'\n")
            raise
        else:
            print("Test EC19.3 passed: Error text is 'Email-ID is not valid'\n")

    def test_ec19_4(self):
        self.driver.find_element(By.NAME, "cusid").send_keys("17344")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        email = self.driver.find_element(By.NAME, "emailid")
        email.clear()
        self.driver.find_element(By.NAME, "emailid").send_keys("gurugmail.com")
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID is not valid"
        except AssertionError:
            print("Test EC19.4 failed: Error text is not 'Email-ID is not valid'\n")
            raise
        else:
            print("Test EC19.4 passed: Error text is 'Email-ID is not valid'\n")

    # test submit button
    def test_ec20(self):
        email_id = self.driver.find_element(By.NAME, "emailid")
        email_id.clear()
        sleep(1)
        self.driver.find_element(By.NAME, "emailid").send_keys("testemail@test.com")
        self.driver.find_element(By.NAME, "sub").click()
        try:
            assert self.driver.switch_to.alert.text == "Update done successfully"
        except AssertionError:
            print("Test EC20 failed: Alert text is not 'Update done successfully'\n")
            raise
        else:
            print("Test EC20 passed: Alert text is 'Update done successfully'\n")
