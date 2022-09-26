import os

import requests
import yaml
from loguru import logger

root_path=os.path.dirname(os.path.abspath(__file__))
class Base:
    def __init__(self,baseurl):
        conf_path = os.sep.join([root_path, '..', '/config/conf.yaml'])
        with open(conf_path,encoding='u8') as f:
            data=yaml.safe_load(f)
        self.baseurl = data['test_env']
        """获取access token"""
        # id='wwf6f7e8b7dbd227cc'
        # secret='6t7XTlKf913kYFDIs47zlvPR72mgVsPzwX1zHCAY1kY'
        params1 = {
            "corpid": data['id'],
            "corpsecret": data['secret']
        }
        r=self.get_token(params1)
        self.access_token=r['access_token']
        logger.info(f"获取token{self.access_token}")
        self.params={
            'access_token': self.access_token
        }

    def req(self,method,url,tools='requests',**kwargs):
        logger.info(f"method--url--tools--**kwargs==>{method}--{url}--{tools}--{kwargs}")
        if tools=='requests':
            r=requests.request(method,self.baseurl+url,**kwargs)
            return r.json()
        else:
            pass

    def get_token(self,params=None):
        url = "/gettoken"
        r=self.req(method="GET",url=url,params=params)
        return r