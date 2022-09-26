import csv
import logging
import os
import sys

import pytest

from study202208.practice.study.study0823.base.base import Base

mydir=os.path.dirname(os.path.dirname(__file__))
sys.path.append(mydir)
# print(mydir+'\data\divdata.csv')

# with open('../data/divdata.csv') as f:
#     list1 = []
#     for i in csv.reader(f):
#         list1.append(i)
#     print(list1)
class Testdiv(Base):
    @pytest.mark.parametrize('a,b,expect',csv.reader(open(mydir+'\data\divdata.csv')))
    def test_case_div(self,a,b,expect):
        logging.info("除法计算开始啦")
        result=self.cal.div(float(a),float(b))
        assert result==float(expect)
        open(mydir+'\data\divdata.csv').close()