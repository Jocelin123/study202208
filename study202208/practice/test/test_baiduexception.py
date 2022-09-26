import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

def Exception1(func):
    def inner(*args,**kwargs):
    #获取被装饰方法的driver，即实例对象;前提条件：1.被装饰的方法是一个实例方法，2.实例需要有实例变量self.driver
        driver=args[0].driver
        try:
            return func(*args,**kwargs)
        except Exception:
            print("出现异常处理")
            timestamp = int(time.time())
            imagepath = f"./image/image_{timestamp}.PNG"
            pagesourcepath = f"./htmlsource/source_{timestamp}.html"
            driver.save_screenshot(imagepath)
            with open(pagesourcepath, "w", encoding='u8') as f:
                f.write(driver.page_source)
            allure.attach.file(imagepath, name="测试截图", attachment_type=allure.attachment_type.PNG, extension=".png")
            allure.attach.file(pagesourcepath, name="html源码", attachment_type=allure.attachment_type.TEXT)
            raise Exception
    return inner

class TestBaiduException:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://baidu.com")

    def teardown_class(self):
        self.driver.quit()

    @Exception1
    def test_baidu(self):
        self.driver.find_element(By.ID,"su1").click()
