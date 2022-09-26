import json

import pymysql
import requests
# from requests_xml import XMLSession
from hamcrest import *
from jsonpath import jsonpath
from jsonschema import validate


class TestRequests:
    def test_requests(self):
        r=requests.get('http://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code==200

    def test_get_query(self):
        payload={
            'a': 1,
            'name': 'seveniruby'
        }
        r=requests.get("http://httpbin.testing-studio.com/get",params=payload)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_post_form(self):
        payload={
            'a': 1,
            'name': 'seveniruby'
        }
        r=requests.post("http://httpbin.testing-studio.com/post",data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            'a': 1,
            'name': 'seveniruby'
        }
        r = requests.post("http://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_post_xml(self):
        xml = """<?xml version='1.0' encoding='utf-8'?><a>123</a>"""
        headers = {'Content-Type': 'application /xml'}
        r = requests.post('http://httpbin.org/post', data=xml, headers=headers)
        print(r.text)

#报错
    # def test_xml(self):
    #     session = XMLSession()
    #     r = session.get('https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss')
    #     print(r.xml.links)#按原样获取页面上所有链接的列表（这仅适用于RSS提要或碰巧具有“link”元素的其他提要）
    #     item = r.xml.xpath('//item', first=True)
    #     print(item.text)#获取元素的文本内容

    def test_hamcrast(self):
        payload = {
            'a': 1,
            'name': 'seveniruby'
        }
        r = requests.post("http://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert_that(r.json()['json']['name'],equal_to('seveniruby'))

    def test_jsonpath(self):
        r = requests.get("http://home.testing-studio.com/categories.json")
        assert jsonpath(r.json(),'$..name')[0]=='提问区'

    def test_get_login_jsonschema(self):
        url="http://home.testing-studio.com/categories.json"
        data=requests.get(url).json()
        schema=json.load(open("./data/topic_schema.json"))
        validate(data,schema=schema)

    def test_proxies(self):
        proxy={
            'http':'http://127.0.0.1:8080',
            'https':'http://127.0.0.1:8080'
        }
        data={"a":1}
        requests.post('http://httpbin.testing-studio.com/post',proxies=proxy,json=data,verify=False,timeout=3)

    def test_proxy_form(self):
        proxy = {
            'http': 'http://127.0.0.1:8080',
            'https': 'http://127.0.0.1:8080'
        }
        data = {"a": 1}
        requests.post('http://httpbin.testing-studio.com/post', proxies=proxy, data=data, verify=False)

    def get_connect(self):
        connect=pymysql.connect(
            host="litemall.hogwarts.ceshiren.com",
            port=13306,
            user="test",
            password="test123456",
            database="litemall",
            charset="utf8mb4"
        )
        return connect

    def execuate_sql(self,sql):
        connect=self.get_connect()
        cursor=connect.cursor()
        cursor.execute(sql)
        record=cursor.fetchone()
        return record

    def test_mysql(self):
        sql="select * from litemall_cart where user_id=1 and deleted=0"
        value=self.execuate_sql(sql)
        print(value)
        assert value