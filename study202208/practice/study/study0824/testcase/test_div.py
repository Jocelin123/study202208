import pytest

from study202208.practice.study.study0824.base.base import Base
from study202208.practice.study.study0824.config.setting import divfilepath
from study202208.practice.study.study0824.util.open_file import open_file


class Testdiv(Base):
    # print(Openfile.open_file(divfilepath))
    # @pytest.mark.flaky(rerun=3,reruns_delay =2)
    @pytest.mark.parametrize("x,y,expect",open_file(divfilepath))
    def testcasediv(self,x,y,expect):
        result=self.cal.div(float(x),float(y))
        assert result==float(expect)