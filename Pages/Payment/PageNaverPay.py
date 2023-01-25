from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *

from selenium.webdriver.common.by import By
import time, pyautogui, pyperclip, os

class NaverPay(BaseItem):
    
    naver_login_ID = (By.ID,"id")
    naver_login_PW = (By.ID,"pw")
    naver_login_btn = (By.CSS_SELECTOR,"#log\.login")
    naver_payment = (By.XPATH,"//*[@id='paymentSheetForm']/div/div/div[3]/button[1]")
    

    def __init__(self,driver):
        super(NaverPay,self).__init__(driver)

    def Naver_login(self):
        # 새로운 창 전환
        driver = self.inter.driver
        driver.switch_to.window(driver.window_handles[1])
        
        self.Click(self.naver_login_ID)
        pyperclip.copy(ID["Naver_ID"])
        pyautogui.hotkey("ctrl","v")

        # 네이버 비번
        self.Click(self.naver_login_PW)
        pyperclip.copy(PW["Naver_PW"])
        pyautogui.hotkey("ctrl","v")

        self.Click(self.naver_login_btn)
        self.Click(self.naver_payment)
        time.sleep(5)

    def keypad_selected_pyautogui(self):
        number_image = ["Naver_Pay_Keypad(0)","Naver_Pay_Keypad(1)","Naver_Pay_Keypad(6)"]
        
        for i in number_image:
            naverpay_keypad = pyautogui.locateOnScreen("Image/"+ i +".png")
            pyautogui.click(naverpay_keypad)






