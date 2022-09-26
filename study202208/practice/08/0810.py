import os
import sys
# import time
# import yaml
# import requests
# import os

# from baidu import *
#
# print(sys.path)
# time.sleep(1)
#
# search()
# print(hello)
#
# print(dir(sys))
# def div(a,b):
#     return a/b
#
# try:
#     print(div(1, 2))
#     list=[1,2,3]
#     list[3]
# except Exception as e:
#     print("这里有异常：",{e})



# class MyError(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
#
# def set_age(num):
#     if num <= 0 or num > 200:
#         raise MyError(f"值错误：{num}")
#     else:
#         print(f"设置年龄为：{num}")

# set_age(10)
# help(os)
# print(dir(os))
# os.system('cmd')
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# print(os.listdir())
# os.rmdir('demo.py')
# print(os.path.abspath("./0810.py"))
# print(os.path.basename(os.path.abspath("./0810.py")))
# print(os.path.dirname(os.path.abspath("./0810.py")))
# a=os.path.split(os.path.abspath("./0810.py"))
# print(os.path.join(a[0],a[1]))
# print(os.path.getsize("./0810.py"))
# import selenium
# my_dir=os.path.dirname(os.path.abspath(__file__))+"/study"
# sys.path.append(my_dir)
# from path_demo import hello
# hello()
# print(sys.path)
import time

# f=open('data.txt','r',encoding='utf-8')
# print(f.read())
# print(type(f.read()))
# f.seek(0)
# print(f.readline())
# print(type(f.readline()))
# f.seek(0)
# print(f.readlines())
# print(type(f.readlines()))
# f.close()
# with open('data.txt','a+',encoding='utf-8') as f:
#     f.write("qqq")
#     f.seek(0)
#     print(f.read())
# import math
# print(math.pi)
# print(math.inf)
# print(-math.inf)
# print(math.nan)
# print(math.pow((1.0 + 0.01), 365))
# print(math.pow((1.0 - 0.01), 365))
from datetime import datetime

# s="2021-09-27 06:47:06"
# print(type(datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S')))
# a=datetime.datetime.now()
# print(type(datetime.datetime.strftime(a,'%Y-%m-%d %H:%M:%S')))
# a=12345
# print(datetime.datetime.fromtimestamp(a))
now=datetime.now()
result=now.strftime('%Y%m%d_%H%M%S')
log_name=result+'.log'
with open(log_name,'w+',encoding='utf-8') as f:
    message=f"{now}[info]line:14 this is a log message"
    f.write(message)
