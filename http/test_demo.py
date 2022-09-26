import json

import requests
import jsonpath
from hamcrest import *

class TestDemo:
    # def test_get(self):
    #     r=requests.get('https://httpbin.testing-studio.com/get')
    #     # print(r.status_code)
    #     # print(r.headers['content-type'])
    #     # print(r.json())
    #     assert r.status_code==200
    #
    # def test_query(self):
    #     payload={
    #         "level":1,
    #         "name":"seveniruby"
    #     }
    #     r = requests.get('https://httpbin.testing-studio.com/get',params=payload)
    #     print(r.text)
    #     assert r.status_code==200
    #
    # def test_form(self):
    #     payload={
    #         "level":1,
    #         "name":"seveniruby"
    #     }
    #     r = requests.post('https://httpbin.testing-studio.com/post',data=payload)
    #     print(r.text)
    #     assert r.status_code==200
    #
    # def test_fileload(self):
    #     files={'file':open('report.xls','rb')}
    #     r = requests.post('https://httpbin.testing-studio.com/post',files=files)
    #     print(r.text)
    #     assert r.status_code==200
    #
    # def test_header(self):
    #     headers={'User-Agent':'my-app/0.0.1'}
    #     r = requests.post('https://httpbin.testing-studio.com/post',headers=headers)
    #     print(r.text)
    #     assert r.status_code==200
    #
    # def test_json(self):
    #     json={'Host':'www.baidu.com'}
    #     r = requests.post('https://httpbin.testing-studio.com/post',json=json)
    #     print(r.text)
    #     assert r.json()['json']['Host']=='www.baidu.com'
    #
    # # def test_request(self):
    # #     r = requests.post('https://httpbin.testing-studio.com/post')
    # #     print(r.raw.read(10))
    # #     assert r.status_code==200
    #
    # def test_xml(self):
    #     xml="""<?xml version='1.0' encoding='utf-8'?>
    #            <a>6</a>"""
    #     headers={'Content-Type':'application/xml'}
    #     r = requests.post('https://httpbin.testing-studio.com/post',data=xml,headers=headers)
    #     print(r.text)
    #     assert r.status_code==200

    # def test_hogwarts_json(self):
    #     r = requests.get('https://ceshiren.com/categories.json')
    #     print(r.text)
    #     # assert r.status_code==200
    #     # assert r.json()['category_list']['categories'][0]['name']=="提问区"
    #     # assert jsonpath.jsonpath(r.json(),'$..name')[0]=="提问区"
    #     assert_that(jsonpath.jsonpath(r.json(),'$..name')[0],has_length(3))

    def test_xml_assert(self):
        # from requests_xml import XMLSession
        # session = XMLSession()
        # r = session.get('https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss')
        # print('start')
        # print(r.xml.links)
        # print('end')
        # item = r.xml.xpath('//item', first=True)
        # print('start')
        # print(item.text)
        # print('end')
        # item = r.xml.xpath('//rss', first=True)
        # print('start')
        # print(item.attrs)
        # print('end')
        # doc = """
        # <employees>
        # <person>
        # <name value="Alice"/>
        # </person>
        # <person>
        # <name value="Bob"/>
        # </person>
        # </employees>"""
        # from requests_xml import XML
        # xml=XML(xml=doc)
        # print(xml.json())
        from jsonschema import validate
        url="https://testerhome.com/api/v3/topics.json"
        data=requests.get(url,params={'limit':'2'}).json()
        schema=json.load(open('topic_schema.json'))
        validate(data,schema=schema)

        

