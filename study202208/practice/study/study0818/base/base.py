import os
import sys

import pytest
import yaml

from study202208.script.calculator import Calculator

# path = os.path.dirname(os.path.dirname((os.path.abspath(__file__)))) + '\\data'
# print(path)
# with open(path + '\\adddata.yaml') as f:
#     data = yaml.safe_load(f)
#     print(data['success'].values())


class Base:
    def setup_class(self):
        self.cal=Calculator()
        print("测试开始")

    def teardown_class(self):
        print("测试结束")

    def setup_method(self):
        print("计算开始")

    def teardown_method(self):
        print("计算结束")