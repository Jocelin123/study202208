from loguru import logger

from study202208.practice.infterface_weixin.base.base import Base


class GetToken(Base):
    def __init__(self,baseurl):
        self.baseurl = baseurl
        """获取access token"""
        id='wwf6f7e8b7dbd227cc'
        secret='6t7XTlKf913kYFDIs47zlvPR72mgVsPzwX1zHCAY1kY'
        params1 = {
            "corpid": id,
            "corpsecret": secret
        }
        r=self.get_token(params1)
        self.access_token=r['access_token']
        logger.info(f"获取token{self.access_token}")
        self.params={
            'access_token': self.access_token
        }