# Names: Megan Clarke, Colin Eade, Noelle Dacayo
# Date: April 07, 2023
# File Name: test_m1_new_customer.py
# Description: All tests for the New Customer Module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep


# Set up the main class
class TestNewCustomer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.get("https://demo.guru99.com/V4/index.php")
        self.driver.find_element(By.NAME, "uid").send_keys("mngr491421")
        self.driver.find_element(By.NAME, "password").send_keys("mYdAqyj")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.get("https://demo.guru99.com/V4/manager/addcustomerpage.php")

    def teardown(self):
        self.driver.quit()

    # Test the Name field
    def test_nc01(self):
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message").text == "Customer name must not be blank"
        except AssertionError:
            print("Test NC01 failed: Error text is not 'Customer name must not be blank'\n")
            raise
        else:
            print("Test NC01 passed: Error text is 'Customer name must not be blank'\n")

    def test_nc02_1(self):
        self.driver.find_element(By.NAME, "name").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message").text == "Numbers are not allowed"
        except AssertionError:
            print("Test NC02.1 failed: Error text is not 'Numbers are not allowed'\n")
            raise
        else:
            print("Test NC02.1 passed: Error text is 'Numbers are not allowed'\n")

    def test_nc02_2(self):
        self.driver.find_element(By.NAME, "name").send_keys("name123")
        try:
            assert self.driver.find_element(By.ID, "message").text == "Numbers are not allowed"
        except AssertionError:
            print("Test NC02.2 failed: Error text is not 'Numbers are not allowed'\n")
            raise
        else:
            print("Test NC02.2 passed: Error text is 'Numbers are not allowed'\n")

    def test_nc03_1(self):
        self.driver.find_element(By.NAME, "name").send_keys("name!@#")
        try:
            assert self.driver.find_element(By.ID, "message").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC03.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC03.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_nc03_2(self):
        self.driver.find_element(By.NAME, "name").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC03.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC03.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_nc04(self):
        self.driver.find_element(By.NAME, "name").send_keys(Keys.SPACE)
        try:
            assert self.driver.find_element(By.ID, "message").text == "First character cannot have space"
        except AssertionError:
            print("Test NC04 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test NC04 passed: Error text is 'First character cannot have space'\n")

    # test the address field
    def test_nc05(self):
        self.driver.find_element(By.NAME, "addr").click()
        self.driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message3").text == "Address Field must not be blank"
        except AssertionError:
            print("Test NC05 failed: Error text is not 'Address Field must not be blank'\n")
            raise
        else:
            print("Test NC05 passed: Error text is 'Address Field must not be blank'\n")

    def test_nc06(self):
        self.driver.find_element(By.NAME, "addr").send_keys(Keys.SPACE)
        try:
            assert self.driver.find_element(By.ID, "message3").text == "First character cannot have space"
        except AssertionError:
            print("Test NC06 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test NC06 passed: Error text is 'First character cannot have space'\n")

    # test city field
    def test_nc07(self):
        self.driver.find_element(By.NAME, "city").click()
        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message4").text == "City Field must not be blank"
        except AssertionError:
            print("Test NC07 failed: Error text is not 'City Field must not be blank'\n")
            raise
        else:
            print("Test NC07 passed: Error text is 'City Field must not be blank'\n")

    def test_nc08_1(self):
        self.driver.find_element(By.NAME, "city").send_keys("city123")
        try:
            assert self.driver.find_element(By.ID, "message4").text == "Numbers are not allowed"
        except AssertionError:
            print("Test NC08.1 failed: Error text is not 'Numbers are not allowed'\n")
            raise
        else:
            print("Test NC08.1 passed: Error text is 'Numbers are not allowed'\n")

    def test_nc08_2(self):
        self.driver.find_element(By.NAME, "city").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message4").text == "Numbers are not allowed"
        except AssertionError:
            print("Test NC08.2 failed: Error text is not 'Numbers are not allowed'\n")
            raise
        else:
            print("Test NC08.2 passed: Error text is 'Numbers are not allowed'\n")

    def test_nc09_1(self):
        self.driver.find_element(By.NAME, "city").send_keys("City!@#")
        try:
            assert self.driver.find_element(By.ID, "message4").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC09.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC09.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_nc09_2(self):
        self.driver.find_element(By.NAME, "city").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message4").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC09.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC09.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_nc10(self):
        self.driver.find_element(By.NAME, "city").send_keys(Keys.SPACE, "city")
        try:
            assert self.driver.find_element(By.ID, "message4").text == "First character cannot have space"
        except AssertionError:
            print("Test NC10 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test NC10 passed: Error text is 'First character cannot have space'\n")

    # test state field
    def test_nc11(self):
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message5").text == "State must not be blank"
        except AssertionError:
            print("Test NC11 failed: Error text is not 'State must not be blank'\n")
            raise
        else:
            print("Test NC11 passed: Error text is 'State must not be blank'\n")

    def test_nc12_1(self):
        self.driver.find_element(By.NAME, "state").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message5").text == "Numbers are not allowed"
        except AssertionError:
            print("Test NC12.1 failed: Error text is not 'Numbers are not allowed'\n")
            raise
        else:
            print("Test NC12.1 passed: Error text is 'Numbers are not allowed'\n")

    def test_nc12_2(self):
        self.driver.find_element(By.NAME, "state").send_keys("State123")
        try:
            assert self.driver.find_element(By.ID, "message5").text == "Numbers are not allowed"
        except AssertionError:
            print("Test NC12.2 failed: Error text is not 'Numbers are not allowed'\n")
            raise
        else:
            print("Test NC12.2 passed: Error text is 'Numbers are not allowed'\n")

    def test_nc13_1(self):
        self.driver.find_element(By.NAME, "state").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message5").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC13.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC13.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_nc13_2(self):
        self.driver.find_element(By.NAME, "state").send_keys("State!@#")
        try:
            assert self.driver.find_element(By.ID, "message5").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC13.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC13.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_nc14(self):
        self.driver.find_element(By.NAME, "state").click()
        self.driver.find_element(By.NAME, "state").send_keys(" ")
        try:
            assert self.driver.find_element(By.ID, "message5").text == "First character cannot have space"
        except AssertionError:
            print("Test NC14 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test NC14 passed: Error text is 'First character cannot have space'\n")

    # test PIN field
    def test_nc15_1(self):
        self.driver.find_element(By.NAME, "pinno").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "Characters are not allowed"
        except AssertionError:
            print("Test NC15 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test NC15 passed: Error text is 'Characters are not allowed'\n")

    def test_nc15_2(self):
        self.driver.find_element(By.NAME, "pinno").send_keys("1234PIN")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "Characters are not allowed"
        except AssertionError:
            print("Test NC12.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test NC12.2 passed: Error text is 'Characters are not allowed'\n")

    def test_nc16(self):
        self.driver.find_element(By.NAME, "pinno").click()
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message6").text == "PIN Code must not be blank"
        except AssertionError:
            print("Test NC16 failed: Error text is not 'PIN Code must not be blank'\n")
            raise
        else:
            print("Test NC16 passed: Error text is 'PIN Code must not be blank'\n")

    def test_nc17_1(self):
        self.driver.find_element(By.NAME, "pinno").send_keys("12")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "PIN Code must have 6 Digits"
        except AssertionError:
            print("Test NC17.1 failed: Error text is not 'PIN Code must have 6 Digits'\n")
            raise
        else:
            print("Test NC17.1 passed: Error text is 'PIN Code must have 6 Digits'\n")

    def test_nc17_2(self):
        self.driver.find_element(By.NAME, "pinno").send_keys("123")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "PIN Code must have 6 Digits"
        except AssertionError:
            print("Test NC17.2 failed: Error text is not 'PIN Code must have 6 Digits'\n")
            raise
        else:
            print("Test NC17.2 passed: Error text is 'PIN Code must have 6 Digits'\n")

    def test_nc18_1(self):
        self.driver.find_element(By.NAME, "pinno").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC18.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC18.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_nc18_2(self):
        self.driver.find_element(By.NAME, "pinno").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC18.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC18.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_nc19(self):
        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.SPACE, "123")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "First character cannot have space"
        except AssertionError:
            print("Test NC19 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test NC19 passed: Error text is 'First character cannot have space'\n")

    def test_nc20(self):
        self.driver.find_element(By.NAME, "pinno").send_keys("123 45")
        try:
            assert self.driver.find_element(By.ID, "message6").text == "Characters are not allowed"
        except AssertionError:
            print("Test NC20 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test NC20 passed: Error text is 'Characters are not allowed'\n")

    # test mobile number field
    def test_nc21(self):
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message7").text == "Mobile no must not be blank"
        except AssertionError:
            print("Test NC21 failed: Error text is not 'Mobile no must not be blank'\n")
            raise
        else:
            print("Test NC21 passed: Error text is 'Mobile no must not be blank'\n")

    def test_nc22(self):
        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.SPACE, "905")
        try:
            assert self.driver.find_element(By.ID, "message7").text == "First character cannot have space"
        except AssertionError:
            print("Test NC21 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test NC21 passed: Error text is 'First character cannot have space'\n")

    def test_nc23(self):
        self.driver.find_element(By.NAME, "telephoneno").send_keys("123", Keys.SPACE, "123")
        try:
            assert self.driver.find_element(By.ID, "message7").text == "Characters are not allowed"
        except AssertionError:
            print("Test NC23 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test NC23 passed: Error text is 'Characters are not allowed'\n")

    def test_nc24_1(self):
        self.driver.find_element(By.NAME, "telephoneno").send_keys("886636!@12")
        try:
            assert self.driver.find_element(By.ID, "message7").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC24.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC24.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_nc24_2(self):
        self.driver.find_element(By.NAME, "telephoneno").send_keys("!@88662682")
        try:
            assert self.driver.find_element(By.ID, "message7").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC24.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC24.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_nc24_3(self):
        self.driver.find_element(By.NAME, "telephoneno").send_keys("88663682!@")
        try:
            assert self.driver.find_element(By.ID, "message7").text == "Special characters are not allowed"
        except AssertionError:
            print("Test NC24.3 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test NC24.3 passed: Error text is 'Special characters are not allowed'\n")

    # test email field
    def test_nc25(self):
        self.driver.find_element(By.NAME, "emailid").click()
        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID must not be blank"
        except AssertionError:
            print("Test NC25 failed: Error text is not 'Email-ID must not be blank'\n")
            raise
        else:
            print("Test NC25 passed: Error text is 'Email-ID must not be blank'\n")

    def test_nc26_1(self):
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail ")
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID is not valid"
        except AssertionError:
            print("Test NC26.1 failed: Error text is not 'Email-ID is not valid'\n")
            raise
        else:
            print("Test NC26.1 passed: Error text is 'Email-ID is not valid'\n")

    def test_nc26_2(self):
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99")
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID is not valid"
        except AssertionError:
            print("Test NC26.2 failed: Error text is not 'Email-ID is not valid'\n")
            raise
        else:
            print("Test NC26.2 passed: Error text is 'Email-ID is not valid'\n")

    def test_nc26_3(self):
        self.driver.find_element(By.NAME, "emailid").send_keys("Guru99@")
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID is not valid"
        except AssertionError:
            print("Test NC26.3 failed: Error text is not 'Email-ID is not valid'\n")
            raise
        else:
            print("Test NC26.3 passed: Error text is 'Email-ID is not valid'\n")

    def test_nc26_4(self):
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail. ")
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID is not valid"
        except AssertionError:
            print("Test NC26.4 failed: Error text is not 'Email-ID is not valid'\n")
            raise
        else:
            print("Test NC26.4 passed: Error text is 'Email-ID is not valid'\n")

    def test_nc26_5(self):
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99gmail.com")
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID is not valid"
        except AssertionError:
            print("Test NC26.5 failed: Error text is not 'Email-ID is not valid'\n")
            raise
        else:
            print("Test NC26.5 passed: Error text is 'Email-ID is not valid'\n")

    def test_nc27(self):
        self.driver.find_element(By.NAME, "emailid").send_keys("guru 99@gmail.com")
        try:
            assert self.driver.find_element(By.ID, "message9").text == "Email-ID is not valid"
        except AssertionError:
            print("Test NC27 failed: Error text is not 'Email-ID is not valid'\n")
            raise
        else:
            print("Test NC27 passed: Error text is 'Email-ID is not valid'\n")

    # Test password field
    def test_nc28(self):
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message18").text == "Password must not be blank"
        except AssertionError:
            print("Test NC28 failed: Error text is not 'Password must not be blank'\n")
            raise
        else:
            print("Test NC28 passed: Error text is 'Password must not be blank'\n")
