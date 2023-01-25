from tpffpsldna.Config.Accounts import *
from tpffpsldna.Pages.Base import BaseItem

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class Login_Job(BaseItem):

    URL = "https://www.jobkorea.co.kr/"
    member = (By.CSS_SELECTOR,"#point > div > div.pointSide > div.loginWrap > ul > li:nth-child(1) > button")
    ID_path = (By.ID,"lb_id")
    PW_path = (By.ID,"lb_pw")
    login_btn = (By.CSS_SELECTOR,"#loginForm > fieldset > div.loginIptWrap.clear > button")
    assert_name = (By.CSS_SELECTOR,"#devLogin > div > div.myInfo > span.name > a")


    def __init__(self, driver):
        super(Login_Job,self).__init__(driver)

    def Login(self):
        self.Get(self.URL)
        self.Click(self.member)
        self.Send_keys(self.ID_path, ID["JobKorea_ID"])
        self.Send_keys(self.PW_path, PW["JobKorea_PW"])
        self.Click(self.login_btn)
        self.Find_Element(self.assert_name)
        