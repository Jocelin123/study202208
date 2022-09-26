from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from study202208.conftest import web_env
from study202208.practice.prepare_ui1.page.base_page import BasePage


class TestLitemall:
    # 前置动作
    def setup_class(self):
        self.browser=web_env.get("browser")
        if self.browser=="chrome":
            self.driver=webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    # 后置动作
    def teardown_class(self):
        self.driver.quit()

    # 登录功能
    def test_login(self):
        self.driver.get("http://litemall.hogwarts.ceshiren.com/")
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME,"username").send_keys("manage")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME,"password").send_keys("manage123")
        self.driver.find_element(By.CSS_SELECTOR,".el-button--primary").click()

    def test_add(self):
        self.driver.get("http://litemall.hogwarts.ceshiren.com/")
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("manage")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("manage123")
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        # self.driver.find_element(By.CSS_SELECTOR,".hamburger").click()
        # sleep(1)
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        # ele=self.driver.find_element(By.XPATH,"//*[text()='商品管理']")
        # self.driver.execute_script("arguments[0].click();",ele)
        # sleep(1)
        self.driver.find_element(By.XPATH,"//*[text()='商品类目']").click()
        # sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,".el-icon-edit").click()
        # sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,".el-input__inner").send_keys("0831新增")
        sleep(2)
        # self.driver.find_element(By.CSS_SELECTOR,".el-input--suffix").click()
        # self.driver.find_element(By.XPATH,"//*[text()='一级类目']").click()
        # ele=self.driver.find_element(By.CSS_SELECTOR,".el-select-dropdown__wrap ul li")
        # self.driver.execute_script("arguments[0].click();", ele)
        # sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,".dialog-footer>.el-button--primary").click()
        result=self.driver.find_elements(By.CSS_SELECTOR,".el-table_1_column_2 .cell")
        sleep(2)
        assert result != None

    def test_delete(self):
        self.driver.get("http://litemall.hogwarts.ceshiren.com/")
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("manage")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("manage123")
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-icon-edit").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("0831新增1")
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".dialog-footer>.el-button--primary").click()
        self.driver.find_element(By.XPATH, "//*[text()='0831新增1']//..//..//*[text()='删除']").click()
        # result=self.driver.find_element(By.XPATH,"//*[text()='成功']").text
        # assert result=="成功"
        #必须等待，否则还没删除完时就已经获取到删除的结果了
        sleep(2)
        result=self.driver.find_elements(By.XPATH, "//*[text()='0831新增1']")
        print(result)
        assert result==[]
