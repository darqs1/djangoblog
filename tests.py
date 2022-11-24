# from django.test import TestCase
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url='http://localhost:8000/admin')

def element_is_clickable():
    driver.find_element("xpath", '//*[@id="id_username"]').send_keys("darek")
    driver.find_element("xpath", '//*[@id="id_password"]').send_keys("darekk")
    time.sleep(2)
    driver.find_element("xpath", '//*[@id="login-form"]/div[3]/input').click()

#element_is_clickable()

def response_check(w,file):
    height = 768
    driver.set_window_size(w,height)
    driver.save_screenshot(file)

response_check(900,"test900.png")
response_check(1800,"test1800.png")
response_check(600,"test600.png")