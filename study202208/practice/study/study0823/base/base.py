from study202208.script.calculator import Calculator


class Base:
    def setup_class(self):
        self.cal = Calculator()
        print("开始测试")

    def teardown_class(self):
        print("清理所有测试灵气")