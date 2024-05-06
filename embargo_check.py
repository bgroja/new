import datetime
import re
import time
import traceback

import Elements
import import_packages
from selenium.common.exceptions import NoSuchElementException


def embargo_check():
    Embargo_check = ''
    try:
        time.sleep(10)
        search_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                            Elements.fraud_Check.search_element)
        search_element.click()
        embargo_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                             Elements.embargo_check.embargo_element)
        embargo_element.click()
        print('embargo search element')
        time.sleep(10)
        pop_up_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                            Elements.embargo_check.pop_up_element)


        if pop_up_element.is_displayed():
            pop_up_element.click()
            embargo_search_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                                        Elements.embargo_check.embargo_search_element)
            embargo_search_element.click()
            print("Embargo button worked")
            time.sleep(10)
            embargo_load_search_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.embargo_check.embargo_record_number_element)
            embargo_text_element = embargo_load_search_element.text
            print(embargo_text_element)
            embargo_text_element = re.findall(r'\d+',embargo_text_element)
            embargo_text_element = [int(n) for n in embargo_text_element]
            print(embargo_text_element)

            if embargo_text_element[0] >0:
                Embargo_check = 'Embargo test passed'
            else :
                Embargo_check = 'Embargo test failed'
            print('test display')
            time.sleep(10)

    except NoSuchElementException:
        embargo_search_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                                    Elements.embargo_check.embargo_search_element)
        embargo_search_element.click()
        print("Embargo button worked")
        time.sleep(10)
        embargo_load_search_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                                         Elements.embargo_check.embargo_record_number_element)
        embargo_text_element = embargo_load_search_element.text
        print(embargo_text_element)
        embargo_text_element = re.findall(r'\d+', embargo_text_element)
        embargo_text_element = [int(n) for n in embargo_text_element]
        print(embargo_text_element)

        if embargo_text_element[0] > 0:
            Embargo_check = 'Embargo test passed'
        else:
            Embargo_check = 'Embargo test failed'
        print('test display')
        time.sleep(10)
    except Exception as e:
        traceback.print_exc()
        print(f"An error occurred: {e}")

    return Embargo_check