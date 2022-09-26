from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



def wait_until():
    driver=webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    #False
    # print(driver.find_element(By.CSS_SELECTOR, "#success_btn").is_enabled())
    #True
    # print(driver.find_element(By.CSS_SELECTOR,"#success_btn>span").is_enabled())
    WebDriverWait(driver,15).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"#success_btn>span"))).click()
    sleep(1)
    driver.quit()
if __name__ == '__main__':
    wait_until()