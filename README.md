# Semester 2 - Software Testing and Automation Final Project
**Date:** Winter 2023

This collection of automated test scripts and accompanying documentation showcases the group final project that I and two 
of my peers developed for our 'Software Testing and Automation' course in the second semester. It is designed to 
evaluate the functionality of a banking application. Utilizing Selenium WebDriver with Python, the scripts perform a 
series of actions mimicking user interactions to test various modules within the application, including new customer 
creation, customer and account editing, account deletion, balance inquiries, mini statements, and customized statements. 
These tests verify the application's functionality, ensuring that all user inputs are correctly validated, and that 
the application behaves as expected under various conditions.
# Languages & Technologies
* Python
  * unittest Framework
* Selenium IDE
* Selenium WebDriver
* Microsoft Excel

# Key Features & Test Cases
* **New Customer Module (test_m1_new_customer.py):** Tests focused on validating customer information input fields, such
as name, address, city, state, and PIN, ensuring proper validation messages are displayed for invalid inputs.


* **Edit Customer Module (test_m2_edit_customer.py):** Verifies the functionality for editing customer details, 
including tests for input validation similar to the New Customer Module but applied in an editing context.


* **Delete Customer Module (test_m3_delete_customer.py):**  Assesses the application's ability to delete customers, 
validating that the process correctly handles various scenarios, including attempts to delete non-existent or already 
deleted customers.


* **New Account Module (test_m4_new_account.py):** Checks the account creation process, ensuring the application 
correctly handles the input of customer IDs, account types, and initial deposits, along with proper error handling.


* **Edit Account Module (test_m5_edit_account.py):**  Focuses on the account modification functionality, ensuring that 
changes to account details are processed correctly and that validations for account numbers are enforced.


* **Delete Account Module (test_m6_delete_account.py):** Tests the account deletion process, validating proper behavior 
for different account numbers and ensuring that accounts can be successfully deleted.


* **Balance Enquiry Module (test_m7_balance_enquiry.py):** Validates the functionality for checking an account's 
balance, ensuring that the account number input is properly validated and that the balance is correctly displayed.


* **Mini Statement Module (test_m8_mini_statement.py):** Verifies the mini statement functionality, ensuring that users 
can retrieve a statement for an account and that the information presented is accurate.


* **Customized Statement Module (test_m9_customized_statement.py):** Tests the customized statement functionality, 
allowing users to specify criteria such as date range, minimum transaction value, and number of transactions for 
the statement they wish to view.
