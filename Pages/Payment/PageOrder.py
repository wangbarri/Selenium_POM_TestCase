from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Order(BaseItem):
    
    Order_btn = (By.CSS_SELECTOR,"#btn-order")

    shipping_note = (By.CSS_SELECTOR,"#dlv_selectbox")
    shipping_value = (By.CSS_SELECTOR,"#dlv_selectbox > option:nth-child(7)")
    shipping_text = (By.ID,"etc_textarea")
    
    Card_selected = (By.CSS_SELECTOR, "#payment_info_area > div.__payment-view.__payment-pg-view > ul > li.cell_discount_detail.payment-area > div.payment-area-wrap > label:nth-child(2)")
    Card_sinhan_selected = (By.CSS_SELECTOR, "#card_code")
    Card_sinhan_value = (By.CSS_SELECTOR, "[value='CCLG']")

    naver_pay = (By.CSS_SELECTOR,"#payment_info_area > div.__payment-view.__payment-pg-view > ul > li.cell_discount_detail.payment-area > div.payment-area-wrap > label:nth-child(14)")
    
    Payment = (By.CSS_SELECTOR,"#btn_pay")

    def __init__(self,driver):
        super(Order,self).__init__(driver)
    
    def Order_Btn_Click(self):
        self.Click(self.Order_btn)
    
    def Shipping_Note(self):
        self.Click(self.shipping_note)
        self.Click(self.shipping_value)
        self.inter.driver.find_element(By.ID,"etc_textarea").send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        self.inter.driver.find_element(By.ID,"etc_textarea").send_keys(Keys.DELETE)
        self.Send_keys(self.shipping_text,shippings["직접입력"])
        

    def Card_Click(self):
        self.Click(self.Card_selected)
        self.Click(self.Card_sinhan_selected)
        self.Click(self.Card_sinhan_value)
        
        
    def Naver_pay_click(self):
        self.Click(self.naver_pay)

    def PayMent_Item(self):
        self.Click(self.Payment)
        