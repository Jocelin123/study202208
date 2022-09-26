from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def element_to_be_clickable1(target_element,next_element):
    def _predicate(driver):
        driver.find_element(*target_element).click()
        return driver.find_element(*next_element)
    return _predicate
def wait_until():
    driver=webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    WebDriverWait(driver,10).until(
        element_to_be_clickable1((By.CSS_SELECTOR,"#primary_btn"),(By.CSS_SELECTOR,".el-message-box__title")))
    driver.find_element(By.CSS_SELECTOR, ".el-message-box__btns span").click()
    sleep(2)
    driver.quit()
if __name__ == '__main__':
    wait_until()


