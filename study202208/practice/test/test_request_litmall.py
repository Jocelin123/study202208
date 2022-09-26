import json

import pytest
import requests
from faker import Faker
from loguru import logger


class TestRequstLitmall:
    def setup_class(self):
        data = {"username": "admin123", "password": "admin123", "code": ""}
        r = requests.post('https://litemall.hogwarts.ceshiren.com/admin/auth/login', json=data)
        self.token = r.json()['data']['token']
        fake = Faker("zh-CN")
        self.name = fake.name()
        self.ssn = fake.ssn()
        data1 = {"username": "user123", "password": "user123"}
        url = "https://litemall.hogwarts.ceshiren.com/wx/auth/login"
        r1 = requests.post(url, json=data1)
        self.token_one = r1.json()['data']['token']

    def teardown(self):
        url = "https://litemall.hogwarts.ceshiren.com/admin/goods/delete"
        data = {"id": self.goodsId}
        r=requests.post(url,json=data,headers={"X-Litemall-Admin-Token": self.token})
        logger.debug(f"删除端口的响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")


    def test_add_goods(self):
        data = {"goods": {"picUrl": "", "gallery": [], "isHot": 'false', "isNew": 'true', "isOnSale": 'true',
                          "goodsSn": self.ssn, "name": self.name},
                "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
                "products": [{"id": 0, "specifications": ["标准"], "price": "1.5", "number": "15", "url": ""}],
                "attributes": []}
        create_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/create"
        header = {"X-Litemall-Admin-Token": self.token}
        r = requests.post(url=create_url, headers=header, json=data)
        logger.debug(f"上架端口接口的相应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        assert r.json()['errmsg'] == '成功'
        goodid_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/list"
        params = {
            'name': self.name,
            'sort': 'add_time',
            'order': 'desc'
        }
        header = {"X-Litemall-Admin-Token": self.token}
        r = requests.get(url=goodid_url, headers=header, params=params)
        self.goodsId = r.json()['data']['list'][0]['id']
        logger.debug(f"获取端口列表的接口{json.dumps(r.json(), indent=2, ensure_ascii=False)}")

        productid_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/detail"
        data = {
            'id': self.goodsId
        }
        header = {"X-Litemall-Admin-Token": self.token}
        r1 = requests.get(url=productid_url, headers=header, params=data)
        # print(r1.json())
        self.productId = r1.json()['data']['products'][0]['id']

        header = {"X-Litemall-Token": self.token_one}
        url = "https://litemall.hogwarts.ceshiren.com/wx/cart/add"
        data = {"goodsId": self.goodsId, "number": 1, "productId": self.productId}
        r2 = requests.post(url, headers=header, json=data)
        logger.debug(f"添加购物车接口响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        assert r2.json()['errmsg'] == '成功'

    # @pytest.mark.dependency(name='查询')
    # def test_search(self):
    #     goodid_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/list"
    #     params = {
    #               'name': self.name,
    #               'sort': 'add_time',
    #               'order': 'desc'
    #             }
    #     header = {"X-Litemall-Admin-Token": self.token}
    #     r = requests.get(url=goodid_url, headers=header, params=params)
    #     self.goodsId=r.json()['data']['list'][0]['id']
    #
    #     productid_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/detail"
    #     data = {
    #         'id': self.goodsId
    #     }
    #     header = {"X-Litemall-Admin-Token": self.token}
    #     r1 = requests.get(url=productid_url, headers=header, params=data)
    #     print(r1.json())
    #     self.productId = r1.json()['data']['products'][0]['id']

    # @pytest.mark.dependency(name='客户端登录')
    # def test_login(self):
    #     data1={"username":"user123","password":"user123"}
    #     url="https://litemall.hogwarts.ceshiren.com/wx/auth/login"
    #     r1=requests.post(url,json=data1)
    #     self.token_one=r1.json()['data']['token']

    # @pytest.mark.dependency(depends=['查询'])
    # def test_add_cart(self):
        # goodid_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/list"
        # params = {
        #     'name': self.name,
        #     'sort': 'add_time',
        #     'order': 'desc'
        # }
        # header = {"X-Litemall-Admin-Token": self.token}
        # r = requests.get(url=goodid_url, headers=header, params=params)
        # self.goodsId = r.json()['data']['list'][0]['id']
        # logger.debug(f"获取端口列表的接口{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        #
        # productid_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/detail"
        # data = {
        #     'id': self.goodsId
        # }
        # header = {"X-Litemall-Admin-Token": self.token}
        # r1 = requests.get(url=productid_url, headers=header, params=data)
        # # print(r1.json())
        # self.productId = r1.json()['data']['products'][0]['id']
        #
        # header = {"X-Litemall-Token": self.token_one}
        # url = "https://litemall.hogwarts.ceshiren.com/wx/cart/add"
        # data = {"goodsId": self.goodsId, "number": 1, "productId": self.productId}
        # r2 = requests.post(url, headers=header, json=data)
        # logger.debug(f"添加购物车接口响应信息为{json.dumps(r.json(), indent=2, ensure_ascii=False)}")
        # assert r2.json()['errmsg'] == '成功'
