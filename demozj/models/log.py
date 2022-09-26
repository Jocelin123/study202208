import logging,time
import os,sys
#获取当前运行脚本的绝对路径（去掉最后两个路径）
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config import setting

if not os.path.exists(setting.LOG_DIR):os.mkdir(setting.LOG_DIR)

class Log():
    def __init__(self):
        self.logname=os.path.join(setting.LOG_DIR,'%s.log'%time.strftime('%Y-%m-%d %H_%M_%S'))
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter=logging.Formatter('[%(asctime)s] [%(filename)s|%(funcName)s] [line:%(lineno)d] %(levelname)-8s: %(message)s')

    def __console(self,level,message):
        fh=logging.FileHandler(self.logname,encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addFilter(ch)

        if level=='info':
            self.logger.info(message)
        if level=='debug':
            self.logger.debug(message)
        if level=='warning':
            self.logger.warning(message)
        if level=='error':
            self.logger.error(message)

        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self,message):
        self.__console('debug',message)

    def info(self,message):
        self.__console('info',message)

    def warning(self,message):
        self.__console('warning',message)

    def error(self,message):
        self.__console('error',message)