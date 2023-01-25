from tpffpsldna.Pages.Base import BaseItem
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as ec

import time

class Nate_Privacy(BaseItem):

    ON_btn = (By.CSS_SELECTOR,"#ipon")
    OFF_btn = (By.CSS_SELECTOR,"#ipoff")
    next_page = (By.CSS_SELECTOR,"#joinPasswordInfo > fieldset > div.join-btnBox > div")

    def __init__(self, driver):
        super(Nate_Privacy, self).__init__(driver)

    def Privacy_page_check(self):
        # 개인정보 페이지 진입 확인
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located(By.CSS_SELECTOR,"#content > h2")).text == "개인정보를 보호하실 수 있습니다."
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located(By.CSS_SELECTOR,"#content > div")).text == "해외 IP 차단을 설정하시면 해외에서 로그인 시"
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located(By.CSS_SELECTOR,"#content > div > br")).text == "본인확인 절차가 진행됩니다."
        
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located(By.CSS_SELECTOR,"#ipBlock > div:nth-child(2)")).text == "가입 이후에는 '내정보>개인정보보호관리>해외IP차단'에서 설정을 변경하실 수 있습니다."
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located(By.CSS_SELECTOR,"#ipBlock > div:nth-child(3)")).text == "개인정보보호관리 메뉴에서는 로그인 기록 확인, 로그인IP 설정, 아이디 지키기 등의 개인정보보호 기능도 이용하실 수 있습니다."
        
    def Privacy_Radio_btn(self):
        self.Click(self.ON_btn)
        self.Click(self.OFF_btn)
        self.Click(self.ON_btn)

    def Next_page(self):
        self.Click(self.next_page)
















