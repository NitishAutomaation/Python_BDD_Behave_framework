from behave import when
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service


@when(u'i access to the application')
def step_impl(context):
    driver = webdriver.Chrome(service=Service(""))
    driver.maximize_window()
    driver.get("https://allensolly.abfrl.in/")

    print("hello i am access to appliation")
