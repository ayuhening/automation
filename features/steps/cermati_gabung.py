from behave import*
from locator import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from database import*
from hamcrest import*

@given(u'I am on cermati gabung page')
def step_impl(context):
    context.browser.get(database.userdata["cermati_com"])
    sleep(10)
    context.browser.find_element(By.XPATH,locator.allow_notif).is_displayed()
    context.browser.find_element(By.XPATH,locator.allow_notif).click()
    sleep(1)

@step(u'I input my email')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.email).is_displayed()
    context.browser.find_element(By.XPATH,locator.email).send_keys(database.userdata["email"])
    sleep(1)

@step(u'I input my password')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.password).is_displayed()
    context.browser.find_element(By.XPATH,locator.password).send_keys(database.userdata["password"])
    sleep(1)

@step(u'I input my first name')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.firstname).is_displayed()
    context.browser.find_element(By.XPATH,locator.firstname).send_keys(database.userdata["firstname"])
    sleep(1)

@step(u'I input my last name')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.lastname).is_displayed()
    context.browser.find_element(By.XPATH,locator.lastname).send_keys(database.userdata["lastname"])
    sleep(1)

@step(u'I input my mobile phone')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.mobilephone).is_displayed()
    context.browser.find_element(By.XPATH,locator.mobilephone).send_keys(database.userdata["mobilephone"])
    sleep(1)

@step(u'I input my residence city')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.residence_city).is_displayed()
    context.browser.find_element(By.XPATH,locator.residence_city).send_keys(database.userdata["residence_city"])
    sleep(5)
    list = context.browser.find_elements(By.XPATH,locator.city_suggestion)
    for suggestion in list:
        if (database.userdata["residence_city"].lower() in suggestion.text.lower()):
            suggestion.click()
    sleep(5)

@when(u'I click submit join button')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.submit_join).is_displayed()
    context.browser.find_element(By.XPATH,locator.submit_join).click()
    sleep(3)

@then(u'The validation success appears')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.validation).is_displayed()
    text_element = context.browser.find_element(By.XPATH,locator.validation)
    edit_text = text_element.text
    assert_that(edit_text, contains_string(database.userdata["validation"]))
    sleep(1)
