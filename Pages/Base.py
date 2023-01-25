from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from tpffpsldna.WebDriver.Driver import Driver

class BaseItem:
    def __init__(self,driver):
        self.inter = driver or Driver()
        self.wait = WebDriverWait(driver=self.inter.driver,timeout=10)
    
    def Get(self,url): # url 이동
        self.inter.driver.get(url)

    def Send_keys(self,locator,value):
        self.inter.driver.find_element(*locator).send_keys(value)

    def Clear(self, locator):
        try:
          self.wait.until(ec.visibility_of_element_located(*locator)).clear()
        except NoSuchElementException:
            raise NoSuchElementException ("\n * ELEMENT NOT FOUND ")
        except TimeoutException:
            raise TimeoutException("Timeout")

    def Click(self, *locator):
        try:
            self.wait.until(ec.element_to_be_clickable(*locator)).click()
            
        # 에러발생
        except NoSuchElementException:
            raise NoSuchElementException ("\n * ELEMENT NOT FOUND ")
        except TimeoutException:
            raise TimeoutException("Timeout")

    def Find_Element(self, *locator):
        try:
            self.wait.until(ec.visibility_of_element_located(*locator))
            return self.inter.driver.find_element(*locator)

        # 에러발생
        except NoSuchElementException:
            raise NoSuchElementException ("\n * ELEMENT NOT FOUND ")
        except TimeoutException:
            raise TimeoutException("Timeout")

    def Find_Elements(self, *locator):
        try:    
            self.wait.until(ec.visibility_of_element_located(*locator))
            # return self.inter.driver.find_elements(*locator)
        
        # 에러발생
        except NoSuchElementException:
            raise NoSuchElementException ("\n * ELEMENT NOT FOUND ")
        except TimeoutException:
            raise TimeoutException("Timeout")

    def SendKeys_ENTER(self, locator):
        try:    
            self.inter.driver.find_element(*locator).send_keys(Keys.ENTER)
        
        # 에러발생
        except NoSuchElementException:
            raise NoSuchElementException ("\n * ELEMENT NOT FOUND ")
        except TimeoutException:
            raise TimeoutException("Timeout")

            
      
    
    












