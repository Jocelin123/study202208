import os

import allure
import pytest
import yaml

from study202208.practice.study.study0818.base.base import Base
from study202208.test.log_util import logger



@allure.feature("加法计算模块")
class TestAdd(Base):
    logger.info("读取yaml文件的测试数据")
    path = os.path.dirname(os.path.dirname((os.path.abspath(__file__)))) + '\\data'
    print(f"我要打印：{path}")
    with open(path+'\\adddata.yaml') as f:
        data=yaml.safe_load(f)
        print(data)

    logger.info("准备执行加法成功用例")
    @allure.story("加法成功用例")
    @pytest.mark.P0
    @pytest.mark.parametrize('x,y,expect',data['success'].values(),ids=data['success'].keys())
    def test_add0(self,x,y,expect):
        logger.info('调用计算')
        with allure.step(f"步骤一：{x}和{y}开始计算，预期应等于{expect}"):
            result=self.cal.add(x,y)
        logger.info('断言')
        with allure.step(f"步骤二：断言:{result}等于{expect}"):
            assert result==expect

    logger.info("准备执行加法提示用例")
    @allure.story("加法提示用例")
    @allure.step("加法测试步骤")
    @pytest.mark.P1
    @pytest.mark.parametrize('x,y,expect',data['tips'].values(),ids=data['tips'].keys())
    def test_add1(self,x,y,expect):
        logger.info('调用计算')
        with allure.step(f"步骤一：{x}和{y}开始计算，预期应等于{expect}"):
            result=self.cal.add(x,y)
        logger.info('断言')
        with allure.step(f"步骤二：断言:{result}等于{expect}"):
            assert result==expect

    logger.info("准备执行加法报错用例")
    @allure.story("加法报错用例")
    @pytest.mark.P2
    @pytest.mark.parametrize('x,y,expect',data['error'].values(),ids=data['error'].keys())
    def test_add2(self,x,y,expect):
        logger.info(f'调用计算{x, y, expect}')
        with pytest.raises(TypeError) as e:
            with allure.step(f"步骤一：{x}和{y}开始计算，预期应等于{expect}，打印{e}"):
                result=self.cal.add(x,y)
            logger.info('断言')
            with allure.step(f"步骤二：断言:{result}等于{expect}"):
                assert result==expect