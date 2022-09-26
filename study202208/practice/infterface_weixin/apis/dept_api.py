from study202208.practice.infterface_weixin.base.base import Base


class DeptApi(Base):
    def create_dept(self,json=None):
        url = "/department/create"
        r=self.req(method="POST",url=url,params=self.params,json=json)
        return r

    def update_dept(self,**kwargs):
        url="/department/update"
        r=self.req(method="POST",url=url,params=self.params,**kwargs)
        return r

    def delete_dept(self,id):
        url = "/department/delete"
        param={
            'id':id
        }
        r=self.req(method="GET",url=url,params=dict(self.params,**param))
        return r

    def query_dept(self):
        url = "/department/simplelist"

        r = self.req(method="GET", url=url, params=self.params)
        return r