from tpffpsldna.Pages.Base import BaseItem
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class Nate_Singup(BaseItem):
    # 메인 화면 > 회원가입 locator
    Nate_URL = "https://www.nate.com/"
    Main_SignUp = (By.CSS_SELECTOR,"#f_login > fieldset > span.option02 > a:nth-child(4)")
    Back_page = (By.CSS_SELECTOR,"#header > div > a")
    Main_page = (By.LINK_TEXT,"NATE")
   
    def __init__(self, driver):
        super(Nate_Singup, self).__init__(driver)

    def Main_Sign_Up_join(self):
        self.Get(self.Nate_URL)
        self.Click(self.Main_SignUp)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#checkPolicy > h2"))).text == "네이트 회원가입을 시작합니다!\n약관에 동의해 주세요."
        self.Click(self.Back_page)
        self.Click(self.Main_SignUp)
        self.Click(self.Main_page)