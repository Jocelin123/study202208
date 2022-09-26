import requests

def test_litmall():
    data={"username":"user123","password":"user123"}
    r=requests.post('https://litemall.hogwarts.ceshiren.com/wx/auth/login',json=data)
    print(r.json()['data']['token'])
    header_token={'X-Litemall-Token':r.json()['data']['token']}
    detail_r=requests.get('https://litemall.hogwarts.ceshiren.com/wx/goods/detail?id=1057036')
    print(detail_r.json())
    print(detail_r.json()['data']['productList'][0]['id'])
    data1={"goodsId":1057036,"number":1,"productId":71}
    gw=requests.post('https://litemall.hogwarts.ceshiren.com/wx/cart/add',headers=header_token,json=data1)
    a=gw.json()['errmsg']
    print(a)
    assert a=='成功'