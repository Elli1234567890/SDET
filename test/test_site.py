import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.homepage import HomePage
from pages.product import ProductPage

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

