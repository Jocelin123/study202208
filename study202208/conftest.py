import os
import sys
from typing import List, Optional

import pytest
import pymysql

web_env={}
# @pytest.fixture(scope="module",params=['user','name'])
# def login(request):
#     print("完成登录操作")
#     print(f"用户名：{request.param}")
#     yield request.param
#     print("退出登录")
import yaml
from _pytest.config import Config


@pytest.fixture(scope="module")
def login():
    print("完成登录操作")
    yield
    print("退出登录")

@pytest.fixture(scope="session")
def connectDB():
    print("开始数据库连接")
    conn = pymysql.connect(host='mysql.hogwarts.ceshiren.com',
                           user='stu',
                           password='hogwarts_stu',
                           charset="utf8mb4")
    cursor=conn.cursor()
    yield cursor
    conn.close()
    print("关闭数据库连接")

# def pytest_runtest_setup(item: "Item") -> None:
#     print("开始吧")
#
# def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
#     print("结束吧")

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name=item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid=item.nodeid.encode('utf-8').decode('unicode-escape')
    # items.reverse()

def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    mygroup=parser.getgroup("zj")
    mygroup.addoption("--envi",
                      default='test',
                      dest='envion',
                      help='set your run environment')
    mygroup.addoption("--browser",
                      default='chrome',
                      dest='browser',
                      help='select your browser')

#Config导入_pytest的Config
def pytest_configure(config:Config):
    browser=config.getoption("browser")
    web_env["browser"]=browser


@pytest.fixture(scope='session')
def cmdoption(request):
    my_dir = os.path.dirname(os.path.abspath(__file__)) + "\data"
    sys.path.append(my_dir)
    myenv=request.config.getoption("--envi",default='test')
    if myenv == 'test':
        datapath=my_dir+"\\test\data.yaml"
        # datas="testest"
    elif myenv == 'dev':
        datapath=my_dir+"\dev\data.yaml"
        # datas="devdev"

    with open(datapath) as f:
        datas=yaml.safe_load(f)
    return myenv,datas