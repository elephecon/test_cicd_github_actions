from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def chrome_options():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    return chrome_options

@pytest.fixture()
def browser(chrome_options):
    chrome_browser = webdriver.Chrome(options=chrome_options)
    return chrome_browser


def test_button_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()