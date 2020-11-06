import time
import allure
from Vopay_pages import iframe
from Vopay_pages.Flinkspages import Flinkspages
from Vopay_pages.VisaPage import VisaPage
from Vopay_pages.iframe import Iframe
from resources.variables import *
from selenium import webdriver


"""Vopay Iframe"""

"""Outer Html page"""

@allure.suite('Vopay Iframe')
@allure.title('Launch vopay iframe outer page(Vopay Outer)')
def test_cases_VopayOuter(browser):
    global launch
    launch= Iframe(browser)
    launch.browser_load()
    launch.switchtoiframe()

# @allure.suite('Vopay Iframe')
# @allure.title('To loadmore banks and get counts of all bank(Vopay Outer)')
# def test_countbank_VopayOuter(browser):
#     assert launch.verify_loadMore()==False,"Proceed not displayed"
#     launch.showall_banklist()


@allure.suite('Vopay Iframe')
@allure.title('User is able to search and select bank(Vopay Outer)')
def test_selectbank_VopayOuter(browser):
    global launch1
    launch1 = Flinkspages(browser)
    launch.searchBank(bankName)
    assert launch1.selectBankClick()==True,"bank not displayed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to click manual bank link and redirect properly(Vopay Outer)')
# def test_verify_manualBanklink_VopayOuter(browser):
#     assert launch.verify_manualBank()==True,"manual link not displayed"
#     assert launch.verify_manualmsg()=='Add your Bank Information', "not matched"
#     launch.Accept_manualterms()
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to click online bank link and select Terms of use checkbox(Vopay Outer)')
# def test_verify_onlinBanklink_VopayOuter(browser):
#     assert launch.redirect_onlinebank()=='Connect my Bank Online', "not matched"
#     launch.AcceptVopayTerms()
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to click change my bank link and redirect properly to search Bank page (Vopay Outer)')
# def test_Clickchangebanklink_VopayOuter(browser):
#     assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#     launch.verify_changemybank()
#     assert launch1.selectBankClick()== True, "tanger not displayed"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Click changemybank link in account page and To accept Vopay Terms in online credentail page (Vopay Outer)')
# def test_acceptterms_VopayOuter(browser):
#     launch.changebank_differpage()
#     assert launch.selectbankmethod_online()== True, "selected bank not changed"
#     launch.AcceptVopayTerms()
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify link(terms of use) is opened and Enabled "Proceed" button if all required fields are informed (Vopay Outer)')
# def test_VopayTerms_VopayOuter(browser):
#     assert launch.click_VopayTermslink()=='Terms of use',"Vopay terms not opened"
#     assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#     launch.verifyvalidusername_vopay(validuser)
#     assert launch.LoginTransit(pwd)==True,"Proceed button enabled"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User ability to change any bank i.e(flink bank) and verify invalid combination of user and password(Vopay Outer)')
# def test_validuser_invalidpass_VopayOuter(browser):
#     launch.verify_changemybank()
#     assert launch.search_flinknamedBank_vopay(flinkName)==True,"Flink Bank not display"
#     assert launch.selectbankmethod_online()== True, "selected bank not changed"
#     launch.AcceptVopayTerms()
#     launch.verifyinvalidusername_vopay(invalidUser)
#     launch.verifyinvalidPass_vopay(invalidPass)
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Click login button with invalid credentail and received message incorrect credentails(Vopay Outer)')
# def test_incorrectcredentail_vopayOuter(browser):
#     launch.Login_procced()
#     assert launch.retrylogin_incorrect()=='Credentials incorrect', "credentails correct"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify valid user and password and login succesfully(Vopay Outer)')
# def test_validuser_validpass_vopayOuter(browser):
#     launch.verifyvalidusername_vopay(validuser)
#     launch.verifyvalidpass_vopay(validpass)
#     launch.Login_procced()
#
# @allure.suite('Vopay Iframe')
# @allure.title('Enter invalid security question and redirected retry ques page(Vopay Outer)')
# def test_invalidsecurity_vopay(browser):
#     assert launch.invalid_insecurity()==True,"security question correct"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Enter valid security question and redirect successful and select cheque to enabled continue button(Vopay Outer)')
# def test_validsecurity_continue(browser):
#     assert launch.Verifysecurity_answer()==True,"wrong security result"
#     assert launch.selectcheque_continue()==True,"continue button not enabled"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify Token in Vopay Outer Frame with that bank in the list(Vopay Outer)')
# def test_Verify_Outertokenlistbank_Vopay(browser):
#     assert launch.verify_outertoken_vopay()==True,"Outerframe Token not displayed"
#
#     #
#     # @allure.title('After cheque selected ,successsfully transaction msg displayed (Outer Vopay)')
#     # def test_succesfullymsg_display_VopayOuter(browser):
#     #     assert launch.successfullytransactionmsg() == 'Server successful', "bank in the list"
#
#     #
#     # @allure.title('Click on select other bank (Outer Vopay)')
#     # def test_SelectothetBank_OuterVopay(browser):
#     #     assert launch.click_selectotherbank() == True, "select otherbank button not displayed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User back to home page and enter bank manually and verify cross button enabled(Vopay Outer)')
# def test_crossmanually_bankname_VopayOuter(browser):
#     launch.loadurlouter()
#     launch.switchtoiframe()
#     assert launch.enterbank_cancel()==True,"cross icon no displayed"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to enter manually his bank if it is not in the bank list and fill bank info details(Vopay Outer)')
# def test_Entermanually_Bankinfodetails_VopayOuter(browser):
#     assert launch.enterbannotlist()=='Don’t see your bank?',"Bank shown in the list"
#     launch.enterinstitution(institution)
#     launch.enterTransit(Transitno)
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Check validation of accountno that must contains maximum 7 digit or more(Vopay Outer)')
# def test_validateAccountno_VopayOuter(browser):
#     assert launch.enterAccountno(Accountno)=='Add your Bank Information',"Bank shown in the list"
#     launch.verifyproceedclick()
#     assert launch.validationAccountmsg()=='This value is too short. It should have 7 characters or more.',"Account take less than 7 digit"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User can only access the "Proceed" button if all required fields are informed (Vopay Outer)')
# def test_Enter_Bankinfodetails_VopayOuter(browser):
#     assert launch.verifyproceed_enabled()==True,"proceed button disabled"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to change the account type from business to Personal and vice-versa (Vopay Outer)')
# def test_switchAccount_VopayOuter(browser):
#     launch.clickpesonalAccount()
#     assert launch.switchAccounttype()=='Change to Business Account',"Not able to switch Business Account"
#     assert launch.switchAccountpersonal()=='Change to Personal Account',"Not able to switch personal"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Enter Personal account details and verify without entering optional value Proceed button enabled (Vopay Outer)')
# def test_EnterPersonaldetails_VopayOuter(browser):
#     launch.EnterPersonalFirst(firstname)
#     launch.EnterPersonalLast(Lastname)
#     assert launch.Enabled_PersonalProceedbtn()==True,"proceed button disabled"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Validate Email address of Personal Account (Vopay Outer)')
# def test_ValidateEmail_VopayOuter(browser):
#     launch.EnterPersonalEmail(Email)
#     assert launch.ValidateEmail()=='This value should be a valid email.'
#
# @allure.suite('Vopay Iframe')
# @allure.title('Validate Phone no of Personal Account neither less than 9 nor more than 10 digit(Vopay Outer)')
# def test_ValidatePhone_VopayOuter(browser):
#     launch.EnterPersonalPhone(Phone)
#     assert launch.ValidatePhone()=='This value should be a valid phone number',"less than 9 digit phone no working"
#     assert launch.ValidatePhone1()==False,"validation working wrong"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to add address details and Check the provinces that are available(Vopay Outer)')
# def test_AddAddress_VopayOuter(browser):
#     assert launch.EnterAddresss(address)=='Add my Address',"add address button not shown"
#     assert launch.CheckProvinceAvaiable()==True,'Province list shown'
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to edit address details and Click "Cancel/Remove" link is working (all the fields related to address are removed) (Vopay Outer)')
# def test_EditAdddress_Cancelremove_VopayOuter(browser):
#     launch.adddressbtn_Editadddress()
#     launch.CheckProvinceAvaiable()
#     assert launch.ClickCancelRemove()=='Add my Address',"address details not removed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to enter business details and verify with entering required value Proceed button enabled(Vopay Outer)')
# def test_EnterBusinessAccount_VopayOuter(browser):
#     launch.switchAccounttype()
#     launch.EnterCompany(CompName)
#     launch.BusinessFirst(busfirst,buslast)
#     assert launch.ClickProcedBusiness()==True,"proceed btn disabled with all required field informed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify Token in Vopay Outer Frame witn that bank which is not in list(Vopay Outer)')
# def test_Verify_OuterFrametoken_Vopay(browser):
#     assert launch.verify_outertoken_vopay()==True,"Outerframe Token not displayed"


