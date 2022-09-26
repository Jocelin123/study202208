# import yaml
# with open("./data/adddata.yaml","r",encoding='utf-8') as f:
#     print(yaml.safe_load(f))
import os

# print(os.path.dirname(__file__))
# data={
#     "client":{"default-character-set":"utf8"},
#     "mysql":{"user":'root',"password":123},
#     "custom":{
#         "user1": {"user": "张三", "pwd": 666},
#         "user2": {"user": "李四", "pwd": 999},
#     }
# }
#
# with open("./my.yaml",'w',encoding='utf-8') as f:
#     yaml.dump(data,f,allow_unicode=True)
# with open('./my.yaml','r',encoding='utf-8') as f:
#     data = yaml.safe_load(f)
# print(data)
# print(type(data))
# print(data['custom']['user1']['user'])
# import openpyxl
# book=openpyxl.load_workbook('data/0812test.xlsx')
# sheet = book.active
# print(sheet)
# cell_a1=sheet['A1']
# cell_c3=sheet.cell(column=3,row=3)
# print(cell_a1.value)
# print(cell_c3.value)
# list1=[]
# j=0
# print(sheet['A1':'C3'])
# for i in sheet['A1':'C3']:
#     list1[j]=i
#     j=j+1
# print(type(sheet['A1':'C3']))

#某气象观测程序在一个文件记录了每30分钟的天气情况，给定两种天气情况，找出两种天气(不限出现的前后顺序)变化相隔最小的时间间隔。 PS:若两种天气相邻出现，则最小时间间隔即为30分钟
# data=["sunny1","sunny2","sunny2","overcast1","overcast2","sunny1","light rain1","sunny3","sunny2","sunny2","overcast1","overcast2","light rain1","sunny3","light rain1","sunny3","sunny1","sunny2","sunny2","sunny1"]
# def func(a, b):
#     index = [i for i, j in enumerate(data) if j == a]
#     index2 = [i for i, j in enumerate(data) if j == b]
#     ret = [abs(j - i) for i in index for j in index2]
#     print(min(ret) * 30)
#
# func(a="overcast1", b="sunny1")
#
# with open("./data/weather.txt",'r') as f:
#     data=f.read().split(',')
#     # print(f1)
#     # data=[i for i in f1]
#     # print(data)
# def func(a,b):
#     x=[i for i,j in enumerate(data) if j==a]
#     y=[i for i,j in enumerate(data) if j==b]
#     z=[abs(i-j) for i in x for j in y]
#     return min(z)*30
# print(func(a="overcast1", b="sunny1"))
import pytest
import re
def scramble(s1: str, s2: str):
    # for i in s2:
    #     if i not in s1:
    #         return False
    #     if i in s1 and s1.count(i)<s2.count(i):
    #         return False
    # else:
    #     return True
    try:
        temp=list(s1)
        for i in s2:
            temp.remove(i)
        return True
    except ValueError:
        return False
print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
print(scramble('scriptingjav', 'javascript'))
# assert scramble('rkqodlw', 'world') ==  True
# assert scramble('cedewaraaossoqqyt', 'codewars') == True
# assert scramble('katas', 'steak') == False
# assert scramble('scriptjava', 'javascript') == True
# assert scramble('scriptingjava', 'javascript') == True
# assert scramble('scriptingjav', 'javascript') == False