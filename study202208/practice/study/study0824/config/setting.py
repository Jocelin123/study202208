import os
import sys

base_dir=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)

#加法文件路径
addfilepath=os.path.join(base_dir,'data','adddata.yaml')
# print(addfilepath)
#除法文件路径
divfilepath=os.path.join(base_dir,'data','divdata.csv')

#
# path=os.path.dirname(__file__)
# addfilepath=os.path.join(path,'..','data/adddata.yaml')
# print(addfilepath)