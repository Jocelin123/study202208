from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCeshiren:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        # self.driver.get("https://ceshiren.com/search?expanded=true")
        self.driver.get("https://ceshiren.com")

    def teardown(self):
        self.driver.close()

    # def test_search1(self):
    #     self.driver.find_element(By.CSS_SELECTOR,"[placeholder='搜索']").send_keys("appium")
    #     self.driver.find_element(By.CSS_SELECTOR,".search-cta").click()
    #     web_element=self.driver.find_element(By.CSS_SELECTOR,".topic-title")
    #     print(web_element)
    #     assert "appium" in web_element.text.lower()
    #
    # def test_search2(self):
    #     self.driver.find_element(By.CSS_SELECTOR,"[placeholder='搜索']").send_keys("selenium")
    #     self.driver.find_element(By.CSS_SELECTOR,".search-cta").click()
    #     web_element=self.driver.find_element(By.CSS_SELECTOR,".topic-title")
    #     print(web_element)
    #     assert "selenium" in web_element.text.lower()

    def test_click1(self):
        # self.driver.find_element(By.CSS_SELECTOR,'[title="有新帖子的话题")').click()
        self.driver.find_element(By.XPATH,"//text()='最新'").click()
        sleep(2)