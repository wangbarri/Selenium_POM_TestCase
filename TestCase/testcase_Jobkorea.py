from Pages.Jobkorea.PageLogin import Login_Job
from tpffpsldna.Pages.Jobkorea.PageSearch import Job_Search
from tpffpsldna.Pages.Jobkorea.Page_JDC import JD

from tpffpsldna.TestCase.Test import TestRun
from selenium.webdriver.common.by import By

import time

class Job(TestRun):

   # def test_1_Login(self):
    #    login = Login_Job(self.inter)
     #   login.Login()
      #  self.assertEqual("한철현", self.inter.driver.find_element(By.CSS_SELECTOR,"#devLogin > div > div.myInfo > span.name > a").text)

    def test_1_Search(self):
        job = Job_Search(self.inter)
        job.get()
        job.Serch_JD()
        # job.Local_Conditions()
        # job.Category()
        # self.assertEqual("서울", self.inter.driver.find_element(By.CSS_SELECTOR,"#search > div > div > div.search-form > div.search-form-district.pseudo-icn.district > div.search-form-wrap.pseudo-icn.arw-big > button").text)

   # def test_3_JD_Crawling(self):
     #   jd = JD(self.inter)
      #  jd.JD_Crawling()


