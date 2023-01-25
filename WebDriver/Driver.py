from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Driver():
    
    def __init__(self):
       
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
        
        # Selenium Grid
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        # options.set_capability('browserName', 'chrome')
        # self.driver = webdriver.Remote(command_executor='http://localhost:----/wd/hub',options=options)
        


