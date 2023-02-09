from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

class MypageList(BaseItem):
    # 상의 > 전체 > 무신사 스탠다드 > 세일 상품 > 
    # 1 2 페이지 상품 중간 쯤꺼 1개씩 > 옵션 선택 >  
    # 장바구니 담기 > 장바구니에 상품이 print로 확인

    URL = "https://www.musinsa.com/categories/item/001"
    Top_category = (By.CSS_SELECTOR,"#ui-id-3")
    Top_category_all = (By.CSS_SELECTOR,"#ui-id-4 > div > a")

    Brand = (By.CSS_SELECTOR,"#brand_list_area_exclusive > li:nth-child(1) > a > span.brand_name.brandNameOff")
    Sale = (By.CSS_SELECTOR,"#goods_list > div.boxed-list-wrapper > div.thumbType_box.box > span:nth-child(3) > label > input")
    
    item_1 = (By.CSS_SELECTOR,"[title='베이식 긴팔 티셔츠 2팩']")
    item_1_option1 = (By.ID,"option1")
    item_1_option2 = (By.ID,"option2")

    item_2 = (By.CSS_SELECTOR,"[title='스웨트셔츠 [블랙]']")
    item_2_option = (By.ID,"option1")

    like_btn = (By.CSS_SELECTOR,"#buy_option_area > div.box-btn-buy.wrap-btn-buy > div.btn_mylike > a > i")
    basket_btn = (By.CSS_SELECTOR,"#buy_option_area > div.box-btn-buy.wrap-btn-buy > div.btn_cart > a")
    popup_close = (By.XPATH,'/html/body/div/div/div/div/a[1]')
    
    def __init__(self, driver):
        super(MypageList,self).__init__(driver)

    def get(self):
        self.Get(self.URL)
        
    def Brand_sale_Selected(self):
        self.Click(self.Brand)
        self.Click(self.Sale)
    
    def Item_1_Page(self):
        self.Click(self.item_1)
        self.Click(self.item_1_option1)
        WebDriverWait(driver=self.inter.driver, timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"[value='01.화이트/화이트']"))).click()
        self.Click(self.item_1_option2)
        WebDriverWait(driver=self.inter.driver, timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"[value='XL']"))).click()
        time.sleep(3)
        self.Click(self.popup_close)
        time.sleep(3)
        self.Click(self.item_1_option1)
        WebDriverWait(driver=self.inter.driver, timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"[value='01.화이트/화이트']"))).click()
        self.Click(self.item_1_option2)
        WebDriverWait(driver=self.inter.driver, timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"[value='XL']"))).click()
        self.Click(self.basket_btn)
        #self.Click(self.like_btn)
        time.sleep(1)
        self.inter.driver.back()

    def Item_2_Page(self):
        self.Click(self.item_2)
        self.Click(self.item_2_option)
        WebDriverWait(driver=self.inter.driver, timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"[value='L']"))).click()
        time.sleep(2)
        self.Click(self.like_btn)
        time.sleep(1)
        self.Click(self.basket_btn)
        time.sleep(1)
        self.inter.driver.back()
    

        

