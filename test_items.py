import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def test_language(browser):
    browser.get("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    btn_add = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    btn_add_text = btn_add.text
    assert btn_add_text != "", "Кнопки нет или текст не тот"