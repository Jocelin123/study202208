from time import sleep

from study202208.script.calculator import Calculator


class Base:
    def setup_class(self):
        self.cal=Calculator()
        print("测试开始")

    def setup(self):
        sleep(1)
        print("测试前的准备")

    def tearup(self):
        print("测试结束后的数据清理")