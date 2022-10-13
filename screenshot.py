from selenium import webdriver
from shutil import which
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

for i in range(371205, 371225): #select a range of numbers to automatically capture
    driver = webdriver.Firefox();
    driver.get(f'https://www.mrexcel.com/board/threads/{i}/');
    time.sleep(3)
    driver.get_full_page_screenshot_as_file(f"./caps/{i}.png");
    driver.quit()


