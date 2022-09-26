#日志模块的学习
# logging.basicConfig(format='%(asctime)s[%(levelname)s]%(message)s(%(filename)s:%(lineno)s)',datefmt='%m%d%Y %I:%M:%S %p',filename='example.log',level=logging.DEBUG)
# logging.basicConfig(format='%(asctime)s%(message)s%')
# logging.warning(" watch out")
# logging.info(" I told you so")
import json
import logging
#
# # create logger
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
#
# # create console handler and set level to debug
# # 定义一个流处理器
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # add formatter to ch
# ch.setFormatter(formatter)
#
# # add ch to logger
# logger.addHandler(ch)
# # 定义一个文件处理器
# ch_file = logging.FileHandler("example.log")
# ch_file.setLevel(logging.DEBUG)
#
# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# # add formatter to ch
# ch_file.setFormatter(formatter)
#
# # add ch to logger
# logger.addHandler(ch_file)
#
# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')
import os
# def get_logger():
#     # create logger
#     print(os.path.basename(__file__))
#     logger = logging.getLogger(os.path.basename(__file__))
#     logger.setLevel(logging.DEBUG)
#     # create console handler and set level to debug
#     ch = logging.FileHandler(filename='mylog.log', encoding="utf-8")
#     ch.setLevel(logging.DEBUG)
#     # create formatter
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     # add formatter to ch
#     ch.setFormatter(formatter)
#     # add ch to logger
#     logger.addHandler(ch)
#     return logger
# logger1=get_logger()
# def log_info(message):
#     logger1.info(message)
# log_info("info方法")
# import logging.config
# conf=logging.config.fileConfig('logging.conf')
# logger=logging.getLogger(conf)
# logger.info("lala")
from datetime import datetime

import urllib3
# def http1():
#     pm=urllib3.PoolManager()
#     res=pm.request(method="GET",url="http://httpbin.org/get")
#     print(res.status)
#     print(res.headers)
#     print(res.data)
# http1()
# def test_timeout():
#     pm = urllib3.PoolManager()
#     # 访问这个地址，服务器会在3秒后响应
#     url = "http://httpbin.org/delay/3"
#
#     # 设置超时时长
#     resp = pm.request(method='GET', url=url, timeout=4.0)
#     print(resp.status)
# test_timeout()
# def test_HTTPS():
#     # 创建不校验证书的连接池对象
#     pm_https = urllib3.PoolManager(cert_reqs="CERT_NONE")
#     url = "https://httpbin.ceshiren.com/get"
#
#     # 发送HTTPS请求
#     resp = pm_https.request(method='GET', url=url)
#     print(json.dumps(resp.data.decode('utf-8')))

# def students_grade(grade):
#     def output_students(name,gender):
#         print(f"{name},{gender},{grade}")
#     return output_students
# info1=students_grade(1)
# info1("ala","女生")
# info2=students_grade(2)
# info2("ala","女生")
# def logs(func):
#     def inner(*b):
#         print("函数开始执行")
#         return func(*b)
#         print("函数结束执行")
#     return inner
# @logs
# def add1():
#     print("执行1")
#     return 0
# @logs
# def add(x,y):
#     print("执行")
#     return x+y
# @logs
# def add2(x,y,z):
#     print("执行")
#     return x+y+z
#
# print(add1())
# print(add(1, 2))
# print(add2(1,2,3))
    # return x+y
#
# print(add(1, 2))

# print(logs(add1))
# import time
# def timer(func):
#     def inner():
#         print("开始执行")
#         star=datetime.now()
#         print(star)
#         func()
#         end=datetime.now()
#         print(end)
#         print("结束执行")
#         return end-star
#     return inner
# @timer
# def add1():
#     print("执行函数1")
#     time.sleep(2)
#
# @timer
# def add2():
#     print("执行函数2")
#     time.sleep(1)
# print(add1())
# print(add2())

# l1 = [2,4,3]
# l2 = [5,6,4]
# def func(s1,target):
#     l=len(s1)
#     dict={}
#     for i,j in enumerate(s1):
#         if (target-j) in dict:
#             return i,dict[target-j]
#         dict[j]=i
# print(func(s1, target))

# s = "abcagfdsgdgdfbcbb"
# def func(s):
#     l=len(s)
#     left,right=0,1
#     maxlen=1
#     dict={s[0]:0}
#     if l<2: return l
#     while right<l:
#         if s[right] in dict and left<=dict[s[right]] :
#             left=dict[s[right]]+1
#         dict[s[right]]=right
#         right+=1
#         maxlen=max(maxlen,right-left)
#     return maxlen
#
# print(func(s))
def scramble(s1: str, s2: str)  -> bool:
    try:
        s=list(s1)
        print(s)
        for i in s2:
            s.remove(i)
            print(s)
        return True
    except ValueError:
        return False
print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
print(scramble('scriptingjav', 'javascript'))