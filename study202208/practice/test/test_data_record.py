from loguru import logger
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDataRecord:
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    def test_log_data_record(self):
        self.driver.get("https://www.sogou.com")
        search_content="霍格沃兹测试开发"
        self.driver.find_element(By.CSS_SELECTOR,'#query').send_keys(search_content)
        logger.debug(f"搜索的信息是{search_content}")
        self.driver.find_element(By.CSS_SELECTOR,'#stb').click()
        result=self.driver.find_element(By.CSS_SELECTOR,'em')
        logger.info(f"实际结果为{result.text},预期结果为{search_content}")
        assert result.text==search_content
        self.driver.save_screenshot("./image/res.jpg")
        sleep(2)

    def test_pagesource(self):
        self.driver.get("https://www.ceshiren.com")
        with open("./htmlsource/record.html","w",encoding="u8") as f:
            f.write(self.driver.page_source)

