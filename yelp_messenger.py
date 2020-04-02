import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC


class Browser:

    def __init__(self, has_screen):

        """ A browser class for opening Yelp profile, logging in
        and sending messages to user.

        Attributes:
            driver () Chrome driver to open up Chrome browser
            """

        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # print(dir_path)
        # service_args = ["--ignore-ssl-errors=true"]
        chrome_options = Options()
        # if not has_screen:
        #     chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(
            # executable_path= "%s/bin/chromedriver" % dir_path,
            # service_args=service_args,
            chrome_options=chrome_options,
        )
        self.driver.implicitly_wait(5)

    def gets(self, url):
        self.driver.get(url)
        return self.driver

    def login(self, profile):

        driver = self.gets(profile)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log In')))
        driver.find_element_by_link_text("Log In").click()

        username = driver.find_element_by_xpath("//form[@id='ajax-login']/input[2]")
        username.click()
        time.sleep(1)
        username.send_keys("INSERT_ID_HERE")
        time.sleep(1)

        password = driver.find_element_by_xpath("//form[@id='ajax-login']/input[3]")
        password.click()
        time.sleep(1)
        password.send_keys("INSERT_PASS_HERE")
        time.sleep(1)

        driver.find_element_by_xpath("//form[@id='ajax-login']/button").click()

        return self.driver

    def send_message(self):


        user_profile = pd.DataFrame({'profile': ['https://www.yelp.com/user_details?userid=3khkKOy0LdB60TqPK29utQ', 'https://www.yelp.com/user_details?userid=3khkKOy0LdB60TqPK29utQ'],
                                     'category': ['Father Day', 'Father Day']})
        
        print(user_profile)
        # Log into account
        driver = self.login(user_profile.iloc[0]['profile'])

        # 
        try:
            wait = WebDriverWait(driver, 3)
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Send message')))
            driver.find_element_by_link_text("Send message")

        except:
            
            print('bot police')
            


        for index, row in user_profile.iterrows():
            
            print(index)
            print(row['profile'])
            time.sleep(3)
            driver.get(row['profile'])

            driver.find_element_by_link_text("Send message").click()


            wait = WebDriverWait(driver, 10)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//form[@id='compForm']/input[5]")))

            if row['category'] == 'Mother Day':

                subject = driver.find_element_by_xpath("//form[@id='compForm']/input[5]")
                subject.click()
                time.sleep(1)
                subject.send_keys("Mother Day")
                time.sleep(1)

                message = driver.find_element_by_xpath("//form[@id='compForm']/textarea")
                message.click()
                time.sleep(1)
                message.send_keys("body message")
                time.sleep(2)

                driver.find_element_by_xpath("//div[@class='ypop-buttons']/button").click()

            else:
                print('no mother day')
                pass
                

            time.sleep(3)
        


        driver.close()

website = Browser(False)
website.send_message()