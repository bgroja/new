import re
import time


import import_packages,Elements

def transaction():
    time.sleep(10)
    transaction_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.fraud_Check.search_element)
    transaction_element.click()
    transaction_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.Transaction.Transaction_element)
    transaction_element.click()
    time.sleep(8)
    transaction_search_button = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                                   Elements.Transaction.transaction_search_button_element)
    transaction_search_button.click()
    time.sleep(8)
    attribute_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.Transaction.attribute_element)
    attribute_data= attribute_element.text
    print(attribute_data)
    records = re.findall(r'\d+' , attribute_data)
    print(records)
    records_number = [int(n) for n in records]
    print(records_number)
    if records_number[0] > 0:
        transaction_view_status = 'Records loaded'
        print(transaction_view_status)
    else:
        transaction_view_status = ' No Records Loaded'
        print(transaction_view_status)
    return  transaction_view_status




