from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BrowserInteraction():

    def test(self):

    # open google and search for Kavinraj Antony

        driver = webdriver.Firefox()
        driver.get(url)
        time.sleep(3)
        driver.maximize_window()
        search_box = driver.find_element(By.XPATH, xpath_of_input)
        search_box.send_keys(text)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)
        current_url = driver.current_url
        print(f"the current URL is :" + current_url)
        driver.refresh()
        time.sleep(3)
        driver.get(current_url)
        
        driver.quit()


url = "https://www.google.co.in/"
xpath_of_input = '//textarea[@id="APjFqb"]'
text = "Kavinraj Antony"

a = BrowserInteraction()

a.test()

class CloseQuit():
    def test_close(self):
    
    # i want to test the close method of selenium webdriver
        baseurl = "https://www.google.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)

        driver.close()

a = CloseQuit()

a.test_close()










