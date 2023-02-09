from tpffpsldna.Pages.MyPage.PageLogin import Login
from tpffpsldna.Pages.MyPage.PageMypageList import MypageList
from tpffpsldna.Pages.MyPage.PageCheck import Check


from tpffpsldna.TestCase.Test import TestRun
from selenium.webdriver.common.by import By


import time

class TestCase(TestRun):

    def test_1_Login(self):
        login = Login(self.inter)
        login.get()
        login.Login_send_keys_ID()
        login.Login_send_keys_PW()
        login.Login_btn()
        self.assertEqual(self.inter.driver.current_url, "https://www.musinsa.com/app/")
    
         
    def test_2_Basket_List(self):
        BK = MypageList(self.inter)
        BK.get()
        self.assertEqual(self.inter.driver.current_url,"https://www.musinsa.com/categories/item/001")
        BK.Brand_sale_Selected()
        BK.Item_1_Page()
   
        
    
    def test_3_Cart_item_Check(self):
        Cart = Check(self.inter)
        Cart.Check_Basket()
        self.assertEqual(self.inter.driver.find_element(By.XPATH,'//*[@id="page_cart"]/form[1]/div/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td[3]/div[2]/p[2]/a').text, "[무신사 스탠다드] 베이식 긴팔 티셔츠 2팩")
    
    def test_4_Check_mypage(self):
        Cart = Check(self.inter)
        Cart.Check_Mypage()
        self.assertEqual(self.inter.driver.find_elements(By.CLASS_NAME,"name")[0].text, "스웨트셔츠 [블랙]")
        self.assertEqual(self.inter.driver.find_elements(By.CLASS_NAME,"name")[1].text, "베이식 긴팔 티셔츠 2팩")
    
    def test_5_Check_mypage(self):
        Cart = Check(self.inter)    
        Cart.Check_Like()
        self.assertEqual(self.inter.driver.find_elements(By.CLASS_NAME,"name")[0].text, "스웨트셔츠 [블랙]")
        self.assertEqual(self.inter.driver.find_elements(By.CLASS_NAME,"name")[1].text, "베이식 긴팔 티셔츠 2팩")
        
   
