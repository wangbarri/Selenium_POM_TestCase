from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Check(BaseItem):
    
    basket_page = (By.CSS_SELECTOR,"#default_top > div.header-member > div:nth-child(7) > a")
    Mypage_page = (By.CSS_SELECTOR,"#default_top > div.header-member > div:nth-child(4) > a")
    
    def __init__(self,driver):
        super(Check,self).__init__(driver)

    def Check_Basket(self):
        self.Click(self.basket_page)
       
        # basket_item = self.inter.driver.find_element(By.CSS_SELECTOR,".table_basic.cart_table.n-cart-table").find_elements(By.CSS_SELECTOR,".cart-group")
        # for list in basket_item:
        #     cart_item = list.find_element(By.CLASS_NAME,"list_info").text

    def Check_Mypage(self):
        self.Click(self.Mypage_page)
        self.inter.driver.find_element(By.XPATH,"//*[@id='commonMypage']/nav/div[1]/a[6]").send_keys(Keys.ENTER)
    
    def Check_Like(self):
        self.inter.driver.find_element(By.XPATH,'//*[@id="commonMypage"]/nav/div[1]/a[6]').send_keys(Keys.ENTER)




