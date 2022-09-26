import pytest
import pytest_ordering
class TestDemo:
    def testcase1(self):
        print("testcase1")
    @pytest.mark.run(order=1)
    def testcase2(self):
        print("testcase2")
    @pytest.mark.run(order=3)
    def testcase3(self):
        print("testcase3")
    def testcase4(self):
        print("testcase4")