from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as ec

import time

class Nate_Email(BaseItem):

    input_Email = (By.CSS_SELECTOR,"#email")
    warning_message = (By.CSS_SELECTOR,"#email_check_result")
    next_page = (By.CSS_SELECTOR, "#joinEmailInfo > fieldset > div.join-btnBox > div > a")

    def __init__(self, driver):
        super(Nate_Email, self).__init__(driver)

    def Email_page_check(self):
        # 이메일 생성 페이지 진입 확인
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2"))).text == "이메일주소를 입력해 주세요."
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > div"))).text == "아이디/비밀번호 찾기에 사용되니 기존에 사용하시는"
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > br"))).text == "네이트 또는 타 사이트 이메일 주소를 입력해 주세요."

        # 이메일 미입력으로 다음 페이지 이동 시 경고 메시지 노출
        self.Click(self.next_page)
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#email_check_result"))).text == "주로 사용하는 이메일을 입력해 주세요."
    
    def Email_input_test(self):
        # 정상 / 비정상 이메일 문자 입력 및 메시지 노출 확인
        # 정상
        self.Click(self.input_Email)
        self.Send_keys(self.input_Email,nate_Email["normal_Email_1"])
        self.Clear(self.input_Email)

        self.Click(self.input_Email)
        self.Send_keys(self.input_Email,nate_Email["normal_Email_2"])
        self.Clear(self.input_Email)

        # 비정상
        self.Click(self.input_Email)
        self.Send_keys(self.input_Email,nate_Email["address_wrong_Email_1"])
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#email_check_result"))).text == "이메일 주소를 올바르게 입력해 주세요."
        self.Clear(self.input_Email)

        self.Click(self.input_Email)
        self.Send_keys(self.input_Email,nate_Email["address_wrong_Email_2"])
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#email_check_result"))).text == "이메일 주소를 올바르게 입력해 주세요."
        self.Clear(self.input_Email)

        self.Click(self.input_Email)
        self.Send_keys(self.input_Email,nate_Email["malformed_Email"])
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"#email_check_result"))).text == "이메일 주소의 형식이 적합하지 않습니다. 영어, 숫자, '-', '_', '.'만 사용 가능 합니다."
        self.Clear(self.input_Email)

    def Next_page(self):
        # 이메일 입력 후 다음 페이지 이동
        self.Click(self.input_Email)
        self.Send_keys(self.input_Email,nate_Email["normal_Email_1"])

        self.Click(self.next_page)



