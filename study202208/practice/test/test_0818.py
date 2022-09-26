import logging
from loguru import logger
import pytest
import pymysql

# trace=logger.add('./log/runtime_{time}.log')

def test_case1():
    logging.info("case1")

def test_case2(connectDB):
    logging.info("case2")

def test_case3():
    logging.info("case3")

class TestDemo1:
    # @logger.catch()
    def test_search(self):
        # connectDB.execute("SELECT VERSION();")
        # version=connectDB.fetchone()
        # print(version)
        # logging.info("搜索")
        a=1/0
    def test_cart(self):
        # print(login)
        logger.info("购物车")
    def test_order(self):
        logger.info("下单功能")
class TestDemo2:
    def test_case1(self):
        logging.info("class1")

    def test_case2(self):
        logger.info("class2")