from time import sleep

import pytest
import pytest_ordering
class TestDemo:
    @pytest.mark.first
    def testcase11(self):
        sleep(1)
        print("testcase11")
    @pytest.mark.four
    def testcase22(self):
        sleep(1)
        print("testcase22")
    @pytest.mark.run(order=7)
    def testcase33(self):
        sleep(1)
        print("testcase33")
    @pytest.mark.run(order=2)
    def testcase44(self):
        sleep(1)
        print("testcase44")

        import json
        import pytest
        from filelock import FileLock
        @pytest.fixture(scope="session")
        def session_data(tmp_path_factory, worker_id):
            fn = "data.json"#存放session
            with FileLock(str(fn) + ".lock"):
                if fn.is_file():
                    data = json.loads(fn.read_text())
                else:
                    data = get_session()#获取session
                    fn.write_text(json.dumps(data))
            return data
