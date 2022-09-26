import pytest


def check_aaa():
    print("test_xfail1方法执行")
    pytest.xfail(reason="该功能尚未完成")
    assert 2==2