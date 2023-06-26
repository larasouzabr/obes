import time
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
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get("http://localhost:8080/login")
    context.driver.maximize_window()
    enter_button = context.driver.find_element(By.CLASS_NAME, "enter")
    enter_button.click()
    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.ID, 'email')
    ))
    email_field = context.driver.find_element(By.ID, "email")
    email_field.send_keys("usuario@gmail.com")
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys("12345678")
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div/main/form/div/button")
    login_button.click()

    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div/nav/div/div/div[2]/ul/a')
    ))

    profile_navbar = context.driver.find_element(By.XPATH, '/html/body/div/nav/div/div/div[2]/ul/a')
    profile_navbar.click()


@when("clicks in Edit and edit some book information")
def when(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    edit_book_button = context.driver.find_element(By.XPATH,
                                                   '/html/body/div/section/section[4]/div/div/div[1]/div[4]/button')
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    edit_book_button.click()

    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div[1]/section/section[4]/div/div/div[2]/div/div/div[2]/div[1]/input')
    ))
    book_title_input = context.driver.find_element(By.XPATH,
                                                   '/html/body/div[1]/section/section[4]/div/div/div[2]/div/div/div[2]/div[1]/input')
    book_title_input.send_keys(' edited')

    submit_informations_button = context.driver.find_element(By.XPATH,
                                                             '/html/body/div[1]/section/section[4]/div/div/div[2]/div/div/div[3]/button[2]')
    submit_informations_button.click()


@then("system updates the book information")
def then(context):
    WebDriverWait(context.driver, 30).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, '/html/body/div/section/section[4]/div/div'), "Teste automatizado selenium edited"))
    context.driver.quit()
