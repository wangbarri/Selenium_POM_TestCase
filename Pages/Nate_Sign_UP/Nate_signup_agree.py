from tpffpsldna.Pages.Base import BaseItem
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as ec

import time

class Nate_Agree(BaseItem):

    # 회원가입 약관 동의 locator
    Agree_URL = "https://member.nate.com/Member/Regist/Join.sk?cp=main"

    All_Check = (By.CSS_SELECTOR, "#checkPolicy > div.allchkBtn > label")
    Check_service = (By.CSS_SELECTOR, "#checkPolicy > ul > li:nth-child(1) > span > label")
    Check_Privacy = (By.CSS_SELECTOR,"#checkPolicy > ul > li:nth-child(2) > span > label")
    Check_advertisement = (By.CSS_SELECTOR, "#checkPolicy > ul > li:nth-child(3) > span > label")

    link_service = (By.LINK_TEXT, "이용약관 더보기")
    link_Privacy = (By.LINK_TEXT, "개인정보 수집 및 이용약관 더보기")
    link_advertisement = (By.LINK_TEXT, "광고성 정보 수신동의 약관 더보기")

    link_any_signup = (By.LINK_TEXT, "법인 / 단체 회원가입")

    next_page = (By.CSS_SELECTOR, "#nextBtn")

    def __init__(self, driver):
        super(Nate_Agree, self).__init__(driver)

    def Sign_Up_agree(self):
        # URL 이동
        self.Get(self.Agree_URL)
        
        # 모두 동의 및 안내 텍스트 노출 확인(다음 버튼 활성화 확인)
        self.Click(self.All_Check)
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#checkPolicy > div.agree-tit"))).text == "필수 및 선택 정보를 한번에 동의하실 수 있습니다."
        self.Click(self.All_Check)

        # 각 이용약관 확인 및 체크 
        self.Click(self.Check_service)
        self.Click(self.Check_Privacy)
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        print(elements)
        assert elements == "active on"
        self.Click(self.Check_advertisement)
        
        # # 각 이용약관 체크 해제(다음 버튼 비활성화 확인)
        self.Click(self.Check_service)
        self.Click(self.Check_Privacy)
        elements = self.inter.driver.find_element(By.CSS_SELECTOR,"#nextBtn").get_attribute("class")
        print(elements)
        assert elements == "active"
        self.Click(self.Check_advertisement)

        # 각 이용약관 내용이 담겨있는 링크 진입
        # 서비스 > 개인정보 > 광고성 정보
        self.Click(self.link_service)
        time.sleep(2)
        self.inter.driver.switch_to.window(self.inter.driver.window_handles[-1])
        assert self.inter.driver.find_element(By.CSS_SELECTOR,"#agree_wrap > p:nth-child(2)").text == "이 서비스 이용약관(이하 “약관”이라 합니다)은 SK커뮤니케이션즈㈜(이하 “회사”라 합니다)가 제공하는 서비스와 관련하여 회사와 이용 고객(또는 회원) 간에 서비스의 이용 조건 및 절차, 회사와 회원 간의 권리, 의무 및 책임 사항 기타 필요한 사항을 규정함을 목적으로 합니다."
        self.inter.driver.close()
        self.inter.driver.switch_to.window(self.inter.driver.window_handles[-1])
        
        self.Click(self.link_Privacy)
        time.sleep(2)
        self.inter.driver.switch_to.window(self.inter.driver.window_handles[-1])
        assert self.inter.driver.find_element(By.CSS_SELECTOR,"#morecnt > div > h1").text == "네이트 개인정보 수집 및 이용동의"
        self.inter.driver.close()
        self.inter.driver.switch_to.window(self.inter.driver.window_handles[-1])

        self.Click(self.link_advertisement)
        time.sleep(2)
        self.inter.driver.switch_to.window(self.inter.driver.window_handles[-1])
        assert self.inter.driver.find_element(By.CSS_SELECTOR,"#morecnt > div > h1").text == "광고성 정보 수신 동의"
        self.inter.driver.close()
        self.inter.driver.switch_to.window(self.inter.driver.window_handles[-1])

        # 법인 / 단체 회원가입 페이지 이동 확인
        self.Click(self.link_any_signup)
        self.inter.driver.back()
        
        # 다음 버튼 클릭으로 다음 절차 페이지 이동
        self.Click(self.All_Check)
        self.Click(self.next_page)

        # 휴대폰 인증 페이지 이동 확인
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > h2"))).text == "휴대폰 인증을 진행해 주세요."
        assert wd(driver=self.inter.driver,timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#content > div"))).text == "휴대폰 번호는 아이디/비밀번호 찾기에 사용됩니다."
        
        







