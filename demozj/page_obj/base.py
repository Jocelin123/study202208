import os,sys
#模块和自己写的脚本不在同一个目录下，在脚本开头加sys.path.append(‘xxx’)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchFrameException,NoSuchWindowException,NoAlertPresentException,NoSuchElementException
import configparser
from models.log import Log

con=configparser.ConfigParser()
con.read(setting.CONFIG_DIR,encoding='utf-8')
login_url=con.get('WebURL','URL')
log=Log()


class Page(object):
    """
    Page封装所有页面都公用的方法，例如driver, url ,FindElement等
    初始化driver、url、pagetitle等
    实例化Page类时，最先执行的就是__init__方法，该方法的入参，其实就是Page类的入参。
    __init__方法不能有返回值，只能返回None
    self只实例本身，相较于类Page而言。
    """
    def __init__(self,selenium_driver,base_url=login_url,parent=None):
        self.base_url=base_url
        self.driver=selenium_driver
        self.parent=parent
        self.timeout=10

    def on_page(self):
        return self.driver.current_url==(self.base_url+self.url)

    def _open(self,url):
        url=self.base_url+url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            log.error('{0}页面中未找到{1}元素'.format(self,loc))

    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            log.error('{0}页面中未找到{1}元素'.format(self,loc))

    def script(self,src):
        return self.driver.execute_script(src)

    def send_key(self,loc,vaule,clear_first=True,click_first=True):
        try:
            loc=getattr(self,'_%s'%loc)
            if click_first:
                self.find_elements(*loc).click()
            if clear_first:
                self.find_elements(*lco).clear()
                self.find_elements(*loc).send_keys(vaule)
        except AttributeError:
            log.error('%s页面中未找到%s元素'%(self,loc))

    def switch_frame(self,loc):
        try:
            return self.driver.switch_to_frame(loc)
        except NoSuchFrameException as msg:
            log.error('查找iframe异常-》{0}'.format(msg))

    def switch_windows(self,loc):
        try:
            return self.driver.switch_to_window(loc)
        except NoSuchWindowException as msg:
            log.error('查找window窗口句柄handle异常-》{0}'.format(msg))

    def switch_alert(self):
        try:
            return self.driver.switch_to_alert(loc)
        except NoAlertPresentException as msg:
            log.error('查找alert弹出框异常-》{0}'.format(msg))
