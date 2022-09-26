import pytest
import pytest_ordering
class TestDemo:
    def testcase111(self):
        print("testcase111")
    @pytest.mark.run(order=8)
    def testcase222(self):
        print("testcase222")
    @pytest.mark.run(order=6)
    def testcase333(self):
        print("testcase333")
    @pytest.mark.run(order=5)
    def testcase444(self):
        print("testcase444")