import requests

from study202208.practice.interface.apis.base_api import BaseApi
from study202208.practice.interface.domain.goods_domain import GoodsDomain


class Goods(BaseApi,GoodsDomain):
    def create(self,goods_data):
        create_url = "admin/goods/create"
        r = self.send("post",url=create_url, json=goods_data,headers={"teacher":"AD"})
        return r

    def list(self,params):
        goodid_url = "admin/goods/list"
        r = self.send('get',url=goodid_url,  params=params)
        return r

    def detail(self,goods_id):
        productid_url = "admin/goods/detail"
        r = self.send('get',url=productid_url,  params=goods_id)
        return r

    def delete(self,goods_id):
        gooddelet_url = "admin/goods/delete"
        r = self.send("post", gooddelet_url, json=goods_id)
        return r