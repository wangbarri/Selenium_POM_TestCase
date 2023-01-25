from tpffpsldna.TestCase.Test import TestRun
from tpffpsldna.Pages.Nate_Sign_UP.Nate_signup import Nate_Singup
from tpffpsldna.Pages.Nate_Sign_UP.Nate_signup_agree import Nate_Agree
from tpffpsldna.Pages.Nate_Sign_UP.Nate_signup_ID import Nate_ID
from tpffpsldna.Pages.Nate_Sign_UP.Nate_signup_PW import Nate_PW
from tpffpsldna.Pages.Nate_Sign_UP.Nate_signup_email import Nate_Email
from tpffpsldna.Pages.Nate_Sign_UP.Nate_signup_information import Nate_Information
from tpffpsldna.Pages.Nate_Sign_UP.Nate_signup_privacy import Nate_Privacy
from tpffpsldna.Pages.Nate_Sign_UP.Nate_signup_end import Nate_End
from tpffpsldna.Pages.Nate_Sign_UP.Nate_Login import Nate_Login


import time


class TestCases(TestRun):
    
    def testcase_1_Main(self):
        NS = Nate_Singup(self.inter)
        NS.Main_Sign_Up_join()
        self.assertEqual(self.inter.driver.current_url , "https://member.nate.com/Member/Regist/Join.sk?cp=main")

    def testcase_2_Agree(self):
        NA = Nate_Agree(self.inter)
        NA.Sign_Up_agree()

    def testcase_3_ID(self):
        NI = Nate_ID(self.inter)
        NI.ID_page_check()
        NI.ID_input_test()
        NI.next_page()
    
    def testcase_4_PW(self):
        NP = Nate_PW(self.inter)
        NP.PW_page_check()
        NP.PW_input_check()
        NP.PW_input_test()
        NP.input_PW_Check_test()
        NP.Next_page()

    def testcase_5_Email(self):
        NE = Nate_Email(self.inter)
        NE.Email_page_check()
        NE.Email_input_test()
        NE.Next_page()

    def testcase_6_Other_information(self):
        NO = Nate_Information(self.inter)
        NO.Information_page_check()
        NO.Information_Name()
        NO.Information_date()
        NO.Information_gender()
        NO.under_14_Next_page()
        NO.Up_14_Next_page()

    def testcase_7_Privacy(self):
        NP = Nate_Privacy(self.inter)
        NP.Privacy_page_check()
        NP.Privacy_Radio_btn()
        NP.Next_page()

    def testcase_8_End(self):
        NE = Nate_End(self.inter)
        NE.End_page_check()

    def testcase_9__Login(self):
        NL = Nate_Login(self.inter)
        NL.Login_page_check()



