import pytest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_find_btn_add_to_basket(browser):
    # Переходим по ссылке
    browser.get(link)
    time.sleep(30)
    # Находим кнопку
    button = len(browser.find_elements_by_css_selector(".btn-add-to-baskets"))
    # Проверяем соответствует фитбек заданному значению
    assert button > 0, "No button!"
