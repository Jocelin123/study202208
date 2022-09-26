class GoodsDomain:
    def create(self):
        pass

    def delete(self):
        pass

    def list(self):
        pass

    def deletebyname(self,name):
        good_list_r=self.list(name)
        goods_id=good_list_r['data']['list'][0]['id']
        goodsId = {
            'id': goods_id
        }
        r=self.delete(goodsId)
        return r
