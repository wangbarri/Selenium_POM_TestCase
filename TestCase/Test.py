import time
import unittest
import xmlrunner

from tpffpsldna.WebDriver.Driver import Driver

class TestRun(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.inter = Driver()
        cls.inter.driver.maximize_window()
        
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        return xmlrunner.XMLTestRunner(output='test_result')
    
    @classmethod
    def tearDownClass(cls) -> None:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_result'))
        cls.inter.driver.quit()
       # unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_result'))
        return xmlrunner.XMLTestRunner(output='test_result')
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRun)
    unittest.TextTestRunner(verbosity=2).run(suite)

