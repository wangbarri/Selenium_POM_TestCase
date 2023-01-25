from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as ec

import time

class Nate_Login(BaseItem):

    keep_login = (By.CSS_SELECTOR,"#keeplogin")
    input_ID = (By.CSS_SELECTOR,"#ID")
    input_PW = (By.CSS_SELECTOR,"#PW")
    login_btn = (By.CSS_SELECTOR,"#btnLOGIN")
    my_name = (By.CSS_SELECTOR,"#btnNameNate > a > strong")

    def __init__(self, driver):
        super(Nate_Login,self).__init__(driver)


    def Login_page_check(self):
        # 로그인 유지 확인 및 클릭
        self.Click(self.keep_login)
        #해제
        self.Click(self.keep_login)
        
        # 아이디 입력란 메시지 확인 및 입력, alert 확인
        self.inter.driver.find_element(*self.input_ID).get_attribute("placeholder") == "아이디 or @이하 모두 입력"
        self.Send_keys(self.input_ID,"아이디 입력")
        self.Click(self.login_btn)
        wd(driver=self.inter.driver,timeout=10).until(ec.alert_is_present())
        result = self.inter.driver.switch_to.alert
        assert result.text == "비밀번호를 입력하세요"
        result.dismiss()
        self.Clear(self.input_ID)

        # 비밀번호 입력란 메시지 확인 및 입력, alert 확인
        self.inter.driver.find_element(*self.input_PW).get_attribute("placeholder") == "비밀번호"
        self.Send_keys(self.input_PW,"비밀번호 입력")
        self.Click(self.login_btn)
        wd(driver=self.inter.driver,timeout=10).until(ec.alert_is_present())
        result = self.inter.driver.switch_to.alert
        assert result.text == "아이디를 입력하세요"
        result.dismiss()
        self.Clear(self.input_ID)

        # 로그인 확인
        self.Send_keys(self.input_ID,"아이디 입력")
        self.Send_keys(self.input_PW,"비밀번호 입력")
        self.Click(self.login_btn)
        self.inter.driver.find_element(*self.my_name).text == "사용자 이름"
        
        