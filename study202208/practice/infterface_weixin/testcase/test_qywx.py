import pytest
import requests
from loguru import logger

from study202208.practice.infterface_weixin.apis.dept_api import DeptApi


class TestQYWX:
    def setup_class(self):
        self.api=DeptApi("https://qyapi.weixin.qq.com/cgi-bin")

    @pytest.mark.parametrize("name, name_en, parent_id, order, depart_id", [
        ("深圳研发66", "szcen66", 1, 1, 242)
    ])
    def test_createdept(self, name, name_en, parent_id, order, depart_id):
        data={
            "name": name,
            "name_en": name_en,
            "parentid": parent_id,
            "order": order,
            "id": depart_id
        }

        r=self.api.create_dept(json=data)
        logger.info(f"获取创建部门的返回值{r}")
        # assert r['errcode']==0
        assert depart_id in self.test_get_departments()
        r=self.api.delete_dept(depart_id)
        assert r['errcode'] == 0

    def test_get_departments(self):
        r = self.api.query_dept()
        logger.info(f"获取查询部门列表返回{r}")
        assert r.get('errcode') == 0
        departids = [depart.get("id") for depart in r['department_id']]
        logger.info(f"获取创建部门id列表{departids}")
        return departids

