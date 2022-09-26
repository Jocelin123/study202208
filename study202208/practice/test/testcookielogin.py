import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCookieLogin:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(20)
        cookie=self.driver.get_cookies()
        with open("cookie.yaml","w") as f:
            yaml.safe_dump(cookie,f)


    def test_add_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        with open("cookie.yaml") as f:
            cookies=yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def test_add_member(self):
        self.add_cookie()
        ele=self.driver.find_element(By.XPATH,"//*[text()='添加成员']")
        ele.click()