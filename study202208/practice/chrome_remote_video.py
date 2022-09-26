from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option=Options()
option.debugger_address="localhost:9222"
driver=webdriver.Chrome(options=option)
driver.get("https://work.weixin.qq.com/wework_admin/frame")


# from selenium.webdriver import Remote
#
# def browser():
#     """
#     启动浏览器驱动
#     :return: 返回浏览器驱动URL
#     """
#     try:
#         host = 'localhost:9222'
#         driver = Remote(command_executor='http://' + host + '/wd/hub',
#                         desired_capabilities={ 'platform': 'ANY',
#                                                'browserName': 'chrome',
#                                                'version': "",
#                                                'javascriptEnabled': True
#                                             }
#                         )
#         return driver
#     except Exception as msg:
#         print("驱动异常-> {0}".format(msg))