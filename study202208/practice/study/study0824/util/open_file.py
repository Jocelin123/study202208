import csv

import yaml

from study202208.practice.study.study0824.config.setting import addfilepath


# class Openfile:
def open_file(x):
    if x.endswith(".yaml"):
        with open(x, encoding='utf-8') as f:
            data=yaml.safe_load(f.read())
        return data
    elif x.endswith(".csv"):
        with open(x, encoding='utf-8') as f:
            data=[]
            for i in csv.reader(f):
                data.append(i)
        return data
        # with open(x, encoding='utf-8') as f:
        #     yield from csv.reader(f)
        #     print(type(f.read()))
    else:
        return "无此文件格式的打开方式"


# print(open_file(addfilepath))
