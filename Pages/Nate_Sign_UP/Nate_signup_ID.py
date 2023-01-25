from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

class Nate_ID(BaseItem):
    
    warning_message = (By.CSS_SELECTOR,"#id_duplicate_check_result")
    input_ID = (By.CSS_SELECTOR,"#svc_id")
    double_check_btn = (By.CSS_SELECTOR,"#joinIdInfo > fieldset > div.ifBox.id > button")
   
    def __init__(self, driver):
        super(Nate_ID, self).__init__(driver)

    def ID_page_check(self):
        # 회원가입 아이디 생성 페이지 진입 확인
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2"))).text == "네이트 아이디를 만들어 주세요."
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > div"))).text == "네이트온 메신저 아이디와 네이트 메일 주소로 사용됩니다."

        # 아이디 입력란 영역 메시지 노출 확인
        self.inter.driver.find_element(By.CSS_SELECTOR,"#svc_id").get_attribute("placeholder") == "영문소문자, 숫자조합 6~40자 (-,_가능)"
    
    def ID_input_test(self):

        # 중복확인 버튼 클릭 후 경고 메시지 노출 확인
        self.Click(self.double_check_btn)
        self.Find_Element(self.warning_message)

        # 정상적인 / 가입되지 않은 ID 입력
        self.Send_keys(self.input_ID,nate_ID["normal_ID"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "사용할 수 있는 아이디입니다."
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active on"
        self.Clear(self.input_ID)


        self.Send_keys(self.input_ID,nate_ID["subscribed_ID"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "사용할 수 있는 아이디입니다."
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active on"
        self.Clear(self.input_ID)

        # 비정상적 / 가입된 ID 입력
        self.Send_keys(self.input_ID,nate_ID["abnormal_ID"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "사용할 수 없는 아이디입니다."
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active on"
        self.Clear(self.input_ID)


        self.Send_keys(self.input_ID,nate_ID["unsubscribed_ID"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "사용할 수 없는 아이디입니다."
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active on"
        self.Clear(self.input_ID)

        # 영소문자 / 숫자 /-,_ 5 ~ 40자리 조합 입력
        # 5자리 조합
        self.Send_keys(self.input_ID,nate_ID["Combination_5"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "영문소문자, 숫자조합 6~40자 (-,_가능)"
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active"
        self.Clear(self.input_ID)

        # 6자리 조합
        self.Send_keys(self.input_ID,nate_ID["Combination_6"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "사용할 수 있는 아이디입니다."
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active on"
        self.Clear(self.input_ID)

        # 15자리 조합
        self.Send_keys(self.input_ID,nate_ID["Combination_15"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "사용할 수 있는 아이디입니다."
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active on"
        self.Clear(self.input_ID)

        # 30자리 조합
        self.Send_keys(self.input_ID,nate_ID["Combination_30"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "사용할 수 있는 아이디입니다."
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active on"
        self.Clear(self.input_ID)

        # 40자리 조합
        self.Send_keys(self.input_ID,nate_ID["Combination_40"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "사용할 수 있는 아이디입니다."
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active on"
        self.Clear(self.input_ID)

        # 41자리 조합
        self.Send_keys(self.input_ID,nate_ID["Combination_41"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "영문소문자, 숫자조합 6~40자 (-,_가능)"
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active"
        self.Clear(self.input_ID)
    
    def next_page(self):
        self.Send_keys(self.input_ID,nate_ID["normal_ID"])
        self.Click(self.double_check_btn)
        assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#id_duplicate_check_result"))).text == "사용할 수 있는 아이디입니다."
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        assert elements == "active on"
        self.Click(self.next_page)

    


















    # def Image_captcha(self):
        
    #     img = cv2.imread(self.capcha_url, cv2.IMREAD_GRAYSCALE)
    #     # gray = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    #     gray = cv2.threshold(img, 127 ,255,cv2.THRESH_TRUNC)
   
        
    #     cv2.imshow('qw',gray)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()


    #     configg = ('--oem 3 --psm 8')
    #     text = pytesseract.image_to_string(img,config=configg)
        
    #     print(text)
    #     # assert WebDriverWait(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#checkPolicy > h2"))).text == "네이트 회원가입을 시작합니다!\n약관에 동의해 주세요."
    