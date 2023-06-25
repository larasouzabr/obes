from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
@given("the user is in the profile page and scroll into the registered books")
def given(context):
    pass

@when("clicks in Edit and edit some book information")
def when(context):
    pass

@then("system updates the book information")
def then(context):
    pass