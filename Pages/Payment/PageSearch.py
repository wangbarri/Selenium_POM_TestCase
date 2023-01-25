from tpffpsldna.Pages.Base import BaseItem
from tpffpsldna.Config.Accounts import *

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class search(BaseItem):
    URL = "https://www.musinsa.com/app/"
    input_Search = (By.ID,"search_query")
    click_Search_Btn = (By.ID,"search_button")
    clear = (By.CSS_SELECTOR,"#search_query")

    def __init__(self,driver):
        super(search,self).__init__(driver)

    def get(self):
        self.Get(self.URL)

    def Item_send_keys(self):
        for i in Item:
            self.Click(self.input_Search)
            self.inter.driver.find_element(By.CSS_SELECTOR,"#search_query").send_keys(Keys.CONTROL + "a")
            time.sleep(1)
            self.inter.driver.find_element(By.CSS_SELECTOR,"#search_query").send_keys(Keys.DELETE)
            self.Send_keys(self.input_Search,i)
            self.Click(self.click_Search_Btn)
