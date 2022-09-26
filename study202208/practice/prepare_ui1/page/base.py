from loguru import logger
from selenium import webdriver
from study202208.conftest import web_env


class Base:
    # _BASE_URL=""
    def __init__(self,base_driver=None):
        #初始化driver，如果存在，就复用driver，如果不存在或执行过程中driver突然崩溃或连接断开，则拿到的是None并创建一个新driver
        if base_driver:
            self.driver=base_driver
        else:
            self.driver=webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
        # if not self.driver.current_url.startswith("http"):
            # 如果打开的页面不是http开头的页面，就打开我们指定的URL(self._BASE_URL)
            #print能成功打印网址，为何logger不行？
            # print(self._BASE_URL)
            # logger(self._BASE_URL)
            # self.driver.get(self._BASE_URL)
        # self.browser = web_env.get("browser")
        # if self.browser == "chrome":
        #     self.driver = webdriver.Chrome()
        # else:
        #     self.driver = webdriver.Firefox()
        # self.driver.implicitly_wait(3)
        # self.driver.maximize_window()
    #if语句是为了支持传两个参数，或一个参数为元素

    def find_ele(self,by,ele=None):
        """查找单个元素"""
        if ele:
            return self.driver.find_element(by,ele)
        else:
            return self.driver.find_element(*by)

    def find_eles(self,by,ele=None):
        """查找多个元素"""
        if ele:
            return self.driver.find_element(by,ele)
        else:
            return self.driver.find_element(*by)

    def click_ele(self,ele):
        ele1=self.find_ele(ele)
        return ele1.click()

    #value=None极其重要
    def sendkeys_ele(self,text,by,value=None):
        ele=self.find_ele(by,value)
        ele.clear()
        return ele.send_keys(text)

    # def sendkeys_ele(self,text,by,value=None):
    #     ele=self.find_ele(by,value)
    #     ele.clear()
    #     return ele.send_keys(text)

    def get_text(self,ele):
        return self.find_ele(ele).text