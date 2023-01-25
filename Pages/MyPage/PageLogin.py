from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *

from selenium.webdriver.common.by import By


class Login(BaseItem):
    URL = "https://www.musinsa.com/auth/login?referer=https%3A%2F%2Fwww.musinsa.com%2Fapp%2F"
    input_email_id = (By.CSS_SELECTOR,"body > div.container.login > section > div.login-member > form > div.login-member__form > div:nth-child(10) > div > input")
    input_pw =(By.CSS_SELECTOR,"body > div.container.login > section > div.login-member > form > div.login-member__form > div:nth-child(11) > div > input")
    click_Login_Btn = (By.CSS_SELECTOR,"body > div.container.login > section > div.login-member > form > div.login-button.login-button--static > button")
  
    def __init__(self,driver):
        super(Login,self).__init__(driver)

    def get(self):
        self.Get(self.URL)

    def Login_send_keys_ID(self):
        self.Send_keys(self.input_email_id,ID["ID"])
    
    def Login_send_keys_PW(self):
        self.Send_keys(self.input_pw,PW["PW"])
    
    def Login_btn(self):
        self.Click(self.click_Login_Btn)
