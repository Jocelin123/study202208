import time
from time import sleep

from loguru import logger
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class TestKeyboard:
    def setup_class(self):
        capability={"paltformName":'windows'}
        self.driver=webdriver.Chrome(desired_capabilities=capability)
        # self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # def teardown_class(self):
    #     self.driver.quit()

    def test_shift(self):
        self.driver.get("https://ceshiren.com")
        self.driver.find_element(By.ID,'search-button').click()
        ele=self.driver.find_element(By.ID,"search-term")
        ActionChains(self.driver).key_down(Keys.SHIFT,ele).\
            send_keys("appium")\
            .perform()
        ele.send_keys("ssss")
        sleep(1)

    def test_sogou1(self):
        self.driver.get("https://www.sogou.com")
        self.driver.find_element(By.ID,"query").send_keys("霍格")
        self.driver.find_element(By.ID, "query").send_keys(Keys.ENTER)
        # ActionChains(self.driver).key_down(Keys.ENTER).perform()
        sleep(1)

    def test_sogou2(self):
        self.driver.get("https://ceshiren.com")
        self.driver.find_element(By.ID, 'search-button').click()
        ele = self.driver.find_element(By.ID, "search-term")
        ActionChains(self.driver).key_down(Keys.SHIFT,ele).\
            send_keys("selenium").key_down(Keys.ARROW_LEFT).\
            key_down(Keys.CONTROL).send_keys('xvvv').key_up(Keys.CONTROL).perform()
        ele.send_keys("wo")
        sleep(2)

    def test_doubleclick(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        ele=self.driver.find_element(By.ID,"primary_btn")
        ActionChains(self.driver).double_click(ele).perform()
        sleep(2)

    def test_draganddrop(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        self.driver.find_element(By.CSS_SELECTOR,".el-icon-star-on").click()
        ele1 = self.driver.find_element(By.CSS_SELECTOR, ".item1")
        ele2=self.driver.find_element(By.CSS_SELECTOR,".item3")
        ActionChains(self.driver).drag_and_drop(ele1,ele2).perform()
        sleep(2)

    def test_xuanfu(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        self.driver.find_element(By.XPATH,"//*[text()='ActionChains2']").click()
        ele1 = self.driver.find_element(By.XPATH, "//*[text()=' 请选择']")
        ActionChains(self.driver).move_to_element(ele1).perform()
        self.driver.find_element(By.XPATH,"//*[text()=' 测开班 ']").click()
        self.driver.find_element(By.CSS_SELECTOR,"[name='dx']").click()
        sleep(2)

    def test_move(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        self.driver.find_element(By.CSS_SELECTOR,"#action_chains2").click()
        ele = self.driver.find_element(By.CSS_SELECTOR, ".menu")
        ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".menu>.options>div:nth-of-type(1)").click()
        sleep(2)

#报错找不到元素问题或者找到了无法点击？？？
    def test_roll(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(10)
        st = time.time()
        while time.time() - st < 10:
            self.driver.execute_script('document.documentElement.scrollTop=10000')
            try:
                sleep(2)
                ele = self.driver.find_element(By.XPATH, "//*[text()='测试管理圆桌讨论会']")
                # self.driver.execute_script("arguments[0].click();", ele)
                # ele.click()
                ActionChains(self.driver).move_to_element(ele).click(ele).perform()
                print("点击成功")
                break
            except Exception as e:
                print(e)
        sleep(3)

#此代码经常遇到元素点击失败的情况
    def test_roll1(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(10)
        st = time.time()
        while time.time() - st < 50:
            self.driver.execute_script('document.documentElement.scrollTop=10000')
            try:
                ele = self.driver.find_element(By.XPATH, "//*[text()='使用显示等待报超时']")
                print('找到了')
                ActionChains(self.driver).scroll_to_element(ele).perform()
                # self.driver.execute_script("arguments[0].click();", ele)
                ele.click()
                print('点击了')
                break
            except Exception as e:
                print(e)
                print("未发现")
        sleep(3)

    def test_roll2(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(10)
        sleep(3)
        self.driver.execute_script("document.querySelector('a[data-topic-id=\'20288\']').scrollIntoView()")
        ele = self.driver.find_element(By.CSS_SELECTOR, "[data-topic-id='20288']")
        # self.driver.execute_script("arguments[0].click();", ele)
        # sleep(3)
        ele.click()
        sleep(3)

    def test_scroll_to_amount(self):
        # 演练环境
        self.driver.get("https://ceshiren.com/")
        # 4.2 之后才提供这个方法
        ActionChains(self.driver).scroll_by_amount(0, 100000).perform()
        sleep(5)

    def test_scoll_to_element(self):
        # 演练环境
        self.driver.get("https://ceshiren.com/")
        # 4.2 之后才提供这个方法
        ele = self.driver.find_element \
            (By.XPATH, "//*[text()='pytest注册命令之后，使用命令时报错了']")
        # ActionChains(self.driver).scroll_to_element(ele).perform()
        ele.click()
        sleep(3)

    def test_frame(self):
        # 演练环境
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element(By.ID, 'draggable').text)
        self.driver.switch_to.parent_frame()


    def test_switchwindow(self):
        # 演练环境
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID,'s-top-loginbtn').click()
        sleep(2)
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__regLink').click()
        sleep(2)
        windowall=self.driver.window_handles
        # print(windowall)
        window2=self.driver.current_window_handle
        # print(window2)
        # print(self.driver.window_handles[-1])
        self.driver.switch_to.window(windowall[-1])
        # window1 = self.driver.current_window_handle
        # print(window1)
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__userName').send_keys('zhuce')
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__phone').send_keys('13100000000')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__password').send_keys('123456')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__verifyCodeSend').click()
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__verifyCode').send_keys('654321')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__isAgree').click()
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__submit').click()
        self.driver.switch_to.window(window2)
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('zjocelin')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys('1986119')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()
        sleep(2)


    def test_loadfile(self):
        self.driver.get("https://image.baidu.com")
        # sleep(2)
        ele=self.driver.find_element(By.CSS_SELECTOR,".st_camera_on")
        self.driver.execute_script("arguments[0].click();", ele)
        sleep(2)
        ele=self.driver.find_element(By.CSS_SELECTOR,"#stfile")
        ele.send_keys("C:\\Users\\lvy\\Pictures\视频项目\\hvV03bKpkLD.jpg")
        sleep(6)

    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame('iframeResult')
        ele1=self.driver.find_element(By.CSS_SELECTOR,'#draggable')
        ele2=self.driver.find_element(By.CSS_SELECTOR,'#droppable')
        ActionChains(self.driver).drag_and_drop(ele1,ele2).perform()
        sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.parent_frame()
        self.driver.find_element(By.CSS_SELECTOR,'#submitBTN').click()
        sleep(3)

    def test_js1(self):
        self.driver.get("https://www.taobao.com/")
        self.driver.execute_script('document.querySelector("#J_SiteNavMytaobao").'
                                   'className="site-nav-menu site-nav-mytaobao site-nav-multi-menu\
                                    J_MultiMenu site-nav-menu-hover"')
        sleep(3)
        self.driver.find_element(By.XPATH,"//*[text()='已买到的宝贝']").click()
        sleep(3)

    def test_js2(self):
        self.driver.get("https://www.taobao.com/")
        self.driver.execute_script('document.querySelector("#J_SiteNavMytaobao").'
                                   'className="site-nav-menu site-nav-mytaobao site-nav-multi-menu\
                                    J_MultiMenu site-nav-menu-hover"')
        sleep(3)
        self.driver.find_element(By.XPATH,"//*[text()='已买到的宝贝']").click()
        sleep(3)


    def test_js3(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID,"kw").send_keys("haha")
        self.driver.execute_script('document.querySelector("#su").click()')
        sleep(3)

    def test_capabilities(self):
        self.driver.get("https://ceshiren.com/")

    def test_practice(self):
        self.driver.get("https://vip.ceshiren.com")
        WebDriverWait(self.driver,10).until(lambda x:x.find_element(By.XPATH,"//*[text()='个人中心']"))
        self.driver.find_element(By.CSS_SELECTOR,".el-menu--inline>li")[1].click()
        sleep(3)

    def test_practice1(self):
        self.driver.get("https://vip.ceshiren.com/#/ui_study")
        ele=self.driver.find_element(By.CSS_SELECTOR,"[frameborder='0']")
        self.driver.switch_to.frame(ele)
        self.driver.find_element(By.CSS_SELECTOR, "#frame_btn").click()
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.parent_frame()
        self.driver.find_element(By.CSS_SELECTOR,".el-icon-remove").click()
        self.driver.find_elements(By.CSS_SELECTOR,".el-menu--inline>li")[1].click()
        self.driver.find_element(By.CSS_SELECTOR,"#openWindows").click()
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        self.driver.find_element(By.XPATH,"//*[text()='练习按钮']").click()
        self.driver.switch_to.alert.dismiss()
        self.driver.switch_to.window(handles[0])
        self.driver.find_element(By.XPATH, "//*[text()='文件下载']").click()
        ele=self.driver.find_element(By.CSS_SELECTOR, ".el-upload__input")
        ele.send_keys("D:\\1.jpeg")
        WebDriverWait(self.driver, 20).until(lambda x:x.find_element(By.XPATH,"//*[text()='1.jpeg']"))
        # sleep(3)

    def test_loadfile(self):
        self.driver.get("https://image.baidu.com")
        # self.driver.find_element(By.XPATH, "//*[text()='文件下载']").click()D:\\1.jpeg
        # ele = self.driver.find_element(By.CSS_SELECTOR,".st_camera_on")
        # ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.find_element(By.CSS_SELECTOR,'.st_camera_off').click()
        self.driver.find_element(By.CSS_SELECTOR, "#stfile").send_keys("C:\\Users\\lvy\\Pictures\\视频项目\\123.jpg")
        # WebDriverWait(self.driver, 20).until(lambda x:x.find_element(By.XPATH,"//*[text()='123.jpg']"))