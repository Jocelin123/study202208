import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

# from study202208.practice.prepare_ui1.page.page_object import PageObject


class TestWeiworkLogin():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    # def teardown_class(self):
    #     self.driver.quit()

    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        time.sleep(10)
        cookies=self.driver.get_cookies()
        with open("../data/cookies.yaml","w",encoding='u8') as f:
            yaml.safe_dump(cookies,f)

    def test_add_cookie(self):
        self.driver.delete_all_cookies()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        with open("../data/cookies.yaml", "r", encoding='u8') as f:
            cookies=yaml.safe_load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        # time.sleep(2)
        # self.driver.find_element(By.CSS_SELECTOR, ".js_party_info .js_has_member>div:nth-child(1) .js_add_member").click()
        time.sleep(3)
