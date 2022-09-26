from study202208.practice.interface.apis.admin.goods import Goods
from study202208.practice.interface.apis.wx.cart import Cart
from faker import Faker


class TestCart:
    def setup_class(self):
        self.good=Goods("https://litemall.hogwarts.ceshiren.com/","admin")
        self.cart=Cart("https://litemall.hogwarts.ceshiren.com/","client")
        fake = Faker("zh-CN")
        self.name = fake.name()
        self.ssn = fake.ssn()
        self.goodsId=0

    # def teardown(self):
        # data = {"id": self.goodsId}
        # self.good.delete({"id": self.goodsId})


    def test_add_cart(self):
        """
        添加购物车的测试：
        上架商品接口
        获取商品列表
        获取商品详情
        添加购物车
        """
        goods_data = {"goods": {"picUrl": "", "gallery": [], "isHot": 'false', "isNew": 'true', "isOnSale": 'true',
                          "goodsSn": self.ssn, "name": self.name},
                "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
                "products": [{"id": 0, "specifications": ["标准"], "price": "1.5", "number": "15", "url": ""}],
                "attributes": []}
        goods_params = {
            'name': self.name,
            'sort': 'add_time',
            'order': 'desc'
        }
        self.good.create(goods_data)
        good_list_r=self.good.list(goods_params)
        self.goodsId = good_list_r['data']['list'][0]['id']
        goods_id = {
            'id': self.goodsId
        }
        good_detail_r=self.good.detail(goods_id)
        productId = good_detail_r['data']['products'][0]['id']

        cart_data = {"goodsId": self.goodsId, "number": 1, "productId": productId}
        # r=self.good.delete({"id": self.goodsId})
        r=self.good.deletebyname(goods_params)
        assert r['errmsg'] == '成功'
