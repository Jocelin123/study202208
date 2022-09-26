'''
#加法模块+allure装饰器用法
import logging
from study202208.test.log_util import logger
import pytest
import yaml
from study202208.script.calculator import Calculator
import sys
import os
from study202208.test.base.base import Base
import allure

my_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"\data"
sys.path.append(my_dir)
my_dir1=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))+"\\test"+"\\base"
sys.path.append(my_dir1)
@allure.feature("加法模块")
class TestAdd(Base):
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("加法测试P0")
    @pytest.mark.P0
    @pytest.mark.parametrize('x,y,expect',yaml.safe_load(open(my_dir+"/adddata.yaml")))
    def test_add1(self,x,y,expect):
        # with allure.step():
        # self.cal = Calculator()
        logger.info(f"输入数据：{x},{y},期望结果：{expect}")
        with allure.step("相加操作"):
            result=self.cal.add(x,y)
        with allure.step("相加操作"):
            assert result==expect
        logger.info(f"实际结果：{result}")
        open(my_dir + "/adddata.yaml").close()

    @allure.story("加法测试P1")
    @pytest.mark.P1
    @pytest.mark.parametrize('x,y,expect',[["文",9.3,"参数大小超出范围"],["",9.3,"参数大小超出范围"]])
    def test_add2(self,x,y,expect):
        with pytest.raises(TypeError) as e:
            # self.cal = Calculator()
            logger.info(f"输入数据：{x},{y},期望结果：{expect}")
            result=self.cal.add(x,y)
            assert result==expect
            logger.info(f"实际结果：{result}")
            open(my_dir + "/adddata.yaml").close()

    @allure.story("加法测试P2")
    @pytest.mark.P2
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("定义成功")
    def test_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登录页面"):
            print("登录页面")
            allure.attach.file("D:\吕扬420117198710240832.jpg",
                               name="截图",attachment_type=allure.attachment_type.JPG,extension=".jpg")
        with allure.step("步骤3：输入用户信息"):
            # assert 1==2
            allure.attach("这是一段文本信息",name="文本展示")
            print("输入用户名和密码")
        with allure.step("步骤4：进入成功页面"):
            allure.attach('<a href="/" data-auto-route="true"><img src="https://ceshiren.com/uploads/default/original/1X/809c63f904a37bc0c6f029bbaf4903c27f03ea8a.png" alt="测试人社区" id="site-logo" class="logo-big"></a>',
                          name="html展示",attachment_type=allure.attachment_type.HTML)
            print("登录成功")

    @allure.story("加法测试P2")
    @pytest.mark.P2
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("定义失败")
    def test_failure(self):
        assert False

    @allure.story("加法测试P2")
    @pytest.mark.P2
    @allure.story("定义跳过")
    def test_skip(self):
        pytest.skip("for a reason!")

    # @allure.story("加法测试P2")
    # @pytest.mark.P2
    # @allure.story("定义异常")
    # def test_broken(self):
    #     raise Exception("oops")

    # def test_raise():
    #     with pytest.raises(ValueError, match='must be 0 or None'):
    #         raise ValueError("value must be 0 or None")
    #
    # def test_raise1():
    #     with pytest.raises(ValueError) as exc_info:
    #         raise ValueError("value must be 42")
    #     assert exc_info.type is ValueError
    #     assert exc_info.value.args[0] == "value must be 42"

    # @pytest.mark.div
    # @pytest.mark.parametrize('x,y,z', yaml.safe_load(open(my_dir + "/adddata.yaml")))
    # def test_div1(self, x, y, z):
    #     self.cal = Calculator()
    #     result = self.cal.div(x, y)
    #     expect = z
    #     assert result == expect
    '''
