from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

class Basket(BaseItem):
    
    url = "https://www.musinsa.com/app/goods/2649028"
    basket_btn = (By.CSS_SELECTOR,"#buy_option_area > div.box-btn-buy.wrap-btn-buy > div.btn_cart > a > i")
    option_1 = (By.ID, "option1")
    basket_page = (By.CSS_SELECTOR,"#default_top > div.header-member > div:nth-child(7) > a")
    
    def __init__(self,driver):
        super(Basket,self).__init__(driver)
    
    def get(self):
        self.Get(self.url)
        
    def Add_item_basket(self):
        self.Click(self.option_1)
        WebDriverWait(driver=self.inter.driver, timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"[value='220']"))).click()
        
        try:
            self.Click(self.basket_btn)
            time.sleep(1)
        except:
            print("장바구니 미추가")

        self.Click(self.basket_page)
        
        

    def product_title(self):
        self.inter.driver.find_element(By.CSS_SELECTOR,"#page_product_detail > div.right_area.page_detail_product > div.right_contents.section_product_summary > span").text
        return "Ultimashow Shoes"





        # count = 1
        # a = self.inter.driver.find_element(By.CLASS_NAME,"boxed-list-wrapper").find_elements(By.CLASS_NAME,"li_box")
        # for i in a:
        #     self.inter.driver.find_element(By.XPATH,"//*[@id='searchList']/li[%d]/div[4]/div[2]/p[2]/a" %count).click()
        #     self.Click(self.option_1)
        #     WebDriverWait(driver=self.inter.driver, timeout=10).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"[value='220']"))).click()
        #     time.sleep(1.5)
        #     self.Click(self.basket_btn)
        #     self.inter.driver.back()
        #     count += 1
            
                
            
            
   


