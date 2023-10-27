import time
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class Kavin:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()

    def cred_input(self, emailID, password):
        self.driver.get(self.url)
        time.sleep(5)
        input1 = self.driver.find_element(By.NAME , value= "email")
        input1.send_keys(emailID)
        input2 = self.driver.find_element(By.NAME, value= "password")
        input2.send_keys(password)
        input1.send_keys(Keys.ENTER)
        print(self.driver.title)
        time.sleep(5)
        self.driver.close()

    
url = "https://www.zenclass.in/class"

a = Kavin(url)

a.cred_input("kavinraj.antony@gmail.com" , "Stark@3112")

