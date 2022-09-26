from selenium.webdriver.common.by import By

from study202208.practice.prepare_ui1.page.base import Base
from study202208.practice.prepare_ui1.page.contact_page import ContactPage


class AddMemberPage(Base):
    #提取元素属性
    _INPUT_USERNAME=(By.CSS_SELECTOR,"#username")
    _INPUT_ACCID=(By.CSS_SELECTOR,"#memberAdd_acctid")
    _INPUT_PHONE=By.CSS_SELECTOR,"#memberAdd_phone"
    _BTN_OK=By.CSS_SELECTOR, ".js_member_editor_form>div:nth-child(1)>.js_btn_save"

    def fillinfo_member(self,*args):
        # ele1=self.find_ele(self._INPUT_USERNAME)
        # ele2=self.find_ele(self._INPUT_ACCTID)
        # ele3=self.find_ele(self._INPUT_PHONE)
        # self.sendkeys_ele(ele1,args[0])
        # self.sendkeys_ele(ele2,args[1])
        # self.sendkeys_ele(ele3,args[2])
        self.sendkeys_ele(args[0],self._INPUT_USERNAME)
        self.sendkeys_ele(args[1],self._INPUT_ACCID)
        self.sendkeys_ele(args[2],self._INPUT_PHONE)
        # ele4 = self.find_ele(self._BTN_OK)
        self.click_ele(self._BTN_OK)
        return ContactPage(self.driver)