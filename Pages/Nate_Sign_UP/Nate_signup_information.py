from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as ec

import time

class Nate_Information(BaseItem):

    input_name = (By.CSS_SELECTOR,"#name")
    warning_message = (By.CSS_SELECTOR,"#email_check_result")
    
    year = (By.CSS_SELECTOR,"#yy")
    month = (By.CSS_SELECTOR,"#mm")
    day = (By.CSS_SELECTOR,"#dd")

    man = (By.CSS_SELECTOR,"#gender_m")
    girl = (By.CSS_SELECTOR,"#id_gender_f")
    back_page = (By.CSS_SELECTOR,"#header > div > a")
    next_page = (By.CSS_SELECTOR, "#joinOtherInfo > fieldset > div.join-btnBox > div > a")

    def __init__(self, driver):
        super(Nate_Information, self).__init__(driver)

    def Information_page_check(self):
        # 기타 정보 입력 페이지 진입 확인
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2"))).text == "기타 정보를 입력해 주세요."

        # 생년월일 사용여부 안내 문구 확인
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#birthday > div.infomsg"))).text == "연령확인 (만 14세 미만 여부) 등에 사용됩니다."

    def Information_Name(self):

        # 이름 입력란 영역 메시지 확인
        self.inter.driver.find_element(By.CSS_SELECTOR,"#name").get_attribute("placeholder") == "20자 이내로 입력 가능합니다."

        # 정상 이름 입력 확인
        self.Send_keys(self.input_name,nate_Name["normal_Email_1"])
        self.Clear(self.input_name)
        
        self.Send_keys(self.input_name,nate_Name["normal_Email_2"])
        self.Clear(self.input_name)

        self.Send_keys(self.input_name,nate_Name["normal_Email_3"])
        self.Clear(self.input_name)

        # 비정상 이름 입력 및 alert 팝업창 출력 확인
        self.Send_keys(self.input_name,nate_Name["abnormal_Email_1"])
        self.Click(self.next_page)
        wd(driver=self.inter.driver,timeout=10).until(ec.alert_is_present())
        result = self.inter.driver.switch_to.alert
        assert result.text == "이름은 한글 또는 영어로만 입력이 가능합니다."
        result.dismiss()
        self.Clear(self.input_name)

        self.Send_keys(self.input_name,nate_Name["abnormal_Email_5"])
        self.Click(self.next_page)
        wd(driver=self.inter.driver,timeout=10).until(ec.alert_is_present())
        result = self.inter.driver.switch_to.alert
        assert result.text == "이름의 입력 형식이 올바르지 않습니다."
        result.dismiss()
        self.Clear(self.input_name)

        self.Send_keys(self.input_name,nate_Name["abnormal_Email_2"])
        self.Click(self.next_page)
        wd(driver=self.inter.driver,timeout=10).until(ec.alert_is_present())
        result = self.inter.driver.switch_to.alert
        assert result.text == "이름에 숫자가 들어갈 수 없습니다."
        result.dismiss()
        self.Clear(self.input_name)

        self.Send_keys(self.input_name,nate_Name["abnormal_Email_3"])
        self.Click(self.next_page)
        wd(driver=self.inter.driver,timeout=10).until(ec.alert_is_present())
        result = self.inter.driver.switch_to.alert
        assert result.text == "생년월일을 선택해 주세요."
        result.dismiss()
        self.Clear(self.input_name)

        self.Send_keys(self.input_name,nate_Name["abnormal_Email_4"])
        self.Click(self.next_page)
        wd(driver=self.inter.driver,timeout=10).until(ec.alert_is_present())
        result = self.inter.driver.switch_to.alert
        assert result.text == "한글 20자, 영문 40자 이상 입력하실 수 없습니다."
        result.dismiss()
        self.Clear(self.input_name)
    
    def Information_date(self):
        # 년도 클릭
        self.Click(self.year)
        self.Click((By.CSS_SELECTOR,"[value ='1900']"))
        self.Click(self.year)
        self.Click((By.CSS_SELECTOR,"[value ='1950']"))
        self.Click(self.year)
        self.Click((By.CSS_SELECTOR,"[value ='2000']"))
        self.Click(self.year)
        self.Click((By.CSS_SELECTOR,"[value ='2010']"))
        self.Click(self.year)
        self.Click((By.CSS_SELECTOR,"[value ='2023']"))
        self.Click(self.next_page)
        wd(driver=self.inter.driver,timeout=10).until(ec.alert_is_present())
        result = self.inter.driver.switch_to.alert
        assert result.text == "생년월일을 선택해 주세요."
        result.dismiss()

        # 월 클릭
        self.Click(self.month)
        self.Click((By.CSS_SELECTOR,"[value ='1']"))
        self.Click(self.month)
        self.Click((By.CSS_SELECTOR,"[value ='3']"))
        self.Click(self.month)
        self.Click((By.CSS_SELECTOR,"[value ='6']"))
        self.Click(self.month)
        self.Click((By.CSS_SELECTOR,"[value ='10']"))
        self.Click(self.month)
        self.Click((By.CSS_SELECTOR,"[value ='12']"))
        self.Click(self.next_page)
        wd(driver=self.inter.driver,timeout=10).until(ec.alert_is_present())
        result = self.inter.driver.switch_to.alert
        assert result.text == "생년월일을 선택해 주세요."
        result.dismiss()

        # 일 클릭
        self.Click(self.day)
        self.Click((By.CSS_SELECTOR,"[value ='1']"))
        self.Click(self.day)
        self.Click((By.CSS_SELECTOR,"[value ='10']"))
        self.Click(self.day)
        self.Click((By.CSS_SELECTOR,"[value ='15']"))
        self.Click(self.day)
        self.Click((By.CSS_SELECTOR,"[value ='28']"))
        self.Click(self.day)
        self.Click((By.CSS_SELECTOR,"[value ='31']"))
        self.Click(self.next_page)
        wd(driver=self.inter.driver,timeout=10).until(ec.alert_is_present())
        result = self.inter.driver.switch_to.alert
        assert result.text == "생년월일을 선택해 주세요."
        result.dismiss()

    def Information_gender(self):
        self.Click(self.man)
        self.Click(self.girl)
        self.Click(self.man)

    def under_14_Next_page(self):
        self.Send_keys(self.input_name,nate_Name["홍길동"])
        self.Click(self.year)
        self.Click((By.CSS_SELECTOR,"[value ='2015']"))
        self.Click(self.month)
        self.Click((By.CSS_SELECTOR,"[value ='10']"))
        self.Click(self.day)
        self.Click((By.CSS_SELECTOR,"[value ='25']"))
        self.Click(self.man)
        self.Click(self.next_page)
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2"))).text == "14세 미만 법정대리인 동의를"
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2 > br"))).text == "진행해 주세요."
        self.Click(self.back_page)

    def Up_14_Next_page(self):
        self.Send_keys(self.input_name,nate_Name["홍길동"])
        self.Click(self.year)
        self.Click((By.CSS_SELECTOR,"[value ='1900']"))
        self.Click(self.month)
        self.Click((By.CSS_SELECTOR,"[value ='3']"))
        self.Click(self.day)
        self.Click((By.CSS_SELECTOR,"[value ='10']"))
        self.Click(self.girl)
        self.Click(self.next_page)












