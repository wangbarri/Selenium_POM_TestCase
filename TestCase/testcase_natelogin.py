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
    



