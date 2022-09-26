import json

import requests
from loguru import logger

from study202208.practice.interface.apis.base_api import BaseApi


class Cart(BaseApi):
    def add(self,data):
        url = "wx/cart/add"
        r = self.send("post",url, json=data)
        return r