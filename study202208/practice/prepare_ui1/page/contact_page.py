import time

from selenium.webdriver.common.by import By

from study202208.practice.prepare_ui1.page.base import Base
from study202208.practice.prepare_ui1.page.dept_page import DeptPage


class ContactPage(Base):
    _INPUT_TIPSMEMBER=By.XPATH,"//*[text()='保存成功']"
    _INPUT_TIPSDEPT=By.XPATH,"//*[text()='新建部门成功']"
    _INPUT_ADDBTN=By.CSS_SELECTOR, ".member_colLeft_top_addBtn"
    _INPUT_ADDBTN1=By.CSS_SELECTOR, ".js_create_party"

    def get_tips_member(self):
        return self.get_text(self._INPUT_TIPSMEMBER)

    def get_tips_dept(self):
        return self.get_text(self._INPUT_TIPSDEPT)

    def click_adddept(self):
        self.click_ele(self._INPUT_ADDBTN)
        self.click_ele(self._INPUT_ADDBTN1)
        return DeptPage(self.driver)