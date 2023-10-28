from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class atmosol():

    def test(self):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        
        username_input = driver.find_element(By.ID , "user-name")
        username_input.send_keys(username)
        
        password_input = driver.find_element(By.ID , "password")
        password_input.send_keys(password)

        submit_button = driver.find_element(By.ID , "login-button")
        submit_button.click()
        driver.implicitly_wait(15)

        menu_button = driver.find_element(By.ID , "react-burger-menu-btn")
        menu_button.click()
        driver.implicitly_wait(15)
        
        about_button = driver.find_element(By.ID , "about_sidebar_link")
        about_button.click()
        driver.implicitly_wait(15)

        try :
            driver.back()
            driver.implicitly_wait(15)
        except :
            print("back button is not found") 

        try :
            sort_by_button = driver.find_element(By.XPATH , '//select[@class="product_sort_container"]') 
            sort_by_button.click()
            driver.implicitly_wait(15)
            time.sleep(5)

        except :
            print("sort by button is not found") 

        sort_by_button.send_keys(Keys.ARROW_DOWN)



        driver.quit()


url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

a = atmosol()
b = atmosol()

a.test()