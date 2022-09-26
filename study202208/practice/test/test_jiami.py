import requests
import xmltodict

from study202208.practice.test import jiami
class TestApiRequest():
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }
    def test_send(self):
        ar=jiami.ApiRequest()
        print(ar.send(self.req_data))

    def test_xml_to_dict(self):
        ar = jiami.ApiRequest()
        res=requests.get("https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss")
        final_res=ar.response_to_dict(res)
        assert isinstance(final_res,dict)
