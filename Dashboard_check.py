import time

import Elements
import import_packages
#import org.openqa.selenium.WebElement

def Dashboard_check_fun():
    time.sleep(10)
    dashboard_home_button = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.dashboard_webelements.dashboard_home_element)
    dashboard_home_button.click()
    time.sleep(5)
    #dashboard_FDN_button = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.dashboard_webelements.FDN_dashboard_element)
    #if dashboard_FDN_button.is_displayed():
    dashboard_FDN_button= import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.dashboard_webelements.FDN_dashboard_element)
    actions= import_packages.ActionChains(import_packages.driver_details.driver)
    actions.move_to_element(dashboard_FDN_button).perform()
    time.sleep(4)

    dashboard_FDN_button_element = import_packages.driver_details.driver.find_element(import_packages.By.XPATH,Elements.dashboard_webelements.FDN_Dashboard_element_button)
    if dashboard_FDN_button_element.is_displayed():

    #if(dashboard_FDN_button.isDisplayed()):
      dashboard_view = "Ready for testing"
    else:
      dashboard_view = 'Not ready for testing'
    return dashboard_view




