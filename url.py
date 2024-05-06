import import_packages,Elements,time
from import_packages import driver_details ,By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def check_url():
    url_result=''
    try:
        driver_details.driver.get(Elements.login_webelements.app_url)
        driver_details.driver.maximize_window()

        # Handling the security warnings (if any)
        advanced_element = WebDriverWait(driver_details.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Elements.login_webelements.advanced_element)))
        advanced_element.click()
        proceed_link = WebDriverWait(driver_details.driver, 20).until(EC.element_to_be_clickable((By.ID, Elements.login_webelements.proceed_link)))
        proceed_link.click()
        print("Entering the Credentails now")
        time.sleep(5)
        current_url = driver_details.driver.current_url
        print(current_url)
        if current_url == Elements.login_webelements.validation_url:
           url_result = 'Url Check pass'
        else:
            url_result = 'Url Check Fail'

    except Exception as e:
        print(f"An error occurred: {e}")
    return url_result