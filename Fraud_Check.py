import Elements
from import_packages import Service,ActionChains,WebDriverWait,By,EC,webdriver,time
from Elements import login_webelements , fraud_Check
from import_packages import driver_details


def fraud_check_fun():
     Fraud_check_result = ''
     try:
        WebDriverWait(driver_details.driver, 10).until(EC.visibility_of_element_located((By.XPATH,fraud_Check.search_element)))
        search_element = driver_details.driver.find_element(By.XPATH, fraud_Check.search_element)
        time.sleep(10)
        driver_details.actions.move_to_element(search_element)
        driver_details.actions.click()
        driver_details.actions.perform()
        fraud_element = driver_details.driver.find_element(By.XPATH,fraud_Check.fraud_element)
        fraud_element.click()
        time.sleep(10)
        fraud_search_element = driver_details.driver.find_element(By.XPATH, fraud_Check.fraud_search_element)
        driver_details.actions.move_to_element(fraud_search_element)
        print('test')
        driver_details.actions.click().perform()
        #pop_element = driver_details.driver.find_element(By.XPATH,Elements.camt_054.pop_up_element)
        #pop_element.click()
        fraud_check_validation_element = driver_details.driver.find_element(By.XPATH,Elements.fraud_Check.fraud_check_validation_element)
        if fraud_check_validation_element.is_displayed() :
           Fraud_check_result = 'Fraud check View is Ready for testing'
        else:
            Fraud_check_result = 'Fraud Check is not Ready for testing'
        print(Fraud_check_result)
        #result_list.result_list.append(Fraud_check_result)
     except Exception as e:
        print(f"An error occurred: {e}")
     return  Fraud_check_result














