import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from demo_test.pages.homepage import HomePage
from demo_test.pages.product import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    productpage = ProductPage(driver)
    productpage.check_title_is('Samsung galaxy s6')


def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.clock_monitor()
    time.sleep(2)  # это плохо, лучше изучить типы ожидания в Selenium
    homepage.check_products_count(2)

