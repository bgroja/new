from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import import_packages
from import_packages import driver_details
import Elements,time,traceback

def login():
   login_validation_result = ''
   try:
        time.sleep(10)
        username_element = driver_details.driver.find_element(By.NAME,Elements.login_webelements.username_element)
        username_element.send_keys('W136610')

        pwd_element = driver_details.driver.find_element(By.XPATH,Elements.login_webelements.password_element)
        driver_details.actions.move_to_element(pwd_element)
        driver_details.actions.click()  # If necessary
        time.sleep(3)
        driver_details.actions.send_keys('Welcome-welcome5f')
        driver_details.actions.perform()
        login_element = driver_details.driver.find_element(By.XPATH, Elements.login_webelements.login_element)
        login_element.click()
        time.sleep(10)  # Add a wait for the next page to load
        login_validation_element = driver_details.driver.find_element(By.XPATH,Elements.login_webelements.login_validation_element)
        time.sleep(8)
        if login_validation_element.is_displayed():
            login_validation_result = 'Login Successful'
            print(login_validation_result)
        else:
            login_validation_result = 'Login Unsuccessful'
            print(login_validation_result)
   except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
   return  login_validation_result