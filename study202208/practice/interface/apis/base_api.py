import json

import requests
from loguru import logger


class BaseApi:
    def __init__(self,base_url,role=None):
        # self.base_url="https://litemall.hogwarts.ceshiren.com/"
        self.base_url=base_url
        if role:
            self.role=role

        data = {"username": "admin123", "password": "admin123", "code": ""}
        url1 = 'admin/auth/login'
        r = requests.request("post", self.base_url + url1, json=data)
        self.token = r.json()['data']['token']
        self.adminheader = {"X-Litemall-Admin-Token": self.token}

        data1 = {"username": "user123", "password": "user123"}
        url = "wx/auth/login"
        r1 = requests.request("post", self.base_url + url, json=data1)
        self.token_one = r1.json()['data']['token']
        self.wxheader = {"X-Litemall-Token": self.token_one}

    def __set_token(self,request_info):
        if self.role=="admin":
            self.final_token=self.adminheader
        else:
            self.final_token=self.wxheader

        if request_info.get("headers"):
            #此方式在原header值不变的情况下加入X-Litemall-Admin-Token的值
            request_info["headers"].update(self.final_token)
        else:
            # 此方式如原header有值，会被X-Litemall-Admin-Token覆盖，只剩下这一个头信息
            request_info["headers"] = self.final_token
        return request_info


    # def __set_token(self,request_info):
    #     if self.role=="admin":
    #         data = {"username": "admin123", "password": "admin123", "code": ""}
    #         url1 = 'admin/auth/login'
    #         r = requests.request("post", self.base_url + url1, json=data)
    #         self.token = r.json()['data']['token']
    #         self.adminheader = {"X-Litemall-Admin-Token": self.token}
    #         self.final_token=self.adminheader
    #     else:
    #         data1 = {"username": "user123", "password": "user123"}
    #         url = "wx/auth/login"
    #         r1 = requests.request("post", self.base_url + url, json=data1)
    #         self.token_one = r1.json()['data']['token']
    #         self.wxheader = {"X-Litemall-Token": self.token_one}
    #         self.final_token=self.wxheader
    #
    #     if request_info.get("headers"):
    #         #此方式在原header值不变的情况下加入X-Litemall-Admin-Token的值
    #         request_info["headers"].update(self.final_token)
    #     else:
    #         # 此方式如原header有值，会被X-Litemall-Admin-Token覆盖，只剩下这一个头信息
    #         request_info["headers"] = self.final_token
    #     return request_info


    def send(self,method,url,**kwargs):
        kwargs=self.__set_token(kwargs)
        r=requests.request(method,self.base_url+url,**kwargs)
        logger.debug(f"{url}接口的相应值为{json.dumps(r.json(),indent=2,ensure_ascii=False)}")
        return r.json()