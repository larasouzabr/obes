import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@given("institutional or common user is in the homepage")
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
    email_field.send_keys("intituicao@gmail.com")
    password_field = context.driver.find_element(By.ID, "password")
    password_field.send_keys("12345678")
    login_button = context.driver.find_element(By.XPATH, "/html/body/div/div/main/form/div/button")
    login_button.click()

    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div/nav/div/div/div[2]/ul/a')
    ))


@when("clicks in some available book and clicks in Add to Cart")
def when(context):
    context.driver.execute_script("window.scrollTo(0, 150);")
    time.sleep(1)
    book_for_sale = context.driver.find_element(By.XPATH,
                                                    '/html/body/div/div[2]/div[1]/section/div[1]/ol/li/div/div/a/div[3]/button')
    book_for_sale.click()

    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div/main/div/div[2]/div[2]/div[1]/a')
    ))

    request_donation_button = context.driver.find_element(By.XPATH, '/html/body/div/main/div/div[2]/div[2]/div[1]/a')
    request_donation_button.click()
    context.driver.execute_script("window.scrollTo(0, 0);")


@then("system shows the message that the product has been added to cart")
def then(context):
    WebDriverWait(context.driver, 30).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, '/html/body/div/main/section/div'), "Produto adicionado no carrinho!"))
    context.driver.quit()
