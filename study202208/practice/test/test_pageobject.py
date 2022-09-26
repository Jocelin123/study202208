# test_search.py

from selenium import webdriver
from selenium.webdriver.common.by import By

from study202208.practice.pageobject.xueqiu_pageobject import XueQiuPO


class TestSearch():
    def test_search(self):
        name=XueQiuPO().search_stock("阿里巴巴-SW")
        assert name == "阿里巴巴-SW"