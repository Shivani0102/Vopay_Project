import random
import time
import allure
import keyboard
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class VisaPage:
    iframelink= (By.XPATH,"//body/center[1]/iframe[1]")
    cardholdername =(By.XPATH,"//input[@name='cc-name']")
    cardNumber = (By.XPATH,"//input[@name='cc-number']")
    submitbtn= (By.XPATH,"//input[@value='Submit']")
    cardholdertext =(By.XPATH,"//label[contains(text(),'Cardholder Name')]")
    invalidcardholdermsg=(By.XPATH,"//pre[contains(text(),'Invalid Cardholder Name')]")
    invalidcardnotext=(By.XPATH,"//pre[contains(text(),'Invalid Card Number')]")
    thanktoken=(By.XPATH,"//div[@class='token-container']/div[1]/div[1]")



    def __init__(self, driver):
        self.driver= driver


    def switchwindow_VisaInner(self):
        time.sleep(2)
        self.driver.execute_script("window.open('http://vopay-testing.com/iframe/visa/inner.html','new window6')")
        time.sleep(3)
        print("open in new tab7")
        self.driver.switch_to.window(self.driver.window_handles[9])
        time.sleep(3)
        get= self.driver.current_url
        print(get)
        return get

    def Invalid_Cardholdername(self):
        name= self.driver.find_element(*self.cardholdername)
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        time.sleep(2)
        name.send_keys("456$#gs")
        time.sleep(3)

    def validcardholdername(self,cardholder):
        name = self.driver.find_element(*self.cardholdername)
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        time.sleep(2)
        name.send_keys(cardholder)

    def getcardholdertext(self):
        text= self.driver.find_element(*self.cardholdertext).text
        print(text)
        return text

    def clickSubmitbtn(self):
        self.driver.find_element(*self.submitbtn).click()
        time.sleep(3)


    def InvalidCardNumber(self):
        number = self.driver.find_element(*self.cardNumber)
        number.send_keys(Keys.CONTROL + "a")
        number.send_keys(Keys.DELETE)
        time.sleep(2)
        number.send_keys("cardno78437883f")
        time.sleep(2)

    def EnterCardNumber(self,cardno):
        number = self.driver.find_element(*self.cardNumber)
        number.send_keys(Keys.CONTROL + "a")
        number.send_keys(Keys.DELETE)
        time.sleep(2)
        number.send_keys(cardno)

    def invalidmsg_cardholder(self):
        text=self.driver.find_element(*self.invalidcardholdermsg).text
        print(text)
        return text

    def invalidmsg_cardNo(self):
        text=self.driver.find_element(*self.invalidcardnotext).text
        print(text)
        return text


    def verify_innerVisatoken(self):
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[9])
        time.sleep(2)
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        get= self.driver.current_url
        print(get)
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        time.sleep(4)
        getcountOR =str("http://vopay-testing.com/iframe/visa/inner.html")
        value = self.driver.find_element(*self.thanktoken).text
        print(value)
        if str(getcountOR) == str(get):
            return True
        else:
            return False


    def switchwindow_VisaJS(self):
        time.sleep(2)
        self.driver.execute_script("window.open('http://vopay-testing.com/iframe/visa/js.html','new window7')")
        time.sleep(3)
        print("open in new tab7")
        self.driver.switch_to.window(self.driver.window_handles[10])
        time.sleep(3)
        get= self.driver.current_url
        print(get)
        return get



    def verify_VisaJStoken(self):
        time.sleep(8)
        self.driver.switch_to.window(self.driver.window_handles[10])
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        # text1 = self.driver.find_element(*self.thanktoken).text
        # print(text1)
        self.driver.switch_to.window(self.driver.window_handles[10])
        time.sleep(2)
        elem = self.driver.find_element_by_xpath('//input[@id="Token"]')
        value = self.driver.execute_script('return arguments[0].value;', elem)
        token = str(print("{}".format(value)))
        if token != "" and token!=None:
            return True
        else:
            return False