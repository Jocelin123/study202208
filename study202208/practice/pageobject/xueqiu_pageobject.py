from selenium import webdriver
from selenium.webdriver.common.by import By


class XueQiuPO:
    _INPUT_SEARCH = (By.NAME, "q")
    _BUTTON_SEARCH = (By.CSS_SELECTOR, "i.search")
    _SPAN_STOCK = (By.XPATH, "//table//strong")
    def __init__(self):
        # 初始化浏览器
        self.driver = webdriver.Chrome()
        self.driver.get("https://xueqiu.com/")
        self.driver.implicitly_wait(3)
    def search_stock(self,stock_name:str):
        self.driver.find_element(self._INPUT_SEARCH).send_keys(stock_name)
        self.driver.find_element(self._BUTTON_SEARCH).click()
        name = self.driver.find_element(self._SPAN_STOCK).text
        return name