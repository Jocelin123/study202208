import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from study202208.practice.prepare_ui1.page.addmember_page import AddMemberPage
from study202208.practice.prepare_ui1.page.base import Base
from study202208.practice.prepare_ui1.page.contact_page import ContactPage


class HomePage(Base):
    _INPUT_ADDMEMBER=By.XPATH,"//*[text()='添加成员']"
    _INPUT_MENU=By.CSS_SELECTOR, "#menu_contacts"

    def click_add_member(self):
        self.click_ele(self._INPUT_ADDMEMBER)
        return AddMemberPage(self.driver)

    def click_contactpage(self):
        time.sleep(2)
        self.click_ele(self._INPUT_MENU)
        return ContactPage(self.driver)





