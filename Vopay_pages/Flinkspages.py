import random
import time
from telnetlib import EC

import allure
import keyboard

from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from resources.variables import bankName


class Flinkspages:

    URL= "https://vopay-testing.com/iframe/new/outer.html"
    desired_url = "https://vopay-testing.com/iframe/old/inner.html"
    iframelink= (By.XPATH,"//body/center[1]/iframe[1]")
    iframelink1 = (By.XPATH,"//iframe[@src='https://earthnode-dev.vopay.com/iq11/embed/3498f75d7511a31e3f381e6944a081843ed742f3/true']")
    iframelink2 = (By.XPATH,"//iframe[@sandbox='allow-same-origin allow-scripts allow-popups allow-forms allow-top-navigation']")
    connectbankhomepage = (By.XPATH,"//h4[contains(text(),'Connect with your bank')]")
    cancelbutton= (By.XPATH,"//input[@value='Cancel']")
    logo= (By.XPATH,"//div[@class='my-3x logo-full']")
    searchbar = (By.XPATH,"//input[@placeholder='Search for your bank']")
    proceedButton= (By.XPATH,"//button[@id='procced-bank']")
    selectBank= (By.XPATH,"//img[@src='/images/logos-banks/98.svg']")
    tanFlink =(By.XPATH,"//img[@alt='Tangerine']")
    agreepage= (By.XPATH,"//h2[@class='heading___usvnO ml-2x']")
    manualBank=(By.XPATH,"//span[contains(text(),'Connect my Bank Online')]")
    acceptTerms=(By.XPATH,"//span[@data-ember-action='623']")
    acceptProceed= (By.XPATH,"//button[@class='bank__Button bank__Button--big']")
    userTransit= (By.XPATH,"//input[@id='username']")
    backarrow = (By.XPATH,"//a[@tabindex='101']")
    verifytext = (By.XPATH,"//text[contains(text(),'Access your account number')]")
    verifytext2= (By.XPATH,"//text[contains(text(),'Access your account transaction history')]")
    verifytext3 =(By.XPATH,"//text[contains(text(),'Access your name, email, address and phone number')]")
    Hidebutton= (By.XPATH,"//button[@id='redirectToHide']")
    agreecontinuebutton =(By.XPATH,"//input[@value='Agree and Continue']")
    submitbutton =(By.XPATH,"//input[@value='Submit']")
    redlineHide= (By.XPATH,"//button[@onclick='redirectToHide();']")
    flinkusername= (By.XPATH,"//input[@name='username']")
    flinkpass= (By.XPATH,"//input[@name='password']")
    resetpass = (By.XPATH ,"//text[contains(text(),'Reset password')]")
    SimulateLoginbutton= (By.XPATH,"//button[@id='redirectToSuccessful']")
    invalidpasstext= (By.XPATH,"//p[contains(text(),'Invalid password')]")
    invalidusertext = (By.XPATH, "//p[contains(text(),'Invalid username')]")
    invalidsecuritytext = (By.XPATH, "//p[contains(text(),'Invalid answer')]")
    retrybutton=(By.XPATH,"//input[@value='Retry']")
    thanktoken=(By.XPATH,"//div[@class='token-container']/div[1]/div[1]")
    flinkbank= (By.XPATH,"//img[@alt='Flinks Capital International']")
    # ques1city=(By.XPATH,"//label[contains(text(),'What city were you born in?')]")
    ques1city=(By.XPATH,"//label[contains(text(),'What is the best country on earth?')]")
    answer = (By.XPATH,"//input[@id='mfa-QuestionAndAnswer-0']")
    answertitle =(By.XPATH,"//label[@class='label-small']")
    continuebtn = (By.XPATH,"//input[@value='Continue']")
    connection =(By.XPATH,"//h1[@class='title___2dOQ9 my-3x']")
    securityans = (By.XPATH,"//text[contains(text(),'Answer to security question:')]")
    securityanstext =(By.XPATH,"//ul[@class='list-unstyled']/li[1]")
    selectaccount =(By.XPATH,"//h1[@class='h4']/span[1]/div[1]")
    cheque1=(By.XPATH,"//a[@tabindex='2']")
    cheque2 = (By.XPATH,"//a[@tabindex='1']")
    innertoken = (By.XPATH, "//div[@class='well']/text()")
    tokensimulatejs=(By.XPATH,"//input[@value='og88s44wgswc4gwc4oc00s08kskgw0www440ok8ko44c40c480kcsk8okk480css']")



    def __init__(self, driver):
        self.driver= driver

    def browser_load(self):
        self.driver.get(self.URL)
        self.driver.implicitly_wait(150)

    def switchtoiframe(self):
        time.sleep(6)
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)


    def switchtoiframesimulate(self):
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[5])
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        frame= self.driver.find_element(*self.iframelink2)
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        frame= self.driver.find_element(*self.iframelink2)
        self.driver.switch_to.frame(frame)

    def switchtoiframesimulate_JS(self):
        time.sleep(6)
        self.driver.switch_to.window(self.driver.window_handles[7])
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        element=print (self.driver.page_source)
        string = str(element)


    def refreshpage(self):
        self.driver.refresh()
        self.driver.implicitly_wait(100)
        time.sleep(4)

    def switchtoiframe2(self):
        time.sleep(2)
        try:
            hide= self.driver.find_element(*self.redlineHide).is_displayed()
            if hide==True:
                frame1 = self.driver.find_element(*self.iframelink2)
                self.driver.switch_to.frame(frame1)
                time.sleep(2)
                frame2 = self.driver.find_element(*self.iframelink2)
                self.driver.switch_to.frame(frame2)
                return True
            # else:
            #     frame1 = self.driver.find_element(*self.iframelink1)
            #     self.driver.switch_to.frame(frame1)
            #     time.sleep(2)
            #     frame2 = self.driver.find_element(*self.iframelink2)
            #     self.driver.switch_to.frame(frame2)
        except:
            frame2 = self.driver.find_element(*self.iframelink2)
            self.driver.switch_to.frame(frame2)
            return False


    def searchBank1(self, TanName):
        time.sleep(5)
        bankname= self.driver.find_element(*self.searchbar)
        bankname.clear()
        bankname.send_keys(TanName)
        time.sleep(2)
        display = self.driver.find_element(*self.tanFlink).is_displayed()
        return display

    def search_flinknamedBank(self, flinkName):
        time.sleep(5)
        bankname= self.driver.find_element(*self.searchbar)
        bankname.send_keys(Keys.CONTROL + "a")
        bankname.send_keys(Keys.DELETE)
        bankname.send_keys(flinkName)
        time.sleep(2)
        display = self.driver.find_element(*self.flinkbank).is_displayed()
        self.driver.find_element(*self.flinkbank).click()
        return display
    #
    def selectBankClick(self):
        Tan = self.driver.find_element(*self.selectBank).is_displayed()
        self.driver.find_element(*self.selectBank).click()
        time.sleep(2)
        self.driver.find_element(*self.proceedButton).click()
        time.sleep(3)
        return Tan

    def selectTan_flink(self):
        time.sleep(2)
        self.driver.find_element(*self.tanFlink).click()
        time.sleep(3)
        agree = self.driver.find_element(*self.agreepage).text
        return agree

    def selectFlink_Bank(self):
        time.sleep(2)
        self.driver.find_element(*self.flinkbank).click()
        time.sleep(3)
        agree = self.driver.find_element(*self.agreepage).text
        return agree


    def verifyAgreepage(self):
        text= self.driver.find_element(*self.verifytext).text
        return text

    def verifyTextAgree(self):
        text = self.driver.find_element(*self.verifytext2).text
        get = self.driver.current_url
        print(get)
        return text

    def verifyTextAgree2(self):
        text = self.driver.find_element(*self.verifytext3).text
        print(text)
        return text

    def ClickCancelbutton(self):
        self.driver.find_element(*self.cancelbutton).click()
        time.sleep(2)
        homepage = self.driver.find_element(*self.connectbankhomepage).text
        return homepage

    def Click_agreeButton(self):
        logo =self.driver.find_element(*self.logo).is_displayed()
        self.driver.find_element(*self.agreecontinuebutton).click()
        time.sleep(3)
        return logo


    def clickonBackarrow(self):
        self.driver.find_element(*self.backarrow).click()
        time.sleep(2)
        homepage = self.driver.find_element(*self.connectbankhomepage).text
        return homepage

    @allure.description('Enter Invalid username in FlinkURL')
    def verifyinvalidusername(self, invalidUser):
        self.driver.implicitly_wait(60)
        user =self.driver.find_element(*self.flinkusername)
        user.send_keys(Keys.CONTROL + "a")
        user.send_keys(Keys.DELETE)
        time.sleep(3)
        user.send_keys(invalidUser)


    @allure.description('Enter Valid username in FlinkURL')
    def verifyvalidusername(self,validuser):
        self.driver.implicitly_wait(50)
        user= self.driver.find_element(*self.flinkusername)
        user.send_keys(Keys.CONTROL + "a")
        user.send_keys(Keys.DELETE)
        time.sleep(2)
        user.send_keys(validuser)
        time.sleep(2)



    @allure.description('Enter Invalid password in FlinkURL')
    def verifyinvalidPass(self, invalidPass):
        self.driver.implicitly_wait(60)
        pwd= self.driver.find_element(*self.flinkpass)
        pwd.send_keys(Keys.CONTROL + "a")
        pwd.send_keys(Keys.DELETE)
        time.sleep(2)
        pwd.send_keys(invalidPass)
        time.sleep(2)

    @allure.description('Enter Valid username in FlinkURL')
    def verifyvalidpass(self,validpass):
        self.driver.implicitly_wait(60)
        pwd = self.driver.find_element(*self.flinkpass)
        pwd.send_keys(Keys.CONTROL + "a")
        pwd.send_keys(Keys.DELETE)
        time.sleep(2)
        pwd.send_keys(validpass)
        time.sleep(3)


    @allure.description('Accept Vopay Terms and policy')
    def AcceptVopayTerms(self):
        time.sleep(2)
        checkbox= self.driver.find_element(*self.acceptTerms)
        checkbox.click()
        enablebutton= self.driver.find_element(*self.acceptProceed).is_enabled()
        self.driver.find_element(*self.acceptProceed).click()
        time.sleep(3)
        return enablebutton


    def ClickProceedButton(self):
        self.driver.find_element(*self.proceedButton).click()
        time.sleep(3)
        self.driver.find_element(*self.manualBank).click()
        time.sleep(3)

    def switchagain_oldouter(self):
        time.sleep(4)
        self.driver.execute_script("window.open('https://vopay-testing.com/iframe/old/outer.html','new window2')")
        time.sleep(3)
        print("open flinks url in new tab3")
        self.driver.switch_to.window(self.driver.window_handles[3])
        time.sleep(3)
        get= self.driver.current_url
        print(get)
        return get

    def switchwindow_oldinner(self):
        time.sleep(3)
        self.driver.execute_script("window.open('https://vopay-testing.com/iframe/old/inner.html','new window3')")
        time.sleep(5)
        print("open flinks in new tab4")
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[5])
        time.sleep(3)
        get= self.driver.current_url
        print(get)
        return get

    def switchwindow_oldjs(self):
        time.sleep(2)
        self.driver.execute_script("window.open('https://vopay-testing.com/iframe/old/js.html','new window5')")
        time.sleep(3)
        print("open flinks in new tab6")
        self.driver.switch_to.window(self.driver.window_handles[7])
        time.sleep(3)
        get= self.driver.current_url
        print(get)
        return get

    def VerifyonHide(self):
        time.sleep(2)
        self.driver.find_element(*self.Hidebutton).click()
        try:
            time.sleep(3)
            hide= self.driver.find_element(*self.Hidebutton).is_displayed()
            if hide==True:
                return True
            else:
                return False
        except:
            return False

    def Clickresetpassword_button(self):
        self.driver.find_element(*self.resetpass).click()
        self.driver.implicitly_wait(200)
        time.sleep(6)
        self.driver.refresh()
        # """6"""
        self.driver.switch_to.window(self.driver.window_handles[4])
        time.sleep(10)
        self.driver.implicitly_wait(300)
        wait = WebDriverWait(self.driver, 10)
        time.sleep(20)
        get= self.driver.current_url
        print(get)
        return get

    def switchtab(self):
        time.sleep(3)
        # """1/3"""
        self.driver.switch_to.window(self.driver.window_handles[3])

    def Clickresetpassword_button_inner(self):
        self.driver.find_element(*self.resetpass).click()
        self.driver.implicitly_wait(200)
        time.sleep(6)
        self.driver.refresh()
        # """6"""
        self.driver.switch_to.window(self.driver.window_handles[6])
        time.sleep(10)
        self.driver.implicitly_wait(300)
        wait = WebDriverWait(self.driver, 10)
        time.sleep(20)
        get= self.driver.current_url
        print(get)
        return get

    def Clickresetpassword_button_js(self):
        self.driver.find_element(*self.resetpass).click()
        self.driver.implicitly_wait(200)
        time.sleep(6)
        self.driver.refresh()
        # """6"""
        self.driver.switch_to.window(self.driver.window_handles[8])
        time.sleep(10)
        self.driver.implicitly_wait(300)
        wait = WebDriverWait(self.driver, 10)
        time.sleep(20)
        get= self.driver.current_url
        print(get)
        return get

    def switchtabJS(self):
        time.sleep(3)
        # """1"""
        self.driver.switch_to.window(self.driver.window_handles[7])

    def switchtabinner(self):
        time.sleep(3)
        # """1"""
        self.driver.switch_to.window(self.driver.window_handles[5])

    def loginFlinks(self):
        try:
            submit = self.driver.find_element(*self.submitbutton)
            data1= submit.is_enabled()
            if data1==True:
                submit.click()
                return data1
        except:
            data1=False
            return data1
        value= self.driver.find_element(*self.connection).text
        print(value)
        self.driver.implicitly_wait(100)


    def Clickretrybutton(self):
        self.driver.implicitly_wait(100)
        retry= self.driver.find_element(*self.retrybutton).is_displayed()
        try:
            text = self.driver.find_element(*self.invalidpasstext).text
            self.driver.find_element(*self.retrybutton).click()
            print(text)
        except:
            text = self.driver.find_element(*self.invalidusertext).text
            self.driver.find_element(*self.retrybutton).click()
            print(text)
        return retry


    def Clicksimulatebutton_inner(self):
        time.sleep(5)
        self.driver.refresh()
        self.driver.implicitly_wait(150)
        self.driver.switch_to.window(self.driver.window_handles[5])
        time.sleep(3)
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)
        self.driver.find_element(*self.SimulateLoginbutton).click()
        time.sleep(8)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        value= self.driver.find_element(*self.thanktoken).text
        token =str(print(value))
        if token !="":
            return True
        else:
            return False


    def Clicksimulatebutton(self):
        time.sleep(5)
        self.driver.refresh()
        self.driver.implicitly_wait(150)
        self.driver.switch_to.window(self.driver.window_handles[7])
        frame = self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)
        time.sleep(3)
        self.driver.find_element(*self.SimulateLoginbutton).click()
        time.sleep(5)


    def verify_outertoken(self):
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[3])
        time.sleep(2)
        get= self.driver.current_url
        print(get)
        global getcountOR
        getcountOR =self.driver.find_element(*self.thanktoken).text
        print(getcountOR)
        string = str(get)
        token= string.split("&")
        print(token[0])
        string1 = str(token[0])
        getount = string1.split("=")
        get1= str(getount[1])
        print(get1)
        try:
            if str(getcountOR) == str(get1):
                return True
        except:
            return False


    def verify_innertoken(self):
        time.sleep(10)
        # self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        get= self.driver.current_url
        print(get)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        time.sleep(4)
        value = self.driver.find_element(*self.thanktoken).text
        token =str(print(value))
        if token !="":
            return True
        else:
            return False



    def verify_token(self):
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[5])
        time.sleep(2)
        get= self.driver.current_url
        print(get)
        frame= self.driver.find_element(*self.iframelink2)
        self.driver.switch_to.frame(frame)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        value = str("https://vopay-testing.com/iframe/old/inner.html")
        if str(value) == str(get):
            return True
        else:
            return False


    def verify_tokenJS(self):
        time.sleep(10)
        get= self.driver.current_url
        print(get)
        frame= self.driver.find_element(*self.iframelink2)
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        getcountOR =str("og88s44wgswc4gwc4oc00s08kskgw0www440ok8ko44c40c480kcsk8okk480css")
        print(getcountOR)
        time.sleep(2)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        value = self.driver.find_element(*self.thanktoken).text
        print(value)
        if str(getcountOR) == str(value):
            return True
        else:
            return False

    def verify_invalidsecurityans(self):
        time.sleep(2)
        self.driver.find_element(*self.answer).send_keys("answer")
        self.driver.find_element(*self.continuebtn).click()
        time.sleep(3)
        text= self.driver.find_element(*self.retrybutton).is_displayed()
        # print(text)
        self.driver.find_element(*self.retrybutton).click()
        return text

    def verify_security(self):
        text=self.driver.find_element(*self.securityans).text
        get=self.driver.find_element(*self.securityanstext).text
        print(text)
        print(get)
        string = str(get)
        getount = string.split(": ")
        get1= str(getount[1])
        print(get1)
        entervalue= self.driver.find_element(*self.answer)
        entervalue.send_keys(Keys.CONTROL + "a")
        entervalue.send_keys(Keys.DELETE)
        time.sleep(2)
        entervalue.send_keys(get1)
        time.sleep(2)
        self.driver.find_element(*self.continuebtn).click()


    def selectAccount(self):
        text = self.driver.find_element(*self.selectaccount).text
        print(text)
        try:
            self.driver.find_element(*self.cheque1).is_displayed()
            self.driver.find_element(*self.cheque1).click()
        except:
            select= self.driver.find_element(*self.cheque1)
            select.is_displayed()
            select.click()
        time.sleep(2)
        self.driver.find_element(*self.continuebtn).click()
        self.driver.implicitly_wait(100)
        time.sleep(3)
        return text

    def JS_token(self):
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[7])

        new_caps = {}
        new_caps["browserName"] = 'chrome',
        new_caps["javascriptEnabled"] = True,
        new_caps["acceptSslCerts"] = True

        d = DesiredCapabilities.CHROME
        d['goog:loggingPrefs'] = {'browser': 'ALL'}
        # d['loggingPrefs'] = {'browser': 'ALL'}
        # driver = webdriver.Chrome(desired_capabilities=d)
        time.sleep(3)
        logs_1 = self.driver.get_log('browser')
        print("A::", logs_1)
        # logs_2 = self.driver.get_log('browser')
        # print("B::", logs_2)
        # time.sleep(4)
        #
        # for entry in self.driver.get_log('browser'):
        #     print(entry)
        time.sleep(2)
        get = self.driver.current_url
        print(get)
        url=str("https://vopay-testing.com/iframe/old/js.html")
        if str(url)==str(get):
            return True
        else:
            return False

    def check_errors_console_log(self):
        time.sleep(10)

        # log = self.driver.read_browser_console_log()
        # log_errors = []
        # for entry in log:
        #     if entry['level'] == 'SEVERE':
        #         log_errors.append(entry['message'])
        # "Function to get the browser's console log errors"

        current_console_log_errors = []
        # As IE driver does not support retrieval of any logs,
        # we are bypassing the get_browser_console_log() method
        if "ie" not in str(self.driver):
            log_errors = []
            new_errors = []
            log = self.get_browser_console_log()
            print("Console Log: ", log)
            for entry in log:
                if entry['level'] == 'SEVERE':
                    log_errors.append(entry['message'])

            if current_console_log_errors != log_errors:
                # Find the difference
                new_errors = list(set(log_errors) - set(current_console_log_errors))
                # Set current_console_log_errors = log_errors
                current_console_log_errors = log_errors
                print(current_console_log_errors)

            if len(new_errors) > 0:
                print("\nBrowser console error on url: %s\nConsole error(s):%s" % (self.driver.current_url, '\n----'.join(new_errors)))

    def get_browser_console_log(self):
        "Get the browser console log"
        try:
            log = self.driver.get_log('browser')
            return log
        except Exception as e:
            print("Exception when reading Browser Console log")
            print(str(e))

        driver = webdriver.PhantomJS("/usr/local/bin/phantomjs")
        # driver.get("https://infoheap.com/demo/page_having_js_member_errors.html")
        print (self.driver.get_log('browser'))


    def JS_tokenvalue(self):
        time.sleep(8)
        self.driver.switch_to.window(self.driver.window_handles[7])
        elem = self.driver.find_element_by_xpath('//input[@id="Token"]')
        value = self.driver.execute_script('return arguments[0].value;', elem)
        token= str(print("{}".format(value)))
        if token!="" and token != None:
            return True
        else:
            return False

    def JS_Bankvalue(self):
        time.sleep(2)
        elem = self.driver.find_element_by_xpath('//input[@id="Bank"]')
        value = self.driver.execute_script('return arguments[0].value;', elem)
        bank= str(print("{}".format(value)))
        if bank !="" and bank != None:
            return True
        else:
            return False

    def JS_FullName(self):
        time.sleep(2)
        elem = self.driver.find_element_by_xpath('//input[@id="FullName"]')
        value = self.driver.execute_script('return arguments[0].value;', elem)
        Name= str(print("{}".format(value)))
        if Name !="" and Name != None:
            return True
        else:
            return False

    def JS_MaskedAccount(self):
        time.sleep(2)
        elem = self.driver.find_element_by_xpath('//input[@id="MaskedAccount"]')
        value = self.driver.execute_script('return arguments[0].value;', elem)
        Name= str(print("{}".format(value)))
        if Name !="" and Name != None:
            return True
        else:
            return False