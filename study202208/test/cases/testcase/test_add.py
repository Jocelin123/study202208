# test_add.py 文件内容
import pytest
# import openpyxl
# from func.operation import my_add
import json
# def get_excel():
#     book=openpyxl.load_workbook('../data/0812test.xlsx')
#     sheet=book.active
#     cells=sheet['A1':'C3']
#     values=[]
#     for row in cells:
#         cell=[]
#         for col in row:
#             cell.append(col.value)
#         values.append(cell)
#     return values
# class TestWithEXCEL:
#     @pytest.mark.parametrize('x,y,expected', get_excel())
#     def test_add(self, x, y, expected):
#         assert my_add(int(x), int(y)) == int(expected)
# def get_json():
#     with open('../data/params.json','r') as f:
#         a=json.load(f)
#     return list(a.values())
#     # return a
# class TestWithjson:
#     @pytest.mark.parametrize('x,y,expected', get_json())
#     def test_add(self, x, y, expected):
#         assert my_add(int(x), int(y)) == int(expected)
import csv
# def test_get_csv():
#     with open('../data/params.json','r') as f:
#         a=csv.reader(f)
#         print(a)
#         print(type(a))
import pytest
import csv
# class TestWithcsv:
#     @pytest.mark.parametrize('x,y,expected', csv.reader(open('../../../data/params.csv')))
#     def test_add(self,x,y,expected):
#         print(x,y,expected)
#         print(open('../../../data/params.csv').close())