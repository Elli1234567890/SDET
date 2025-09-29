import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Первый автотест, демо
@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')

def test_demo1():
    assert 1 == 1

def test_demo2(before_after):
    assert 2 == 2



# Второй автотест, на сайте
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    # webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()


def test_open_s6(driver):
    driver.get('https://demoblaze.com/index.html')
    galaxy_s6 = driver.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'


def test_two_monitors(driver):
    driver.get('https://demoblaze.com/index.html')
    monitor_link = driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(2) # это плохо, лучше изучить типы ожидания в Selenium
    monitors = driver.find_elements(By.CSS_SELECTOR, '.card')
    assert len(monitors) == 2

