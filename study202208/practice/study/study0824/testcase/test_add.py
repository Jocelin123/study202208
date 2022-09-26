import logging

import allure
import pytest

from study202208.practice.study.study0824.base.base import Base
from study202208.practice.study.study0824.config.setting import addfilepath
from study202208.practice.study.study0824.util.open_file import open_file

# print(open_file(addfilepath))
# print(open_file(addfilepath)['success'].values())
# print(type(open_file(addfilepath)))
class Testadd(Base):
    # print(Openfile.open_file(addfilepath)['success'].keys())
    logging.info("准备测试加法模块")
    @allure.story("加法模块测试success")
    @pytest.mark.P0
    # @pytest.mark.flaky(reruns=3,resuns_delay=2)
    # @pytest.mark.run(order=2)
    @pytest.mark.parametrize("x,y,expect",open_file(addfilepath)['success'].values(),ids=open_file(addfilepath)['success'].keys())
    def testcaseadd1(self,x,y,expect):
        logging.info("加法计算开始")
        with allure.step("调用加法函数"):
            result=self.cal.add(x,y)
        logging.info("加法模块断言")
        assert result==expect


    @allure.story("加法模块测试tips")
    @pytest.mark.P1
    # @pytest.mark.run(order=3)
    @pytest.mark.parametrize("x,y,expect",open_file(addfilepath)['tips'].values(),ids=open_file(addfilepath)['tips'].keys())
    def testcaseadd2(self,x,y,expect):
        logging.info("加法计算开始")
        with allure.step("调用加法函数"):
            result=self.cal.add(x,y)
        logging.info("加法模块断言")
        assert result==expect

    @allure.story("加法模块测试error")
    @pytest.mark.P2
    # @pytest.mark.run(order=1)
    @pytest.mark.parametrize("x,y,expect",open_file(addfilepath)['error'].values(),ids=open_file(addfilepath)['error'].keys())
    def testcaseadd3(self,x,y,expect):
        logging.info(f"开始调用函数{x, y, expect}")
        with pytest.raises(TypeError) as e:
            with allure.step(f"步骤一：{x}和{y}开始计算，预期应等于{expect}，打印{e}"):
                result = self.cal.add(x,y)
            logging.info("加法模块断言")
            with allure.step(f"步骤二：断言:{result}等于{expect}"):
                assert result == expect