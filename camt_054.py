import re
import traceback

import Elements,import_packages,time

def camt_054():
    try :
        time.sleep(10)
        camt_054_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.fraud_Check.search_element)
        import_packages.driver_details.actions.move_to_element(camt_054_element).perform()
        #actions.move_to_element(camt_054_element).click().perform()
        camt_054_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.camt_054.message_element)
        camt_054_element.click()
        time.sleep(10)
        pop_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.camt_054.pop_up_element)
        if pop_element.is_displayed():
           pop_element.click()
           camt_054_element= import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.camt_054.message_search_element)
           #camt_054_element.click()
           time.sleep(5)
           camt_054_element.send_keys('*EWL2GESCHDB*')
           time.sleep(10)
           camt_054_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.camt_054.camt_054_search_element)
           camt_054_element.click()
           time.sleep(10)
           print('1 try')
           camt_054_record_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.camt_054.camt_054_record_element)
           camt_054_record_element = camt_054_record_element.text
           print(camt_054_record_element)
           camt_054_record = re.findall(r'\d+', camt_054_record_element)
           print(camt_054_record)
           camt_054_record = [int(n) for n in camt_054_record]
           print(camt_054_record)

           if camt_054_record[0] > 0:
               camt_054_load_result = 'Ready for testing'
               print(camt_054_load_result)
           else :
               camt_054_load_result = 'No camt records loaded'
               print(camt_054_load_result)

        else:
              camt_054_element= import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.camt_054.message_search_element)
              #camt_054_element.click()
              camt_054_element.send_keys('*EWL2GESCHDB*')
              time.sleep(10)
              camt_054_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.camt_054.camt_054_search_element)
              camt_054_element.click()
              print('else statement camt')
              time.sleep(10)
              print('2 try')
              camt_054_record_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                                           Elements.camt_054.camt_054_record_element)
              camt_054_record_element = camt_054_record_element.text
              print(camt_054_record_element)
              camt_054_record_element = re.findall(r'\d+', camt_054_record_element)
              camt_054_record_element = [int(n) for n in camt_054_record_element]
              print(camt_054_record_element)

              if camt_054_record_element[0] > 0:
                  camt_054_load_result = 'Ready for testing'
                  print(camt_054_load_result)
              else:
                  camt_054_load_result = 'No camt records loaded'
                  print(camt_054_load_result)
    except 'Unable to locate element':
        camt_054_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                              Elements.camt_054.message_search_element)
        # camt_054_element.click()
        camt_054_element.send_keys('*EWL2GESCHDB*')
        time.sleep(10)
        camt_054_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                              Elements.camt_054.camt_054_search_element)
        camt_054_element.click()
        print('exception statement camt')
        time.sleep(10)


        camt_054_record_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,
                                                                                     Elements.camt_054.camt_054_record_element)
        camt_054_record_element = camt_054_record_element.text
        print(camt_054_record_element)
        print('3 try')
        camt_054_record_element = re.findall(r'\d+', camt_054_record_element)
        camt_054_record_element = [int(n) for n in camt_054_record_element]
        print(camt_054_record_element)

        if camt_054_record_element[0] > 0:
            camt_054_load_result = 'Ready for testing'
            print(camt_054_load_result)
        else:
            camt_54_load_result = 'No camt records loaded'
            print(camt_054_load_result)

    except Exception as e:
        traceback.print_exc()
        print(f"An error occured : {e}")

    return camt_054_load_result
