from selenium.webdriver.common.by import By

from study202208.practice.prepare_ui1.page.base import Base


class DeptPage(Base):
    _INPUT_DEPT=By.CSS_SELECTOR, ".inputDlg_item input"
    _SELECT_DEPT=By.XPATH, "//*[text()='选择所属部门']"
    _SELECT_DEPT1=By.XPATH, "//div[@class='inputDlg_item']//a[text()='测试开发1']"
    _BTN_OK=By.XPATH, "//a[text()='确定']"
    def fillinto_dept(self,deptname):
        self.sendkeys_ele(deptname,self._INPUT_DEPT)
        self.click_ele(self._SELECT_DEPT)
        self.click_ele(self._SELECT_DEPT1)
        self.click_ele(self._BTN_OK)
        from study202208.practice.prepare_ui1.page.contact_page import ContactPage
        return ContactPage(self.driver)