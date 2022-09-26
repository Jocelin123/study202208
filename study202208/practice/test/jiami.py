import json
import requests
import base64

import xmltodict


class ApiRequest:
    def send(self,data:dict):
        res=requests.request(data["method"],data["url"],headers=data["headers"])
        if data["encoding"]=="base64":
            # python自带的base64的解密方法
            return json.loads(base64.b64decode(res.content))
        else:
            #把加密过后的响应值发送给第三方服务，让第三方去做解密然后返回
            return requests.post("第三方服务url",data=res.content)

    def response_to_dict(self,response):
        res=response.text
        if res.startswith("<?xml"):
            return xmltodict.parse(res)
        elif res.startswith("<!DOCTYPE html>"):
            return "html"
        else:
            return response.json()