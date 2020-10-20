import random
import time
from telnetlib import EC

import allure

from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from resources.variables import bankName


class Flinkspages:
    URL= "https://dev2.vopay.com/iframe/new/outer.html"
    desired_url = "https://www.tangerine.ca/app/#/"
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
    thanktoken=(By.XPATH,"//h2[contains(text(),'Thank You!')]")
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


    def __init__(self, driver):
        self.driver= driver

    def browser_load(self):
        self.driver.get(self.URL)
        self.driver.implicitly_wait(150)

    def switchtoiframe(self):
        time.sleep(6)
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)

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
        self.driver.implicitly_wait(50)
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
        self.driver.implicitly_wait(50)
        pwd= self.driver.find_element(*self.flinkpass)
        pwd.send_keys(Keys.CONTROL + "a")
        pwd.send_keys(Keys.DELETE)
        time.sleep(2)
        pwd.send_keys(invalidPass)
        time.sleep(2)

    @allure.description('Enter Valid username in FlinkURL')
    def verifyvalidpass(self,validpass):
        self.driver.implicitly_wait(50)
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
        self.driver.execute_script("window.open('https://dev2.vopay.com/iframe/old/outer.html','new window2')")
        time.sleep(3)
        print("open Flinks url in new tab2")
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        get= self.driver.current_url
        print(get)
        return get

    def switchwindow_oldinner(self):
        time.sleep(2)
        self.driver.execute_script("window.open('https://dev2.vopay.com/iframe/old/inner.html','new window3')")
        time.sleep(3)
        print("open in new tab2")
        self.driver.switch_to.window(self.driver.window_handles[5])
        time.sleep(3)

    def switchwindow_oldjs(self):
        time.sleep(2)
        self.driver.execute_script("window.open('https://dev2.vopay.com/iframe/old/js.html','new window4')")
        time.sleep(3)
        print("open in new tab2")
        self.driver.switch_to.window(self.driver.window_handles[5])
        time.sleep(3)

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
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(10)
        self.driver.implicitly_wait(300)
        wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.url_matches())
        # wait.until(
            # lambda driver: driver.current_url == desired_url)
        # wait.until(EC.visibility_of_element_located(By.XPATH,"https://www.tangerine.ca/app/#/"))
        time.sleep(20)
        get= self.driver.current_url
        print(get)
        return get

    def switchtab(self):
        time.sleep(3)
        # """1"""
        self.driver.switch_to.window(self.driver.window_handles[1])


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

    def Clicksimulatebutton(self):
        time.sleep(4)
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)
        self.driver.find_element(*self.SimulateLoginbutton).click()
        time.sleep(3)
        thank= self.driver.find_element(*self.thanktoken).text
        return thank

    def verify_token(self):
        time.sleep(2)
        get= self.driver.current_url
        print(get)
        getcountOR = "og88s44wgswc4gwc4oc00s08kskgw0www440ok8ko44c40c480kcsk8okk480css"
        string = str(get)
        getount = string.split("=")
        print(getount[1])
        try:
            if str(getcountOR) == str(getount[1]):
                return True
            else:
                return False

        except:
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
        self.driver.implicitly_wait(60)
        return text


