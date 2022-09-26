import pytest

# def test_raise():
#     with pytest.raises((ZeroDivisionError,ValueError)):
#         raise ZeroDivisionError("除数不能为0")
#
# def test_raise1():
#     with pytest.raises(ValueError) as exc_info:
#         raise ValueError("value must be 42")
#         print('1')
#         print(exc_info)
#         print('2')
#     assert exc_info.type is ValueError
#     assert exc_info.value.args[0]=="value must be 42"
# import yaml
#
#
# class TestDemo:
#     @pytest.mark.parametrize("env", yaml.safe_load(open("./my.yaml")))
#     def test_demo(self, env):
#         print(env)
#         print(yaml.safe_load(open("./my.yaml")))
#         open("./my.yaml").close()
#         print(open("./my.yaml").closed)
        # if "test" in env:
        #     print(type(env))
        #     print("这是测试环境")
        # elif "dev" in env:
        #     print(type(env))
        #     print("这是开发环境")
        # else:
        #     print("都不是")

    # search_list = [("3+5", 8), ("2+5", 7), ("7+5", 11)]
    #
    # @pytest.mark.parametrize('name1,expected', search_list)
    # def test_search(self,name1, expected):
    #     print(name1, expected)
import re
import pytest_assume
def scramble(s1: str, s2: str)  -> bool:
    # your code here
    if re.search(s1,s2) is None:
        return False
    else:
        return True
# with pytest_assume: assert scramble('rkqodlw', 'world') ==  True
# with pytest_assume: assert scramble('cedewaraaossoqqyt', 'codewars') == True
# with pytest_assume: assert scramble('katas', 'steak') == False
# with pytest_assume: assert scramble('scriptjava', 'javascript') == True
# with pytest_assume: assert scramble('scriptingjava', 'javascript') == True
# with pytest_assume: assert scramble('scriptingjav', 'javascript') == False