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
import time

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "utils/uploads/book-test.jpg")
sys.path.append(path_dir)


@given("user in the Add Book page #2")
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
    profile_sale_button = context.driver.find_element(By.XPATH,
                                                      '/html/body/div/section/section[1]/header/div[2]/a[2]')
    profile_sale_button.click()

@when("fills out all the required information and clicks in Next #2")
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

    price_input = context.driver.find_element(By.ID, 'bookPrice')
    price_input.send_keys("2,00")

    term_checkbox = context.driver.find_element(By.ID, 'invalidCheck')
    term_checkbox.click()

    next_button = context.driver.find_element(By.XPATH, '/html/body/div/section/section[1]/form/div[7]/button')
    next_button.submit()

    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div/section/section[2]/form/div/div[2]/div[6]/button[2]')
    ))
    submit_button = context.driver.find_element(By.XPATH,
                                                '/html/body/div/section/section[2]/form/div/div[2]/div[6]/button[2]')
    submit_button.click()


@then("systems add book to sale page")
def then(context):
    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div/section/div[1]')
    ))

    return_to_page = context.driver.find_element(By.XPATH, '/html/body/div/section/div[1]/a')
    return_to_page.click()

    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/div/nav/div/div/div[2]/ul/a')
    ))
    context.driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    profile_navbar = context.driver.find_element(By.XPATH, '/html/body/div/nav/div/div/div[2]/ul/a')
    profile_navbar.click()


    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(context.driver, 30).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, '/html/body/div/section/section[3]/div/div/div[1]'), "Teste automatizado selenium"))
    WebDriverWait(context.driver, 30).until(expected_conditions.text_to_be_present_in_element(
        (By.XPATH, '/html/body/div/section/section[3]/div/div/div[1]/div[4]/span/strong'), "R$ 2"))
    context.driver.quit()
