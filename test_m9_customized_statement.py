# Names: Megan Clarke, Colin Eade, Noelle Dacayo
# Date: April 07, 2023
# File Name: test_m9_customized_statement.py
# Description: All tests for the Customized Statement Module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


# set up the main class
class TestCustomizedStatement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.get("https://demo.guru99.com/V4/index.php")
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr491421")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("mYdAqyj")
        self.driver.find_element(By.NAME, "btnLogin").click()
        self.driver.get("https://demo.guru99.com/V4/manager/CustomisedStatementInput.php")

    def tearDown(self):
        self.driver.quit()

    # test account number field
    def test_cs01(self):
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Account Number must not be blank"
        except AssertionError:
            print("Test CS01 failed: Error text is not 'Account Number must not be blank'\n")
            raise
        else:
            print("Test CS01 passed: Error text is 'Account Number must not be blank'\n")

    def test_cs02_1(self):
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test CS02.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test CS02.1 passed: Error text is 'Characters are not allowed'\n")

    def test_cs02_2(self):
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test CS02.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test CS02.2 passed: Error text is 'Characters are not allowed'\n")

    def test_cs03_1(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        except AssertionError:
            print("Test CS03.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test CS03.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_cs03_2(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Special characters are not allowed"
        except AssertionError:
            print("Test CS03.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test CS03.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_cs04(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message2").text == "Characters are not allowed"
        except AssertionError:
            print("Test CS04 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test CS04 passed: Error text is 'Characters are not allowed'\n")

    def test_cs05(self):
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message2").text == "First character cannot have space"
        except AssertionError:
            print("Test CS05 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test CS05 passed: Error text is 'First character cannot have space'\n")

    # test FROM date field
    def test_cs06(self):
        self.driver.find_element(By.NAME, "fdate").click()
        self.driver.find_element(By.NAME, "fdate").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message26").text == "From Date Field must not be blank"
        except AssertionError:
            print("Test CS06 failed: Error text is not 'From Date Field must not be blank'\n")
            raise
        else:
            print("Test CS06 passed: Error text is 'From Date Field must not be blank'\n")

    # test TO date field
    def test_cs07(self):
        self.driver.find_element(By.NAME, "tdate").click()
        self.driver.find_element(By.NAME, "tdate").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message27").text == "To Date Field must not be blank"
        except AssertionError:
            print("Test CS07 failed: Error text is not 'To Date Field must not be blank'\n")
            raise
        else:
            print("Test CS07 passed: Error text is 'To Date Field must not be blank'\n")

    # test minimum transaction field
    def test_cs08_1(self):
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message12").text == "Characters are not allowed"
        except AssertionError:
            print("Test CS08.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test CS08.1 passed: Error text is 'Characters are not allowed'\n")

    def test_cs08_2(self):
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("Acc123")
        try:
            assert self.driver.find_element(By.ID, "message12").text == "Characters are not allowed"
        except AssertionError:
            print("Test CS08.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test CS08.2 passed: Error text is 'Characters are not allowed'\n")

    def test_cs09_1(self):
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message12").text == "Special characters are not allowed"
        except AssertionError:
            print("Test CS09.1 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test CS09.1 passed: Error text is 'Special characters are not allowed'\n")

    def test_cs09_2(self):
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID, "message12").text == "Special characters are not allowed"
        except AssertionError:
            print("Test CS09.2 failed: Error text is not 'Special characters are not allowed'\n")
            raise
        else:
            print("Test CS09.2 passed: Error text is 'Special characters are not allowed'\n")

    def test_cs10(self):
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("123 12")
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message12").text == "Characters are not allowed"
        except AssertionError:
            print("Test CS10 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test CS10 passed: Error text is 'Characters are not allowed'\n")

    def test_cs11(self):
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(" ")
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message12").text == "First character cannot have space"
        except AssertionError:
            print("Test CS11 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test CS11 passed: Error text is 'First character cannot have space'\n")

    # test number of transactions field
    def test_cs12_1(self):
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("1234")
        try:
            assert self.driver.find_element(By.ID, "message13").text == "Characters are not allowed"
        except AssertionError:
            print("Test CS12.1 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test CS12.1 passed: Error text is 'Characters are not allowed'\n")

    def test_cs12_2(self):
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("Acc123")
        try:
            assert self.driver.find_element(By.ID, "message13").text == "Characters are not allowed"
        except AssertionError:
            print("Test CS12.2 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test CS12.2 passed: Error text is 'Characters are not allowed'\n")

    def test_cs13_1(self):
        self.driver.find_element(By.NAME, "numtransaction").send_keys("123!@#")
        try:
            assert self.driver.find_element(By.ID, "message13").text == "Number of Transaction cannot have special character"
        except AssertionError:
            print("Test CS13.1 failed: Error text is not 'Number of Transaction cannot have special character'\n")
            raise
        else:
            print("Test CS13.1 passed: Error text is 'Number of Transaction cannot have special character'\n")

    def test_cs13_2(self):
        self.driver.find_element(By.NAME, "numtransaction").send_keys("!@#")
        try:
            assert self.driver.find_element(By.ID,
                                            "message13").text == "Number of Transaction cannot have special character"
        except AssertionError:
            print("Test CS13.2 failed: Error text is not 'Number of Transaction cannot have special character'\n")
            raise
        else:
            print("Test CS13.2 passed: Error text is 'Number of Transaction cannot have special character'\n")

    def test_cs14(self):
        self.driver.find_element(By.NAME, "numtransaction").send_keys("123 12")
        self.driver.find_element(By.NAME, "numtransaction").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message13").text == "Characters are not allowed"
        except AssertionError:
            print("Test CS14 failed: Error text is not 'Characters are not allowed'\n")
            raise
        else:
            print("Test CS14 passed: Error text is 'Characters are not allowed'\n")

    def test_cs15(self):
        self.driver.find_element(By.NAME, "numtransaction").send_keys(" ")
        self.driver.find_element(By.NAME, "numtransaction").send_keys(Keys.TAB)
        try:
            assert self.driver.find_element(By.ID, "message13").text == "First character cannot have space"
        except AssertionError:
            print("Test CS15 failed: Error text is not 'First character cannot have space'\n")
            raise
        else:
            print("Test CS15 passed: Error text is 'First character cannot have space'\n")

    # test reset button
    def test_cs16(self):
        self.driver.find_element(By.NAME, "accountno").click()
        self.driver.find_element(By.NAME, "accountno").send_keys("120802")
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "fdate").send_keys("2023")
        self.driver.find_element(By.NAME, "fdate").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "fdate").send_keys("04")
        self.driver.find_element(By.NAME, "fdate").send_keys("01")
        self.driver.find_element(By.NAME, "fdate").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "tdate").send_keys("2023")
        self.driver.find_element(By.NAME, "tdate").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "tdate").send_keys("04")
        self.driver.find_element(By.NAME, "tdate").send_keys("11")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("1")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("5")
        self.driver.find_element(By.NAME, "res").click()
        try:
            assert self.driver.find_element(By.NAME, "accountno").text == ""
            assert self.driver.find_element(By.NAME, "fdate").text == ""
            assert self.driver.find_element(By.NAME, "tdate").text == ""
            assert self.driver.find_element(By.NAME, "amountlowerlimit").text == ""
            assert self.driver.find_element(By.NAME, "numtransaction").text == ""
        except AssertionError:
            print("Test CS16 failed: Reset button does not empty all fields\n")
            raise
        else:
            print("Test CS16 passed: Reset button empties all fields\n")

    # test submit button
    def test_cs17(self):
        self.driver.find_element(By.NAME, "accountno").send_keys("120802")
        self.driver.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "fdate").send_keys("2023")
        self.driver.find_element(By.NAME, "fdate").send_keys(Keys.TAB)
        self.driver.find_element(By.NAME, "fdate").send_keys("04")
        self.driver.find_element(By.NAME, "fdate").send_keys("01")
        self.driver.find_element(By.NAME, "amountlowerlimit").click()
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys("10")
        self.driver.find_element(By.NAME, "numtransaction").click()
        self.driver.find_element(By.NAME, "numtransaction").send_keys("5")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        try:
            assert self.driver.switch_to.alert.text == "Please fill all fields"
        except AssertionError:
            print("Test CS17 failed: Alert text is not 'Please fill all fields'\n")
            raise
        else:
            print("Test CS17 passed: Alert text is 'Please fill all fields'\n")
