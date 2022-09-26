# import sys


# def inc(x):
#     return x + 1

# def test_answer():
#     assert inc(3) == 5,"结果为假"
#
# def test_str():
#     assert "abc" in "abcd","字符串测试不在里面"
#
# def test_str1():
#     assert ('linux' in sys.platform),"该代码只能在linux下运行"
import pytest
import math

# search_list=[("3+5",8),("2+5",7),("7+5",11)]
# @pytest.mark.parametrize('name1,expected',search_list,ids=["用例1","用例2","用例3"])
# def test_search(name1,expected):
#     assert eval(name1) == expected
# @pytest.mark.parametrize("wd",['appium','selenium','pytest'])
# @pytest.mark.parametrize("code",['uft-8','gbk','gb2312'])
# def test_dkej(wd,code):
#     print(f"wd:{wd},code:{code}")
# def double(x):
#     return  x+x
# def minus(x):
#     return -x
# @pytest.mark.int
# def test_int():
#     print("test int")
#     assert 2==double(1)
# @pytest.mark.minus
# def test_minus():
#     print("test int")
#     assert -2==minus(2)
# def check_login():
#     return True
# @pytest.mark.skip
# def test_aaa():
#     print("代码未开发完")
#     assert True
# @pytest.mark.skipif(not check_login(),reason="未登录")
# def test_bbb():
#         print("执行用例")
# def test_bbb1():
#     if not check_login():
#         pytest.skip("未登录")

# @pytest.mark.xfail(reason="bug 110")
def test_aaa():
    print("test_xfail1方法执行")
    pytest.xfail(reason="该功能尚未完成")
    assert 2==2

