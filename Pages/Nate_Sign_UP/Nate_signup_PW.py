from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

class Nate_PW(BaseItem):
    
    warning_message = (By.CSS_SELECTOR,"#id_duplicate_check_result")
    input_PW = (By.CSS_SELECTOR,"#pw")
    input_PW_Check = (By.CSS_SELECTOR,"#pwc")
    Masking = (By.CSS_SELECTOR,"#btn_mask_pw_1 > span")
    next_page = (By.CSS_SELECTOR,"#joinPasswordInfo > fieldset > div.join-btnBox > div")

    def __init__(self, driver):
        super(Nate_PW, self).__init__(driver)

    def PW_page_check(self):
        # 회원가입 비밀번호 생성 페이지 진입 확인
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2"))).text == "비밀번호를 설정해 주세요."
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > div"))).text == "개인정보 및 사생활 보호를 위해 본인만 알 수 있는"
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > br"))).text == "안전한 비밀번호를 사용해 주세요."
        
        # 비밀번호 입력란 영역 메시지 노출 확인
        self.inter.driver.find_element(By.CSS_SELECTOR,"#pw").get_attribute("placeholder") == "영문소문자, 숫자조합 6~40자 (-,_가능)"
        self.inter.driver.find_element(By.CSS_SELECTOR,"#pwc").get_attribute("placeholder") == "비밀번호 재입력"

        # 아이디와 중복 혹은 3자 이상 연속 등 안내 사항 문구 확인
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#joinPasswordInfo > fieldset > div.ifBox.pw > div.infomsg"))).text == "아이디와 3자 이상 중복되거나, 3자 이상 연속 또는 중복되는 문자, 숫자는 사용할 수 없습니다."
        


    def PW_input_check(self):
        # 비밀번호 마스킹 기능 확인
        self.Send_keys(self.input_PW,"Q1w2e3r")
        self.Click(self.Masking)
        text = self.inter.driver.find_element(By.CSS_SELECTOR,"#pw").get_attribute("type")
        assert text == "text"
        self.Click(self.Masking)
        text = self.inter.driver.find_element(By.CSS_SELECTOR,"#pw").get_attribute("type")
        assert text == "password"

        self.Send_keys(self.input_PW_Check,"Q1w2e3r")
        self.Click(self.Masking)
        text = self.inter.driver.find_element(By.CSS_SELECTOR,"#pwc").get_attribute("type")
        assert text == "text"
        self.Click(self.Masking)
        text = self.inter.driver.find_element(By.CSS_SELECTOR,"#pwc").get_attribute("type")
        assert text == "password"

    def PW_input_test(self):

        # 강함 / 중간 / 약한 강도의 비밀번호 입력
        self.Send_keys(self.input_PW,nate_PW["strong"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#pw_safety_check_msg_result"))).text == "예측이 어려운 강력한 비밀번호 입니다."
        self.Clear(self.input_PW)
        
        self.Send_keys(self.input_PW,nate_PW["middle"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#pw_safety_check_msg_result"))).text == "사용가능한 안전한 비밀번호 입니다."
        self.Clear(self.input_PW)

        self.Send_keys(self.input_PW,nate_PW["weak"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#pw_safety_check_msg_result"))).text == "좀 더 안전한 비밀번호로 설정해 주세요."
        self.Clear(self.input_PW)

        # 영문과 숫자 모두 포함 / 아이디를 비밀번호로 사용 / 3자 연속 사용 비밀번호 입력

        self.Send_keys(self.input_PW,nate_PW["not_included_ID"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#pw_safety_check_msg_result"))).text == "비밀번호는 영문과 숫자 모두 포함되어야 합니다."
        self.Clear(self.input_PW)
        
        self.Send_keys(self.input_PW,nate_PW["abnormal_ID"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#pw_safety_check_msg_result"))).text == "비밀번호는 영문과 숫자 모두 포함되어야 합니다."
        self.Clear(self.input_PW)

        self.Send_keys(self.input_PW,nate_PW["sameID"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#pw_safety_check_msg_result"))).text == "아이디를 비밀번호로 사용하는 것은 사용불가합니다."
        self.Clear(self.input_PW)

        self.Send_keys(self.input_PW,nate_PW["continuity"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#pw_safety_check_msg_result"))).text == "3자 이상 연속된 문자는 사용 불가 합니다."
        self.Clear(self.input_PW)

        # 영문 / 숫자 / 특수문자 조합 입력
        # 7자 조합
        self.Send_keys(self.input_PW,nate_PW["Combination_7"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "비밀번호는 8자리 이상으로 입력해 주세요."
        self.Clear(self.input_PW)
        # 8자 조합
        self.Send_keys(self.input_PW,nate_PW["Combination_8"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "예측이 어려운 강력한 비밀번호 입니다."
        self.Clear(self.input_PW)
        # 16자 조합
        self.Send_keys(self.input_PW,nate_PW["Combination_16"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "예측이 어려운 강력한 비밀번호 입니다."
        self.Clear(self.input_PW)
        # 20자 조합
        self.Send_keys(self.input_PW,nate_PW["Combination_20"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "예측이 어려운 강력한 비밀번호 입니다."
        self.Clear(self.input_PW)
        # 21자 조합
        self.Send_keys(self.input_PW,nate_PW["Combination_21"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "비밀번호는 20자리 이하로 입력해 주세요."
        self.Clear(self.input_PW)

    def input_PW_Check_test(self):

        self.Send_keys(self.input_PW,nate_PW["strong"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#pw_safety_check_msg_result"))).text == "예측이 어려운 강력한 비밀번호 입니다."
        
        # 비밀번호 확인 미입력 메시지 문구 확인
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#pw_pwc_check_msg_result"))).text == "비밀번호 미입력"
        
        # 비밀번호 일치 확인
        self.Send_keys(self.input_PW_Check,nate_PW["strong"])
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#pw_pwc_check_msg_result"))).text == "비밀번호 일치"
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active on"

    def Next_page(self):

        self.Click(self.next_page)


