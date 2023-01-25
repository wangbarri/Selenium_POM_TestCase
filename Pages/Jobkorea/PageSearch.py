from tpffpsldna.Config.Accounts import *
from tpffpsldna.Pages.Base import BaseItem

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

class Job_Search(BaseItem):
    URL = "https://www.jobkorea.co.kr/"
    input_job = (By.ID,"stext")
    Search_btn = (By.ID,"common_search_btn")

    local_conditions = (By.CSS_SELECTOR,"#search > div > div > div.search-form > div.search-form-district.pseudo-icn.district > div.search-form-wrap.pseudo-icn.arw-big > button")
    local_conditions_Seoul_all_assert = (By.XPATH,'//*[@id="toolitems"]/li/button')
    local_condition_select_btn = (By.ID,"dev-btn-search")

    job_category_Career = (By.CSS_SELECTOR,"#careerTitle")
    job_category_Career_1 = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.exp.simple > div > div.ly-cnt > div.choose-box > ul > li:nth-child(1) > label")
    job_category_Career_btn = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.exp.simple > div > div.ly-cnt > div.btns > button.btn-apply.pseudo-icn")

    job_category_business = (By.CSS_SELECTOR,"#coTypeTitle")
    job_category_business_1 = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.scale.simple > div > div.ly-cnt > ul > li:nth-child(1) > label")
    job_category_business_2 = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.scale.simple > div > div.ly-cnt > ul > li:nth-child(4) > label")
    job_category_business_3 = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.scale.simple > div > div.ly-cnt > ul > li:nth-child(7) > label")
    job_category_business_4 = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.scale.simple > div > div.ly-cnt > ul > li:nth-child(8) > label")
    job_category_business_btn = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.scale.simple > div > div.ly-cnt > div > button.btn-apply.pseudo-icn")

    job_category_academic = (By.CSS_SELECTOR,"#eduTitle")
    job_category_academic_1 = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.edu.simple > div > div.ly-cnt > ul > li:nth-child(2) > label")
    job_category_academic_btn = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.edu.simple > div > div.ly-cnt > div > button.btn-apply.pseudo-icn")

    job_category_type = (By.CSS_SELECTOR,"#jobTypeTitle")
    job_category_type_1 = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.type.simple > div > div.ly-cnt > ul > li:nth-child(1) > label")
    job_category_type_2 = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.type.simple > div > div.ly-cnt > ul > li:nth-child(2) > label")
    job_category_type_3 = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.type.simple > div > div.ly-cnt > ul > li:nth-child(3) > label")
    job_category_type_btn = (By.CSS_SELECTOR,"#optional > div > div.optional-detail.clear > div.type.simple > div > div.ly-cnt > div > button.btn-apply.pseudo-icn")


    def __init__(self, driver):
        super(Job_Search,self).__init__(driver)
    
    def get(self):
        self.Get(self.URL)

    def Serch_JD(self):
        
        self.Send_keys(self.input_job,"QA 엔지니어")
        self.Click(self.Search_btn)

    def Local_Conditions(self):
        self.Click(self.local_conditions)
        
        # 지역 선택 조건 선택 
        time.sleep(2)
        a = self.inter.driver.find_element(By.XPATH,'//*[@id="search"]/div/div/div[1]/div[2]/div[2]/div[4]')
        ActionChains(self.inter.driver).click(a).perform()

        time.sleep(2)
        b = self.inter.driver.find_element(By.CSS_SELECTOR,"#search > div > div > div.search-form.on > div.search-form-district.pseudo-icn.district.on > div.layer-comn.lyDistrict > div.ly_sub_cnt.colm2-ty2.clear > dl.detail_sec.barType > dd > div.nano-content.dev-main > ul > li:nth-child(1) > label")
        ActionChains(self.inter.driver).click(b).perform()
        
        self.Click(self.local_condition_select_btn)

  
    def Category(self):
        # 경력 사항 추가
        self.Click(self.job_category_Career)
        self.Click(self.job_category_Career_1)
        self.Click(self.job_category_Career_btn)
        time.sleep(1)

        # 학력 사항 추가
        self.Click(self.job_category_academic)
        self.Click(self.job_category_academic_1)
        self.Click(self.job_category_academic_btn)
        time.sleep(1)
        
        # 기업 형태 추가
        self.Click(self.job_category_business)
        self.Click(self.job_category_business_1)
        self.Click(self.job_category_business_2)
        self.Click(self.job_category_business_3)
        self.Click(self.job_category_business_4)
        self.Click(self.job_category_business_btn)
        time.sleep(1)   

        # 고용 형태 추가
        self.Click(self.job_category_type)
        self.Click(self.job_category_type_1)
        self.Click(self.job_category_type_2)
        self.Click(self.job_category_type_3)
        self.Click(self.job_category_type_btn)
        time.sleep(2)





