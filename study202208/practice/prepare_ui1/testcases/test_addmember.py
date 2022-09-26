from faker import Faker

from study202208.practice.prepare_ui1.page.login_page import LoginPage


class TestAddMember():
    def setup_class(self):
        self.home=LoginPage().login()

    def setup(self):
        fake = Faker("zh-CN")
        self.membername = fake.name()
        self.ssn = fake.ssn()
        self.phone_number = fake.phone_number()
        self.deptname=fake.name()

#浏览器退出存在问题
    def teardown_class(self):
        LoginPage().close_browser()

    def test_addmember(self):
        result=self.home.click_add_member().fillinfo_member(self.membername,self.ssn,self.phone_number).get_tips_member()
        assert result=="保存成功"

    def test_add_dept(self):
        result=self.home.click_contactpage().click_adddept().fillinto_dept(self.deptname).get_tips_dept()
        assert result == "新建部门成功"