from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "utils/uploads/book-test.jpg")
sys.path.append(path_dir)


@given("user in the Add Book page")
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

    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div/section/section[1]/header/div[2]/a[1]')
    ))
    profile_donation_button = context.driver.find_element(By.XPATH,
                                                          '/html/body/div/section/section[1]/header/div[2]/a[1]')
    profile_donation_button.click()


@when("fills out all the required information and clicks in Next")
def when(context):
    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.ID, 'bookName')
    ))
    book_title_input = context.driver.find_element(By.ID, "bookName")
    book_title_input.send_keys("Teste automatizado selenium")

    book_category_select = context.driver.find_element(By.ID, "category")
    select = Select(book_category_select)
    select.select_by_visible_text("Arte, Cinema e Fotografia")

    book_description_input = context.driver.find_element(By.ID, "description")
    book_description_input.send_keys(
        "Descrição teste de livro teste para teste automatizado selenium com mais de 20 caracteres")

    book_image = context.driver.find_element(By.XPATH, '/html/body/div/section/section[1]/form/div[4]/div/input')
    upload = path_dir
    book_image.send_keys(upload)

    term_checkbox = context.driver.find_element(By.XPATH, '/html/body/div/section/section[1]/form/div[5]/div/input')
    term_checkbox.click()

    next_button = context.driver.find_element(By.XPATH, '/html/body/div/section/section[1]/form/div[6]/button')
    next_button.submit()

    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div/section/section[2]/form/div/div[2]/div[5]/button[2]')
    ))

    submit_button = context.driver.find_element(By.XPATH,
                                                '/html/body/div/section/section[2]/form/div/div[2]/div[5]/button[2]')
    submit_button.click()


@then("systems add book to donation page")
def then(context):
    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div/section/div[1]')
    ))

    return_to_page = context.driver.find_element(By.XPATH, '/html/body/div/section/div[1]/a')
    return_to_page.click()

    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div/nav/div/div/div[2]/ul/a')
    ))

    profile_navbar = context.driver.find_element(By.XPATH, '/html/body/div/nav/div/div/div[2]/ul/a')
    profile_navbar.click()

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(context.driver, 30).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, '/html/body/div/section/section[4]/div/div'), "Teste automatizado selenium"))
    context.driver.quit()
