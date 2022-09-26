import time

from faker import Faker
import yaml
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestAddMember:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        with open("../data/cookies.yaml", "r", encoding='u8') as f:
            cookies = yaml.safe_load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()

    def setup(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        fake = Faker("zh-CN")
        self.name = fake.name()
        self.ssn = fake.ssn()
        self.phone_number = fake.phone_number()

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    #加类型提示方便联动出对应的方法和属性
    def test_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR,"#menu_contacts").click()
        def conditon1(by,ele):
            def _inner(driver:WebDriver):
                try:
                    driver.find_element(by,ele).click()
                    return driver.find_element(By.CSS_SELECTOR,"#username")
                except:
                    return False
            return _inner
        WebDriverWait(self.driver,60).until(conditon1(By.CSS_SELECTOR,".js_party_info .js_has_member>div:nth-child(1) .js_add_member"))
        self.driver.find_element(By.CSS_SELECTOR,"#username").send_keys(self.name)
        self.driver.find_element(By.CSS_SELECTOR,"#memberAdd_acctid").send_keys(self.ssn)
        self.driver.find_element(By.CSS_SELECTOR,"#memberAdd_phone").send_keys(self.phone_number)
        self.driver.find_element(By.CSS_SELECTOR,".js_member_editor_form>div:nth-child(1)>.js_btn_save").click()
        time.sleep(2)
        ele=self.driver.find_element(By.XPATH,"//*[text()='保存成功']")
        assert ele.text=="保存成功"

    def test_add_member1(self):
        self.driver.find_element(By.CSS_SELECTOR,"#menu_contacts").click()
        ele=(By.CSS_SELECTOR,"#memberSearchInput")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(ele))
        self.driver.find_element(By.CSS_SELECTOR, ".js_party_info .js_has_member>div:nth-child(1) .js_add_member").click()
        self.driver.find_element(By.CSS_SELECTOR,"#username").send_keys(self.name)
        self.driver.find_element(By.CSS_SELECTOR,"#memberAdd_acctid").send_keys(self.ssn)
        self.driver.find_element(By.CSS_SELECTOR,"#memberAdd_phone").send_keys(self.phone_number)
        self.driver.find_element(By.CSS_SELECTOR,".js_member_editor_form>div:nth-child(1)>.js_btn_save").click()
        time.sleep(2)
        ele=self.driver.find_element(By.XPATH,"//*[text()='保存成功']")
        assert ele.text=="保存成功"

    def test_add_member2(self):
        self.driver.find_element(By.CSS_SELECTOR,"#menu_contacts").click()

        def conditon1(by, ele, max=10):
            def _inner(driver: WebDriver):
                count = 0
                while count < max:
                    count += 1
                    try:
                        driver.find_element(by, ele).click()
                        return driver.find_element(By.CSS_SELECTOR, "#username")
                    except:
                        return False
            return _inner

        WebDriverWait(self.driver, 60).until(
            conditon1(By.CSS_SELECTOR, ".js_party_info .js_has_member>div:nth-child(1) .js_add_member"))
        self.driver.find_element(By.CSS_SELECTOR,"#username").send_keys(self.name)
        self.driver.find_element(By.CSS_SELECTOR,"#memberAdd_acctid").send_keys(self.ssn)
        self.driver.find_element(By.CSS_SELECTOR,"#memberAdd_phone").send_keys(self.phone_number)
        self.driver.find_element(By.CSS_SELECTOR,".js_member_editor_form>div:nth-child(1)>.js_btn_save").click()
        time.sleep(2)
        ele=self.driver.find_element(By.XPATH,"//*[text()='保存成功']")
        assert ele.text=="保存成功"

    def test_add_dept(self):
        #点击通讯录标签
        self.driver.find_element(By.CSS_SELECTOR,"#menu_contacts").click()
        #点击添加按钮
        self.driver.find_element(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        # 点击添加部门按钮
        self.driver.find_element(By.CSS_SELECTOR,".js_create_party").click()
        #输入信息
        self.driver.find_element(By.CSS_SELECTOR,".inputDlg_item input").send_keys("新增部门1")
        self.driver.find_element(By.XPATH,"//*[text()='选择所属部门']").click()
        self.driver.find_element(By.XPATH, "//div[@class='inputDlg_item']//a[text()='测试开发1']").click()
        self.driver.find_element(By.XPATH, "//a[text()='确定']").click()
        ele = self.driver.find_element(By.XPATH, "//*[text()='新建部门成功']")
        assert ele.text == "新建部门成功"



