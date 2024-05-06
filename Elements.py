

class login_webelements:

    app_url = 'https://cfat.p20.internal.zone/BILGUI/loginForm?tenantID=1900&isFromLogin=true'
    advanced_element = 'html/body/div/div[2]/button[3]'
    proceed_link = 'proceed-link'
    validation_url ='https://cfat.p20.internal.zone/BILGUI/loginForm?tenantID=1900&isFromLogin=true'
    username_element = 'username'
    password_element = '/html/body/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div[3]/div[1]/form/div[2]/div/div[1]'
    login_element ='/html/body/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div[3]/div[1]/form/div[3]/div/div[2]/button'
    login_validation_element ='/html/body/div[3]/div[1]/nav/div[5]/div/div/div[1]/span[1]/span'

class fraud_Check:
    search_element = '/html/body/div[3]/div[1]/nav/div[2]/div/div/span[2]/navigation-section/div/div[1]/span'
    fraud_element ='/html/body/div[3]/div[1]/nav/div[2]/div/div/span[2]/navigation-section/div/div[1]/span/navigation-item/div/div[1]/ul/div[2]/div[2]/li/span[2]'
    fraud_search_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/form/div/div/div[1]/ng-include/div[2]/div[2]/ng-include/div/div/button[3]/span'
    fraud_check_validation_element ='/html/body/div[3]/div[1]/nav/div[5]/div/div/div[1]/span[3]/span'




class embargo_check():
    search_element = '/html/body/div[3]/div[1]/nav/div[2]/div/div/span[2]/navigation-section/div/div[1]/span'
    embargo_element = '/html/body/div[3]/div[1]/nav/div[2]/div/div/span[2]/navigation-section/div/div[1]/span/navigation-item/div/div[1]/ul/div[1]/div[2]/li/span[2]'
    pop_up_element = '/html/body/div[3]/div[1]/nav/div[4]/alert-message[2]/div/div/div[3]/i'
    embargo_search_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/form/div/div/div[1]/ng-include/div[2]/div[2]/ng-include/div/div/button[3]/span'
    embargo_load_number_element='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/div[3]/div[1]/results-found/div/span[1]/span[1]'
    embargo_record_number_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/div[3]/div[1]/results-found/div/span[1]'
    embargo_load_date_element='lastUpdate'


class camt_054():
    message_element ='/html/body/div[3]/div[1]/nav/div[2]/div/div/span[2]/navigation-section/div/div[1]/span/navigation-item/div/div[1]/ul/div[1]/div[1]/li/span[2]'
    message_search_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/form/div/div/div[2]/accordion/div/div[1]/div[1]/div[2]/div/div/ng-include/div/div[4]/div[2]/input'
    camt_054_search_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/form/div/div/div[1]/ng-include/div[2]/div[2]/ng-include/div/div/button[3]'
    pop_up_element = '/html/body/div[3]/div[1]/nav/div[4]/alert-message/div/div/div[3]/i'
    selector_element ='#main-container > div.width-align.ng-scope > div > div > div > div.margin-overview.ng-scope > div > div:nth-child(5) > div'
    camt_054_record_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/div[3]/div[2]/results-found/div/span[1]'
    attribute_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/div[3]/div[2]/results-found/div/span[1]/span[1]'
    cl_ref_num_element ='clearingReferenceNumber'



class Transaction():
    transaction_search_element ='<a id="test1" translate="MENU_LBL_SRCH" style="color: rgb(255, 255, 255); font-size: 13px;" class="ng-scope">Search</a>'
    Transaction_element ='/html/body/div[3]/div[1]/nav/div[2]/div/div/span[2]/navigation-section/div/div[1]/span/navigation-item/div/div[1]/ul/div[3]/div[1]/li/span[2]'
    transaction_search_button_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/form/div/div/div[1]/ng-include/div[2]/div[2]/ng-include/div/div/button[3]'
    Advanced_scroll_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/form/div/div/div[2]/accordion/div/div[1]/div[3]/div[1]/h4/div/span/div[1]'
    cl_ref_num_element = 'clearingReferenceNumber'
    cl_ref_search_element='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/form/div/div/div[2]/accordion/div/div[2]/ng-include/div/div/button[3]/span'
    #attribute_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/div[3]/div[2]/results-found/div/span[1]'
    attribute_element= '/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/div[3]/div[2]/results-found/div/span[1]'
    transaction_first_record_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/div[5]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div'


class liquid_management():
    liquid_management = '/html/body/div[3]/div[1]/nav/div[2]/div/div/span[2]/navigation-section/div/div[1]/span/navigation-item/div/div[1]/ul/div[11]/div[2]/li/span[2]'

class dashboard_webelements:
    dashboard_home_element ='/html/body/div[3]/div[1]/nav/div[2]/div/div/span[1]/a'
    FDN_dashboard_element ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/widget-generator/div/ul/li[4]/widget-body/div/div/div[1]/div[1]/span'
    FDN_Dashboard_element_button ='/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/div/widget-generator/div/ul/li[4]/widget-body/div/div/div[2]/business-indicator-generator/div/div[1]/div[1]'