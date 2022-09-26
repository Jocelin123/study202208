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
from path_demo import hello
# hello()
# print(sys.path)
d={'a':1,"b":2,'c':4}
print(len(d))