"""Inner Iframe(Vopay)"""

@allure.suite('Vopay Iframe')
@allure.title('User is able to open new tab in the same browser and load(INNER Vopay)')
def test_newtab_VopayInner(browser):
    assert launch.switchwindow()=='https://vopay-testing.com/iframe/new/inner.html',"New tab not opened with inner url"
    launch.switchtoInnerIframe()
#
# @allure.suite('Vopay Iframe')
# @allure.title('To loadmore banks and get counts of all bank(INNER Vopay)')
# def test_countbank_VopayInner(browser):
#     assert launch.verify_loadMore()==False,"Proceed not displayed"
#     launch.showall_banklist()

# @allure.suite('Vopay Iframe')
# @allure.title('User is able to searchbank and select bank(INNER Vopay)')
# def test_selectbank_VopayInner(browser):
#     global launch1
#     launch1 = Flinkspages(browser)
#     launch.searchBank(bankName)
#     assert launch1.selectBankClick() == True, "bank not displayed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to click manual bank link and redirect properly(INNER Vopay)')
# def test_verify_manualBanklink_VopayInner(browser):
#     assert launch.verify_manualBank() == True, "manual link not displayed"
#     assert launch.verify_manualmsg() == 'Add your Bank Information', "not matched"
#     launch.Accept_manualterms()
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to click online bank link and select checkbox(INNER Vopay)')
# def test_verify_onlinBanklink_VopayInner(browser):
#     assert launch.redirect_onlinebank() == 'Connect my Bank Online', "not matched"
#     launch.AcceptVopayTerms()
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to click change my bank link and redirect properly to search Bank page(INNER Vopay)')
# def test_Clickchangebanklink_VopayInner(browser):
#     assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#     launch.verify_changemybank()
#     assert launch1.selectBankClick() == True, "tanger not displayed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Click change my bank in account page and To accept Vopay Terms in credentail page(INNER Vopay)')
# def test_acceptterms_VopayInner(browser):
#     launch.changebank_differpage()
#     assert launch.selectbankmethod_online() == True, "selected bank not changed"
#     launch.AcceptVopayTerms()
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify link(terms of use) is opened and User can only access the "Proceed" button if all required fields are informed(INNER Vopay)')
# def test_VopayTerms_VopayInner(browser):
#     assert launch.click_VopayTermslink() == 'Terms of use', "Vopay terms not opened"
#     assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#     launch.verifyvalidusername_vopay(validuser)
#     assert launch.LoginTransit(pwd) == True, "Proceed button enabled"
# #
# @allure.suite('Vopay Iframe')
# @allure.title('User ability to change any bank i.e(flink bank) and verify invalid combination of user and password(INNER Vopay)')
# def test_validuser_invalidpass_VopayInner(browser):
#     launch.verify_changemybank()
#     assert launch.search_flinknamedBank_vopay(flinkName)==True,"Flink Bank not display"
#     assert launch.selectbankmethod_online()== True, "selected bank not changed"
#     launch.AcceptVopayTerms()
#     launch.verifyinvalidusername_vopay(invalidUser)
#     launch.verifyinvalidPass_vopay(invalidPass)
#
# @allure.suite('Vopay Iframe')
# @allure.title('Click login button with invalid credentail and received message incorrect credentails(INNER Vopay)')
# def test_incorrectcredentail_VopayInner(browser):
#     launch.Login_procced()
#     assert launch.retrylogin_incorrect()=='Credentials incorrect', "credentails correct"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify valid credentail and login succesfully (INNER Vopay)')
# def test_validuser_validpass_VopayInner(browser):
#     launch.verifyvalidusername_vopay(validuser)
#     launch.verifyinvalidPass_vopay(validpass)
#     launch.Login_procced()
#
# @allure.suite('Vopay Iframe')
# @allure.title('Enter invalid security question and redirected retry ques page (INNER Vopay)')
# def test_invalidsecurity_VopayInner(browser):
#     assert launch.invalid_insecurity()==True,"security question correct"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Enter valid security question and redirect successful and select cheque to enabled continue button(INNER Vopay)')
# def test_validsecurity_continue_VopayInner(browser):
#     assert launch.Verifysecurity_answer()==True,"wrong security result"
#     assert launch.selectcheque_continue()==True,"continue button not enabled"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify Token in Vopay Inner Frame with that bank in the list(INNER Vopay)')
# def test_Verify_Innertokenlistbank_Vopay(browser):
#     launch.switchtoInnerIframe()
#     assert launch.verify_Innertoken() == True, "Innerframe Token not displayed"
#
#     #
#     # @allure.title('Click on select other bank (Inner Vopay)')
#     # def test_SelectothetBank_InnerVopay(browser):
#     #     assert launch.click_selectotherbank() == True, "select otherbank button not displayed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User back to home page and enter bank manually and verify cross button enabled(Vopay Inner)')
# def test_crossmanually_bankname_VopayInner(browser):
#     launch.loadurlinner()
#     launch.switchtoInnerIframe()
#     assert launch.enterbank_cancel()==True,"cross icon no displayed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to enter manually his bank if it is not in the bank list and fill bank info details(Vopay Inner)')
# def test_Entermanually_Bankinfodetails_VopayInner(browser):
#     assert launch.enterbannotlist() == 'Don’t see your bank?', "Bank shown in the list"
#     launch.enterinstitution(institution)
#     launch.enterTransit(Transitno)
#
# @allure.suite('Vopay Iframe')
# @allure.title('Check validation of accountno that must contains maximum 7 digit or more(Vopay Inner)')
# def test_validateAccountno_VopayInner(browser):
#     assert launch.enterAccountno(Accountno) == 'Add your Bank Information', "Bank shown in the list"
#     launch.verifyproceedclick()
#     assert launch.validationAccountmsg() == 'This value is too short. It should have 7 characters or more.', "Account take less than 7 digit"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User can only access the "Proceed" button if all required fields are informed (Vopay Inner)')
# def test_Enter_Bankinfodetails_VopayInner(browser):
#     assert launch.verifyproceed_enabled() == True, "proceed button disabled"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to change the account type from business to Personal and vice-versa (Vopay Inner)')
# def test_switchAccount_VopayInner(browser):
#     launch.clickpesonalAccount()
#     assert launch.switchAccounttype() == 'Change to Business Account', "Not able to switch Business Account"
#     assert launch.switchAccountpersonal() == 'Change to Personal Account', "Not able to switch personal"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Enter Personal account details and verify without entering optional value Proceed button enabled (Vopay Inner)')
# def test_EnterPersonaldetails_VopayInner(browser):
#     launch.EnterPersonalFirst(firstname)
#     launch.EnterPersonalLast(Lastname)
#     assert launch.Enabled_PersonalProceedbtn() == True, "proceed button disabled"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Validate Email address of Personal Account (Vopay Inner)')
# def test_ValidateEmail_VopayInner(browser):
#     launch.EnterPersonalEmail(Email)
#     assert launch.ValidateEmail() == 'This value should be a valid email.'
#
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Validate Phone no of Personal Account neither less than 9 nor more than 10 digit(Vopay Inner)')
# def test_ValidatePhone_VopayInner(browser):
#     launch.EnterPersonalPhone(Phone)
#     assert launch.ValidatePhone() == 'This value should be a valid phone number', "less than 9 digit phone no working"
#     assert launch.ValidatePhone1() == False, "validation working wrong"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to add address details and Check the provinces that are available(Vopay Inner)')
# def test_AddAddress_VopayInner(browser):
#     assert launch.EnterAddresss(address) == 'Add my Address', "add address button not shown"
#     assert launch.CheckProvinceAvaiable() == True, 'Province list shown'
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to edit address details and Click "Cancel/Remove" link is working (all the fields related to address are removed (Vopay Inner)')
# def test_EditAdddress_Cancelremove_VopayInner(browser):
#     launch.adddressbtn_Editadddress()
#     launch.CheckProvinceAvaiable()
#     assert launch.ClickCancelRemove() == 'Add my Address', "address details not removed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to enter business details and verify with entering required value Proceed button enabled(Vopay Inner)')
# def test_EnterBusinessAccount_VopayInner(browser):
#     launch.switchAccounttype()
#     launch.EnterCompany(CompName)
#     launch.BusinessFirst(busfirst, buslast)
#     assert launch.ClickProcedBusiness() == True, "proceed btn disabled with all required field informed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify Token in Vopay Inner Frame(Vopay Inner)')
# def test_Verify_InnerFrametoken_VopayInner(browser):
#     launch.switchtoInnerIframe()
#     assert launch.verify_Innertokenagain() == True, "Innerframe Token not displayed"

"""JS Iframe(Vopay)"""

@allure.suite('Vopay Iframe')
@allure.title('User is able to open new tab3 in the same browser and load JS url')
def test_newtab_VopayJS_sameoperation(browser):
    assert launch.switchagain_jsbrowser()=='https://vopay-testing.com/iframe/new/js.html',"wrong url"
    launch.switchtoiframe()

# @allure.suite('Vopay Iframe')
# @allure.title('To loadmore banks and get counts of all bank(JS Vopay)')
# def test_countbank_VopayJS(browser):
#     assert launch.verify_loadMore()==False,"Proceed not displayed"
#     launch.showall_banklist()
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to searchbank and select bank(JS Vopay)')
# def test_selectbank_VopayJS(browser):
#     global launch1
#     launch1 = Flinkspages(browser)
#     launch.searchBank(bankName)
#     assert launch1.selectBankClick() == True, "bank not displayed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to click manual bank link and redirect properly(JS Vopay)')
# def test_verify_manualBanklink_VopayJS(browser):
#     assert launch.verify_manualBank() == True, "manual link not displayed"
#     assert launch.verify_manualmsg() == 'Add your Bank Information', "not matched"
#     launch.Accept_manualterms()
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to click online bank link and select checkbox(JS Vopay)')
# def test_verify_onlinBanklink_VopayJS(browser):
#     assert launch.redirect_onlinebank() == 'Connect my Bank Online', "not matched"
#     launch.AcceptVopayTerms()
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to click change my bank link and redirect properly to search Bank page(JS Vopay)')
# def test_Clickchangebanklink_VopayJS(browser):
#     assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#     launch.verify_changemybank()
#     assert launch1.selectBankClick() == True, "tanger not displayed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Click change my bank in secure accountpage and To accept Vopay Terms in credentail page(JS Vopay)')
# def test_acceptterms_VopayJS(browser):
#     launch.changebank_differpage()
#     assert launch.selectbankmethod_online() == True, "selected bank not changed"
#     launch.AcceptVopayTerms()
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify link(terms of use) is opened and User can only access the "Proceed" button if all required fields are informed(JS Vopay)')
# def test_VopayTerms_VopayJS(browser):
#     assert launch.click_VopayTermslink() == 'Terms of use', "Vopay terms not opened"
#     assert launch.verify_msg() == 'Enter Your Credentials', "online bank credential tab not displayed"
#     launch.verifyvalidusername_vopay(validuser)
#     assert launch.LoginTransit(pwd) == True, "Proceed button enabled"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User ability to change any bank i.e(flink bank) and verify invalid combination of user and password(JS Vopay)')
# def test_validuser_invalidpass_VopayJS(browser):
#     launch.verify_changemybank()
#     assert launch.search_flinknamedBank_vopay(flinkName)==True,"Flink Bank not display"
#     assert launch.selectbankmethod_online()== True, "selected bank not changed"
#     launch.AcceptVopayTerms()
#     launch.verifyinvalidusername_vopay(invalidUser)
#     launch.verifyinvalidPass_vopay(invalidPass)
#
# @allure.suite('Vopay Iframe')
# @allure.title('Click login button with invalid credentail and received message incorrect credentails(JS Vopay)')
# def test_incorrectcredentail_VopayJS(browser):
#     launch.Login_procced()
#     assert launch.retrylogin_incorrect()=='Credentials incorrect', "credentails correct"
#
# @allure.suite('Vopay Iframe')
# @allure.title('verify valid user and password and login succesfully(JS Vopay)')
# def test_validuser_validpass_VopayJS(browser):
#     launch.verifyvalidusername_vopay(validuser)
#     launch.verifyinvalidPass_vopay(validpass)
#     launch.Login_procced()
#
# @allure.suite('Vopay Iframe')
# @allure.title('Enter invalid security question and redirected retry ques page(JS Vopay)')
# def test_invalidsecurity_vopay_VopayJS(browser):
#     assert launch.invalid_insecurity()==True,"security question correct"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Enter valid security question and redirect successful and select cheque to enabled continue button(JS Vopay)')
# def test_validsecurity_continue_VopayJS(browser):
#     assert launch.Verifysecurity_answer()==True,"wrong security result"
#     assert launch.selectcheque_continue()==True,"continue button not enabled"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify Token in Vopay JS Frame with that bank in the list(JS Vopay)')
# def test_JStokenlistbank_VopayJS(browser):
#     assert launch.verify_JStoken_vopayurl() == True, "JSframe Token not displayed"
#     assert launch.JS_Bankvopayurl() == True, "bank not printed"
#     assert launch.JS_AccountName_Vopayurl() == True, "Account Name not printed"
#     assert launch.JS_institution_vopayurl() == True, "institution not printed"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User back to home page and enter bank manually and verify cross button enabled(Vopay JS)')
# def test_crossmanually_bankname_VopayJS(browser):
#     launch.loadurljs()
#     launch.switchwindow_JS()
#     assert launch.enterbank_cancel()==True,"cross icon no displayed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to enter manually his bank if it is not in the bank list and fill bank info details(Vopay JS)')
# def test_Entermanually_Bankinfodetails_VopayJS(browser):
#     assert launch.enterbannotlist() == 'Don’t see your bank?', "Bank shown in the list"
#     launch.enterinstitution(institution)
#     launch.enterTransit(Transitno)
#
# @allure.suite('Vopay Iframe')
# @allure.title('Check validation of accountno that must contains maximum 7 digit or more(Vopay JS)')
# def test_validateAccountno_VopayJS(browser):
#     assert launch.enterAccountno(Accountno) == 'Add your Bank Information', "Bank shown in the list"
#     launch.verifyproceedclick()
#     assert launch.validationAccountmsg() == 'This value is too short. It should have 7 characters or more.', "Account take less than 7 digit"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User can only access the "Proceed" button if all required fields are informed (Vopay JS)')
# def test_Enter_Bankinfodetails_VopayJS(browser):
#     assert launch.verifyproceed_enabled() == True, "proceed button disabled"
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to change the account type from business to Personal and vice-versa (Vopay JS)')
# def test_switchAccount_VopayJS(browser):
#     launch.clickpesonalAccount()
#     assert launch.switchAccounttype() == 'Change to Business Account', "Not able to switch Business Account"
#     assert launch.switchAccountpersonal() == 'Change to Personal Account', "Not able to switch personal"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Enter Personal account details and verify without entering optional value Proceed button enabled (Vopay JS)')
# def test_EnterPersonaldetails_VopayJS(browser):
#     launch.EnterPersonalFirst(firstname)
#     launch.EnterPersonalLast(Lastname)
#     assert launch.Enabled_PersonalProceedbtn() == True, "proceed button disabled"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Validate Email address of Personal Account (Vopay JS)')
# def test_ValidateEmail_VopayJS(browser):
#     launch.EnterPersonalEmail(Email)
#     assert launch.ValidateEmail() == 'This value should be a valid email.',"wrong validation"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('Validate Phone no of Personal Account neither less than 9 nor more more than 10 digit(Vopay JS)')
# def test_ValidatePhone_VopayJS(browser):
#     launch.EnterPersonalPhone(Phone)
#     assert launch.ValidatePhone() == 'This value should be a valid phone number', "less than 9 digit phone no working"
#     assert launch.ValidatePhone1() == False, "validation working wrong"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to add address details and Check the provinces that are available(Vopay JS)')
# def test_AddAddress_VopayJS(browser):
#     assert launch.EnterAddresss(address) == 'Add my Address', "add address button not shown"
#     assert launch.CheckProvinceAvaiable() == True, 'Province list shown'
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to edit address details and Click "Cancel/Remove" link is working (all the fields related to address are removed (Vopay JS)')
# def test_EditAdddress_Cancelremove_VopayJS(browser):
#     launch.adddressbtn_Editadddress()
#     launch.CheckProvinceAvaiable()
#     assert launch.ClickCancelRemove() == 'Add my Address', "address details not removed"
#
#
# @allure.suite('Vopay Iframe')
# @allure.title('User is able to enter business details and verify with entering required value Proceed button enabled(Vopay JS)')
# def test_EnterBusinessAccount_VopayJS(browser):
#     launch.switchAccounttype()
#     launch.EnterCompany(CompName)
#     launch.BusinessFirst(busfirst, buslast)
#     assert launch.ClickProcedBusiness() == True, "proceed btn disabled with all required field informed"
#
# @allure.suite('Vopay Iframe')
# @allure.title('Verify Token in Vopay JS Frame with that bank not in list(Vopay JS)')
# def test_Verify_JSFrametoken_VopayJS(browser):
#     assert launch.verify_JStoken_vopayurl() == True, "JSframe Token not displayed"
#     assert launch.JS_Bankvopayurl() == True, "bank not printed"
#     assert launch.JS_AccountName_Vopayurl() == True, "Account Name not printed"
#     assert launch.JS_institution_vopayurl() == True, "institution not printed"


"""Flinks Iframe"""
"""Outer url"""

@allure.suite('Flink Iframe')
@allure.title('To open newtab3 and Hide redLine in flinks outer url')
def test_FlinkOuterURL_newbrowser(browser):
    assert launch1.switchagain_oldouter()=='https://vopay-testing.com/iframe/old/outer.html', "URL not matched"
    # launch1.switchtoiframe()
    # assert launch1.VerifyonHide()==False,"Hide button not working"


@allure.suite('Flink Iframe')
@allure.title('Switch to iframe again and search Tan Bank(Outer Flinks)')
def test_searchbankFlinkURL_FlinkOuter(browser):
    launch1.refreshpage()
    launch1.switchtoiframe()
    assert launch1.switchtoiframe2()==True,"Hidebutton not display"
    assert launch1.searchBank1(TanName)==True,"Tan Bank not display"


@allure.suite('Flink Iframe')
@allure.title('Select bank and Navigated to agree and continue page(Outer Flinks)')
def test_selectbankFlinkURL_FlinkOuter(browser):
    assert launch1.selectTan_flink()=="Click 'AGREE and CONTINUE' to allow username test to proceed.","Agree and continue page not displayed"
    assert launch1.verifyAgreepage()=='Access your account number', "text not matched"


@allure.suite('Flink Iframe')
@allure.title('Verify text on agree page and Click on cancel button page redirected to HomePage(Outer Flinks)')
def test_verifyText_AgreeContinuePage_FlinkOuter(browser):
    time.sleep(2)
    assert launch1.verifyTextAgree()=='Access your account transaction history',"text not matched"
    assert launch1.verifyTextAgree2()=='Access your name, email, address and phone number',"text not matched"
    assert launch1.ClickCancelbutton()=='Connect with your bank',"page not redirected to homepage"

@allure.suite('Flink Iframe')
@allure.title('Click AgreeContinue button navigate to login page and click on back arrow on loginpage back to homepage(Outer Flinks)')
def test_RedirectLoginPage_FlinkOuter(browser):
    launch1.selectTan_flink()
    assert launch1.Click_agreeButton()==True,"Logo not displayed on Agreecontinue page "
    assert launch1.clickonBackarrow()=='Connect with your bank',"page not redirected to homepage"
    assert launch1.search_flinknamedBank(flinkName)==True,"Flink bank not display"

@allure.suite('Flink Iframe')
@allure.title('Validate username and password with invalid credentails(Outer Flinks)')
def test_Validate_UserandPass_invalid_FlinkOuter(browser):
    launch1.Click_agreeButton()
#     launch1.verifyinvalidusername(invalidUser)
#     launch1.verifyinvalidPass(invalidPass)
#     assert launch1.loginFlinks()==True,"submit button disabled"
#     assert launch1.Clickretrybutton()==True,"button not displayed"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('Validate username and password with more comination(Outer Flinks)')
# def test_Validate_UserandPass_FlinkOuter(browser):
#     launch1.verifyvalidusername(validuser)
#     launch1.verifyinvalidPass(invalidPass)
#     assert launch1.loginFlinks()==True,"submit button disabled"
#     assert launch1.Clickretrybutton()==True, "invalid login"
#     time.sleep(3)
#
# @allure.suite('Flink Iframe')
# @allure.title('Validate with invalid username and valid password(Outer Flinks)')
# def test_Validate_invalidUser_validPass_FlinkOuter(browser):
#     launch1.verifyinvalidusername(invalidUser)
#     launch1.verifyvalidpass(validpass)
#     assert launch1.loginFlinks()==True,"submit button disabled"
#     assert launch1.Clickretrybutton()==True, "invalid login"


@allure.suite('Flink Iframe')
@allure.title('Click on resetpass and Get url to redirected page(Outer Flinks)')
def test_ClickresetPass_FlinkOuter(browser):
    launch1.verifyvalidusername(validuser)
    launch1.verifyvalidpass(validpass)
    assert launch1.Clickresetpassword_button()=='https://flinks.io/',"navigate wrong url"

@allure.suite('Flink Iframe')
@allure.title('Login with valid credentail and Redirected succesfully to security pag(Outer Flinks)')
def test_VerifyAfterlogin_FlinkOuter(browser):
    launch1.switchtab()
    launch1.switchtoiframe()
    launch1.switchtoiframe2()
#     launch1.search_flinknamedBank(flinkName)
#     launch1.Click_agreeButton()
#     launch1.verifyvalidusername(validuser)
#     launch1.verifyvalidpass(validpass)
#     assert launch1.loginFlinks()==True,"submit button disabled"
#
# @allure.suite('Flink Iframe')
# @allure.title('User provide invalid security question(Outer Flinks)')
# def test_Verify_invalidsecurity_FlinkOuter(browser):
#     time.sleep(2)
#     assert launch1.verify_invalidsecurityans()==True,"answer correct"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('User provide valid security question and click continue to account select (Outer Flinks)')
# def test_validsecurityFlinkOuter(browser):
#     launch1.verify_security()
#     assert launch1.selectAccount()=='Please select an account',"invalid security"
#
# @allure.suite('Flink Iframe')
# @allure.title('To verify the outer redirect(Outer Flinks)')
# def test_verifyouterredirect_FlinkOuter(browser):
#     assert launch1.verify_outertoken() == True, "token not display"
#


"""Inner url (Flinks)"""

@allure.suite('Flink Iframe')
@allure.title('To open newtab5 and Hide redLine in flinks url(Inner Flinks)')
def test_Flinkinnerurl_newbrowser(browser):
    assert launch1.switchwindow_oldinner()=='https://vopay-testing.com/iframe/old/inner.html', "URL not matched"
    # launch1.switchtoiframe()
    # assert launch1.VerifyonHide()==False,"Hide button not working"

@allure.suite('Flink Iframe')
@allure.title('Switch to iframe again and Search Tan Bank(Inner Flinks)')
def test_searchbankFlinkURL_FlinkInner(browser):
    launch1.refreshpage()
    launch1.switchtoiframe()
    assert launch1.switchtoiframe2()==True,"Hidebutton not display"
    assert launch1.searchBank1(TanName)==True,"Tan Bank not display"


@allure.suite('Flink Iframe')
@allure.title('Select bank and Navigated agree and continue page(Inner Flinks)')
def test_selectbankFlinkURL_FlinkInner(browser):
    assert launch1.selectTan_flink() == "Click 'AGREE and CONTINUE' to allow username test to proceed.", "Agree and continue page not displayed"
    assert launch1.verifyAgreepage() == 'Access your account number', "text not matched"


@allure.suite('Flink Iframe')
@allure.title('Verify text on agree page and click on cancel button page redirected to HomePage(Inner Flinks)')
def test_verifyText_AgreeContinuePage_FlinkInner(browser):
    time.sleep(2)
    assert launch1.verifyTextAgree()=='Access your account transaction history',"text not matched"
    assert launch1.verifyTextAgree2()=='Access your name, email, address and phone number',"text not matched"
    assert launch1.ClickCancelbutton()=='Connect with your bank',"page not redirected to homepage"


@allure.suite('Flink Iframe')
@allure.title('Click AgreeContinue button navigate to login page and click on back arrow on loginpage back to homepage(Inner Flinks)')
def test_RedirectLoginPage_FlinkInner(browser):
    launch1.selectTan_flink()
    assert launch1.Click_agreeButton()==True,"Logo not displayed on Agreecontinue page "
    assert launch1.clickonBackarrow()=='Connect with your bank',"page not redirected to homepage"
    assert launch1.search_flinknamedBank(flinkName)==True,"Flink bank not display"


@allure.suite('Flink Iframe')
@allure.title('Validate username and password with invalid credentails(Inner Flinks)')
def test_Validate_UserandPass_invalid_FlinkInner(browser):
    launch1.Click_agreeButton()
    launch1.verifyinvalidusername(invalidUser)
    launch1.verifyinvalidPass(invalidPass)
    assert launch1.loginFlinks() == True, "submit button disabled"
    assert launch1.Clickretrybutton() == True, "button not displayed"

@allure.suite('Flink Iframe')
@allure.title('Validate username and password with more combination(Inner Flinks)')
def test_Validate_UserandPass_FlinkInner(browser):
    launch1.verifyvalidusername(validuser)
    launch1.verifyinvalidPass(invalidPass)
    assert launch1.loginFlinks()==True,"submit button disabled"
    assert launch1.Clickretrybutton()==True, "invalid login"
    time.sleep(3)

@allure.suite('Flink Iframe')
@allure.title('Validate with invalidusername and valid password(Inner Flinks)')
def test_Validate_invalidUser_validPass_FlinkInner(browser):
    launch1.verifyinvalidusername(invalidUser)
    launch1.verifyvalidpass(validpass)
    assert launch1.loginFlinks()==True,"submit button disabled"
    assert launch1.Clickretrybutton()==True, "invalid login"


@allure.suite('Flink Iframe')
@allure.title('Click on resetpass and Get url of redirected page(Inner Flinks)')
def test_ClickresetPass_FlinkInner(browser):
    launch1.verifyvalidusername(validuser)
    launch1.verifyvalidpass(validpass)
    assert launch1.Clickresetpassword_button_inner()=='https://flinks.io/',"navigate wrong url"


@allure.suite('Flink Iframe')
@allure.title('Login with valid credentail and Redirected succesfully to security page(Inner Flinks)')
def test_Afterlogin_verify_FlinkInner(browser):
    launch1.switchtabinner()
    launch1.switchtoiframe()
    launch1.switchtoiframe2()
    launch1.search_flinknamedBank(flinkName)
    launch1.Click_agreeButton()
    launch1.verifyvalidusername(validuser)
    launch1.verifyvalidpass(validpass)
    assert launch1.loginFlinks() == True, "submit button disabled"


@allure.suite('Flink Iframe')
@allure.title('User provide invalid security question(Inner Flinks)')
def test_Verify_invalidsecurity_FlinkInner(browser):
    time.sleep(2)
    assert launch1.verify_invalidsecurityans()==True,"answer correct"


@allure.suite('Flink Iframe')
@allure.title('User provide valid security question and click continue to account select(Inner Flinks)')
def test_validsecurity_FlinkInner(browser):
    launch1.verify_security()
    assert launch1.selectAccount() == 'Please select an account', "invalid security"


@allure.suite('Flink Iframe')
@allure.title('To verify the inner redirect(Flinks Inner)')
def test_verifyinnerredirect_FlinkInner(browser):
    time.sleep(3)
    launch1.switchtoiframesimulate()
    assert launch1.verify_innertoken()==True,"Token inner not verified"


@allure.suite('Flink Iframe')
@allure.title('Click on simulate login and verify the token(Flinks Inner) ')
def test_verifyToken_Onsimulateclick_inner(browser):
    assert launch1.Clicksimulatebutton_inner() == True, "Token page not reached"
    assert launch1.verify_token()==True,"Token inner not verified"

#
# """JS url (Flinks)"""
#
# @allure.suite('Flink Iframe')
# @allure.title('To open newtab6 and Hide redLine in flinks url(JS Flinks)')
# def test_FlinkJSurl_newbrowser(browser):
#     assert launch1.switchwindow_oldjs()=='https://vopay-testing.com/iframe/old/js.html', "URL not matched"
#     launch1.switchtoiframe()
#     assert launch1.VerifyonHide()==False,"Hide button not working"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('Switch to iframe again and search Tan bank(JS Flinks)')
# def test_searchbank_FlinkJS(browser):
#     launch1.refreshpage()
#     launch1.switchtoiframe()
#     assert launch1.switchtoiframe2()==True,"Hidebutton not display"
#     assert launch1.searchBank1(TanName)==True,"Tan Bank not display"
#
# @allure.suite('Flink Iframe')
# @allure.title('Select bank and Navigated to agree and continue page(JS Flinks)')
# def test_selectbank_FlinkJS(browser):
#     assert launch1.selectTan_flink() == "Click 'AGREE and CONTINUE' to allow username test to proceed.", "Agree and continue page not displayed"
#     assert launch1.verifyAgreepage() == 'Access your account number', "text not matched"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('Verify text on agree page and click on cancel button page redirected to HomePage(JS Flinks)')
# def test_verifyText_AgreeContinuePage_FlinkJS(browser):
#     time.sleep(2)
#     assert launch1.verifyTextAgree()=='Access your account transaction history',"text not matched"
#     assert launch1.verifyTextAgree2()=='Access your name, email, address and phone number',"text not matched"
#     assert launch1.ClickCancelbutton()=='Connect with your bank',"page not redirected to homepage"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('Click AgreeContinue button navigate to login page and click on back arrow on loginpage back to homepage(JS Flinks)')
# def test_RedirectLoginPage_FlinkJS(browser):
#     launch1.selectTan_flink()
#     assert launch1.Click_agreeButton()==True,"Logo not displayed on Agreecontinue page "
#     assert launch1.clickonBackarrow()=='Connect with your bank',"page not redirected to homepage"
#     assert launch1.search_flinknamedBank(flinkName)==True,"Flink bank not display"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('Validate username and password with invalid credentails(JS Flinks)')
# def test_Validate_UserandPass_invalid_FlinkJS(browser):
#     launch1.Click_agreeButton()
#     launch1.verifyinvalidusername(invalidUser)
#     launch1.verifyinvalidPass(invalidPass)
#     assert launch1.loginFlinks() == True, "submit button disabled"
#     assert launch1.Clickretrybutton() == True, "button not displayed"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('Validate username and password with more comination(JS Flinks)')
# def test_Validate_UserandPass_FlinkJS(browser):
#     launch1.verifyvalidusername(validuser)
#     launch1.verifyinvalidPass(invalidPass)
#     assert launch1.loginFlinks()==True,"submit button disabled"
#     assert launch1.Clickretrybutton()==True, "invalid login"
#     time.sleep(3)
#
# @allure.suite('Flink Iframe')
# @allure.title('Validate with invalid username and valid password(JS Flinks)')
# def test_Validate_invalidUser_validPass_FlinkJS(browser):
#     launch1.verifyinvalidusername(invalidUser)
#     launch1.verifyvalidpass(validpass)
#     assert launch1.loginFlinks()==True,"submit button disabled"
#     assert launch1.Clickretrybutton()==True, "invalid login"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('Click on resetpass and Get url to redirected page(JS Flinks)')
# def test_ClickresetPass_FlinkJS(browser):
#     launch1.verifyvalidusername(validuser)
#     launch1.verifyvalidpass(validpass)
#     assert launch1.Clickresetpassword_button_js()=='https://flinks.io/',"navigate wrong url"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('Login with valid credentail and Redirected succesfully to security pag(JS Flinks)')
# def test_Afterlogin_verify_FlinkJS(browser):
#     launch1.switchtabJS()
#     launch1.switchtoiframe()
#     launch1.switchtoiframe2()
#     launch1.search_flinknamedBank(flinkName)
#     launch1.Click_agreeButton()
#     launch1.verifyvalidusername(validuser)
#     launch1.verifyvalidpass(validpass)
#     assert launch1.loginFlinks() == True, "submit button disabled"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('User provide invalid security question(JS Flinks)')
# def test_Verify_invalidsecurity_FlinkJS(browser):
#     time.sleep(2)
#     assert launch1.verify_invalidsecurityans()==True,"answer correct"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('User provide valid security question and click continue to account select(JS Flinks)')
# def test_validsecurity_FlinkJS(browser):
#     launch1.verify_security()
#     assert launch1.selectAccount() == 'Please select an account', "invalid security"
#
# @allure.suite('Flink Iframe')
# @allure.title('To verify the JS token from redirected token page(JS Flinks)')
# def test_verifJSredirect_FlinkJS(browser):
#         time.sleep(3)
#         assert launch1.JS_tokenvalue() == True, "token not printed"
#         assert launch1.JS_Bankvalue() == True, "bank not printed"
#         assert launch1.JS_FullName() == True, "fullname not printed"
#         assert launch1.JS_MaskedAccount() == True, "Account not printed"
#
#
# @allure.suite('Flink Iframe')
# @allure.title('Click on simulate login and verify the token and Bank details(JS Flinks) ')
# def test_verifyToken_Onsimulateclick_FlinkJS(browser):
#         launch1.Clicksimulatebutton()
#         assert launch1.JS_tokenvalue() == True, "token not printed"
#         assert launch1.JS_Bankvalue() == True, "bank not printed"
#         assert launch1.JS_FullName() == True, "fullname not printed"
#         assert launch1.JS_MaskedAccount() == True, "Account not printed"
#
#     # import logging
#     # import sys
#     #
#     # @allure.suite('Flink Iframe')
#     # @allure.title('To verify the JS token redirected page(JS Flinks)')
#     # def test_verifJSredirect_FlinkJS(browser):
#     #     time.sleep(3)
#     #     var = launch1.switchtoiframesimulate_JS()
#     #     print(var)
#     #     logger = logging.getLogger()
#     #     logger.setLevel(logging.INFO)
#     #     logger.info(var)
#
# #
#
# """VISA Iframe"""
# """Visa Inner URL"""
#
# @allure.suite('Visa Iframe')
# @allure.title('To open newtab7 and launch visa inner url(Visa Inner)')
# def test_VisaInnerurl_newbrowser(browser):
#     global visa
#     visa = VisaPage(browser)
#     assert visa.switchwindow_VisaInner()=='http://vopay-testing.com/iframe/visa/inner.html', "URL not matched"
#     launch.switchtoiframe()
#
#
# @allure.suite('Visa Iframe')
# @allure.title('Click Submit button without entering required field(Visa Inner)')
# def test_ClickSubmit_withoutinput_VisaInner(browser):
#     visa.clickSubmitbtn()
#     assert visa.getcardholdertext()=='Cardholder Name', "redirect to next page"
#
# @allure.suite('Visa Iframe')
# @allure.title('Validate CardHoldername with invalid input(Visa Inner)')
# def test_verifyCardholder_Validation_VisaInner(browser):
#     visa.Invalid_Cardholdername()
#     visa.EnterCardNumber(cardno)
#     visa.clickSubmitbtn()
#     assert visa.invalidmsg_cardholder()=='Invalid Cardholder Name',"invalid cardholder name taken"
#
# @allure.suite('Visa Iframe')
# @allure.title('Validate Card Number with invalid input(Visa Inner)')
# def test_verifyCardNO_Validation_VisaInner(browser):
#     visa.validcardholdername(cardholder)
#     visa.InvalidCardNumber()
#     visa.clickSubmitbtn()
#     assert visa.invalidmsg_cardNo()=='Invalid Card Number',"invalid cardNumber taken"
#
# @allure.suite('Visa Iframe')
# @allure.title('Valid input Entered in required field and verify token and url(Visa Inner)')
# def test_verifyCardNO_Validation_VisaInner(browser):
#     visa.validcardholdername(cardholder)
#     visa.EnterCardNumber(cardno)
#     visa.clickSubmitbtn()
#     assert visa.verify_innerVisatoken()==True,"Url and token not verified"
#
# """Visa JS URL"""
#
# @allure.suite('Visa Iframe')
# @allure.title('To open newtab7 and launch visa js url(Visa JS)')
# def test_VisaJSurl_newbrowser(browser):
#     assert visa.switchwindow_VisaJS()=='http://vopay-testing.com/iframe/visa/js.html', "URL not matched"
#     launch.switchtoiframe()
#
# @allure.suite('Visa Iframe')
# @allure.title('Click Submit button without entering required field(Visa JS)')
# def test_ClickSubmit_withoutinput_VisaJS(browser):
#     visa.clickSubmitbtn()
#     assert visa.getcardholdertext()=='Cardholder Name', "redirect to next page"
#
# @allure.suite('Visa Iframe')
# @allure.title('Validate CardHoldername with invalid input(Visa JS)')
# def test_verifyCardholder_Validation_VisaJS(browser):
#     visa.Invalid_Cardholdername()
#     visa.EnterCardNumber(cardno)
#     visa.clickSubmitbtn()
#     assert visa.invalidmsg_cardholder()=='Invalid Cardholder Name',"invalid cardholder name taken"
#
# @allure.suite('Visa Iframe')
# @allure.title('Validate Card Number with invalid input(Visa JS)')
# def test_verifyCardNO_Validation_VisaJS(browser):
#     visa.validcardholdername(cardholder)
#     visa.InvalidCardNumber()
#     visa.clickSubmitbtn()
#     assert visa.invalidmsg_cardNo()=='Invalid Card Number',"invalid cardNumber taken"
#
# @allure.suite('Visa Iframe')
# @allure.title('Valid input Entered in required field and verify token and url(Visa JS)')
# def test_verifyCardNO_Validation_VisaJS(browser):
#     visa.validcardholdername(cardholder)
#     visa.EnterCardNumber(cardno)
#     visa.clickSubmitbtn()
#     assert visa.verify_VisaJStoken()==True,"Url and token not verified"
