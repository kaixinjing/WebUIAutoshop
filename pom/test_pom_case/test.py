import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from WebUIAutoshop.pom.base.Event import Event
from WebUIAutoshop.pom.page.UserCenter import UserCenter
from WebUIAutoshop.pom.test_pom_case.conftest import browser
from WebUIAutoshop.settings import ENV


def atest():
    service = Service(r'D:\JetBrains\Chromedrive\chromedriver.exe')
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Chrome(service=service)
    driver.get(ENV.url)
    input()
    # a = driver.find_element(By.CSS_SELECTOR, "body > div.Bott > div > div.you.fl > div:nth-child(3)")
    # b = a.find_elements(By.XPATH, "//div[@class='Bott']//div[3]//div[*]")
    a = driver.find_element(By.CSS_SELECTOR, "body > div.order.cart.mt > div.orderCon.wrapper.clearfix > div.orderR.fr > div.msg")
    b = a.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/ul[*]")
    print(len(b))


if __name__ == '__main__':
    atest()
    # pytest.main(['-vs', 'test.py'])

