from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as ec

import time

class Nate_End(BaseItem):

    Check_btn = (By.CSS_SELECTOR,"#content > div.join-btnBox.t2 > div > a")

    def __init__(self, driver):
        super(Nate_End, self).__init__(driver)

    def End_page_check(self):
        # 회원 가입 완료 페이지 확인
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2"))).text == "네이트 회원가입을"
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > br"))).text == "환영합니다!"

        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > div.comBox > p > strong:nth-child(1)"))).text == "가입한 이름"
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > div.comBox > p > strong:nth-child(2)"))).text == "가입한 아이디"

        self.Click(self.Check_btn)