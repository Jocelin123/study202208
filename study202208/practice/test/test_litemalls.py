import time
from time import sleep

from loguru import logger
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class TestLitemall:
    # 前置动作
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("http://litemall.hogwarts.ceshiren.com/")
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("manage")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("manage123")
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()

    # 后置动作
    def teardown_class(self):
        self.driver.quit()

        def get_sreen(self):
        timestamp=int(time.time())
        imagepath=f"./image/iamge_{timestamp}.PNG"
        self.driver.save_screenshot(imagepath)
        allure.attach.file(imagepath,name="测试截图",
                           attachment_type=allure.attachment_type.PNG,extension=".png")

    def test_add(self):
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH,"//*[text()='商品类目']").click()
        self.driver.find_element(By.CSS_SELECTOR,".el-icon-edit").click()
        self.driver.find_element(By.CSS_SELECTOR,".el-input__inner").send_keys("0831新增")
        # sleep(2)
        #显示等待优化方案1
        # ele=WebDriverWait(self.driver, 10).until(
        #         expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".dialog-footer .el-button--primary"))
        #     )
        # ele.click()
        # ActionChains(self.driver).move_to_element(ele).click(ele).perform()
        # 显示等待优化方案2
        def contions1(by,element,max=5):
            def _inner(driver):
                count=0
                while count<max:
                    count += 1
                    try:
                        self.driver.find_element(by,element).click()
                        return True
                    except Exception:
                        logger.debug("点击发生错误")
                raise Exception("超过最大点击次数")
            return _inner
        WebDriverWait(self.driver,10).until(contions1(By.CSS_SELECTOR,".dialog-footer .el-button--primary"))
        # self.driver.execute_script("arguments[0].click();", ele)
        result=self.driver.find_elements(By.CSS_SELECTOR,".el-table_1_column_2 .cell")
        self.driver.find_element(By.XPATH, "//*[text()='0831新增']//..//..//*[text()='删除']").click()
        self.get_sreen()
        logger.debug("断言开始")
        assert result != None

    def test_delete(self):
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-icon-edit").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys("0831新增1")
        ele=WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".dialog-footer>.el-button--primary"))
            )
        # ele.click()
        self.driver.execute_script("arguments[0].click();", ele)
        self.driver.find_element(By.XPATH, "//*[text()='0831新增1']//..//..//*[text()='删除']").click()
        # result1=self.driver.find_element(By.XPATH,"//*[text()='成功']").text
        # assert result1=="成功"
        #必须等待，否则还没删除完时就已经获取到删除的结果了,只要新增元素在页面任意元素找不到即可
        # sleep(2)
        WebDriverWait(self.driver, 10).until_not(
            expected_conditions.visibility_of_any_elements_located((By.XPATH, "//*[text()='0831新增1']"))
            )
        result=self.driver.find_elements(By.XPATH, "//*[text()='0831新增1']")
        self.get_sreen()
        # print(result)
        assert result==[]
