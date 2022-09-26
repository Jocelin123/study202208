# hello="hello baidu"
# def search():
#     print("这是一个搜索方法")
import os
import sys

my_dir=os.path.dirname(os.path.abspath(__file__))+"\data"
sys.path.append(my_dir)
print(my_dir+"/test/data.yaml")