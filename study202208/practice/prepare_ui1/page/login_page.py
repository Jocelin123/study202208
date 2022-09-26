import time

import yaml

from study202208.practice.prepare_ui1.page.base import Base
from study202208.practice.prepare_ui1.page.home_page import HomePage


class LoginPage(Base):
    # _BASE_URL="https://work.weixin.qq.com/wework_admin/frame"
    def login(self):
        self.driver.delete_all_cookies()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        with open("../data/cookies.yaml", "r", encoding='u8') as f:
            cookies = yaml.safe_load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        return HomePage(self.driver)

    def close_browser(self):
        return self.driver.quit()

