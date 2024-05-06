import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from Elements import login_webelements
import traceback
from flask import Flask,render_template
import datetime


class driver_details:
        driver_path = r'C:\Users\w136610\Downloads\chromedriver-win64\chromedriver.exe'
        #driver_path = r'C:\Users\w136610\Downloads\Chromedriver\chromedriver-win64\chromedriver.exe'
        service = Service(driver_path)
        # Set up Chrome options
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(service=service, options=options)
        actions = ActionChains(driver)
        #WebDriverWait = WebDriverWait(driver, 20)

