#基类，用于测试开始前的准备和测试结束后的相关操作+打印日志
from test.log_util import logger
from script.calculator import Calculator
class Base:
    def setup_class(self):
        logger.info("开始测试")
        self.cal=Calculator()
    def teardown_class(self):
        logger.info("结束测试")
    def setup(self):
        logger.info("开始计算")
    def teardown(self):
        logger.info("结束计算")