from tpffpsldna.Pages.Payment.PageLogin import Login
from tpffpsldna.Pages.Payment.PageSearch import search
from tpffpsldna.Pages.Payment.Pagebasket import Basket
from tpffpsldna.Pages.Payment.PageOrder import Order
from tpffpsldna.Pages.Payment.PageNaverPay import NaverPay

from tpffpsldna.TestCase.Test import TestRun

import time

class TestCase(TestRun):

    def test_1_Login(self):
        login = Login(self.inter)
        login.get()
        login.Login_send_keys_ID()
        login.Login_send_keys_PW()
        login.Login_btn()
        self.assertEqual(self.inter.driver.current_url, "https://www.musinsa.com/app/")

    def test_2_Item_Search(self):
        Search = search(self.inter)
        Search.get()
        self.assertEqual(self.inter.driver.current_url, "https://www.musinsa.com/app/")
        Search.Item_send_keys()

    def test_3_Basket_Item(self):
        basket = Basket(self.inter)
        basket.get()
        self.assertEqual(basket.product_title(), "Ultimashow Shoes")
        basket.Add_item_basket()

    def test_4_order(self):
        order = Order(self.inter)
        order.Order_Btn_Click()
        order.Shipping_Note()
        order.Naver_pay_click()
        order.PayMent_Item()
        
    def test_5_NaverPay_payment(self):
        navpay = NaverPay(self.inter)
        navpay.Naver_login()
        navpay.keypad_selected_pyautogui()
        
        



        






