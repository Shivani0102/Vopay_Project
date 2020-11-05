import random
import time
import allure
import keyboard
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from resources.variables import bankName

# @pytest.mark.usefixtures("browser1")
class Iframe1:
    URL= "https://dev2.vopay.com/iframe/new/outer.html"
    newURL = "https://dev2.vopay.com/iframe/new/inner.html"
    jsurl = "https://dev2.vopay.com/iframe/new/js.html"
    iframelink= (By.XPATH,"//body/center[1]/iframe[1]")
    iframelinkinner = (By.XPATH, "/html[1]/body[1]/center[1]/iframe[1]")
    loadmore= (By.XPATH,"//button[@id='load-more']")
    banklist= (By.XPATH,"//div[@class='bankList__Item ']")
    searchbar= (By.XPATH,"//input[@id='search-bar']")
    flinkbank = (By.XPATH,"//div[@id='1885']//span[contains(text(),'FlinksCapital')]")
    cross= (By.XPATH,"//img[@class='bankListSearch--iconCross']")
    selectBank= (By.XPATH,"//img[@src='/images/logos-banks/98.svg']")
    proceedButton= (By.XPATH,"//button[@id='procced-bank']")
    onlinelBank =(By.XPATH,"//div[@class='bankListContainer desktopOnly']//span[contains(text(),'Connect my Bank Online')]")
    connectonlinelBank = (By.XPATH, "//a[contains(text(),'Connect my Bank Online')]")
    manualBank = (By.XPATH, "//span[contains(text(),'Connect my Bank Manually')]")
    TermsOfuse= (By.XPATH,"//h1[contains(text(),'Terms of use')]")
    verifyonlinemsg= (By.XPATH,"//p[@class='bankflow__StepsText']")
    manualmsg= (By.XPATH,"//p[contains(text(),'Add your Bank Information')]")
    changemybank= (By.XPATH,"//a[@data-ember-action='665']")
    Linkyourbankheader= (By.XPATH,"//h1[@class='bankList__Header']")
    acceptTerms=(By.XPATH,"//span[@data-ember-action='661']")
    accepttermsamepage =(By.XPATH,"//a[@data-ember-action='853']")
    acceptProceed= (By.XPATH,"//button[@class='bank__Button bank__Button--big']")
    crossbutton = (By.XPATH,"//span[@class='cross']")
    VopayTermslink= (By.XPATH,"//a[@data-ember-action='663']")
    # VopayTermslink =(By.XPATH,"//a[contains(text(),'Terms of use')]")
    userTransit= (By.XPATH,"//input[@id='username']")
    passTransit= (By.XPATH,"//input[@id='password']")
    loginclick = (By.XPATH,"//div[@id='ember658']//button[contains(text(),'Proceed')]")
    loginclicksecurit=(By.XPATH,"//div[@id='ember722']//button[contains(text(),'Proceed')]")
    chngbank=(By.XPATH,"//a[@id='change-bank']")
    Ques1= (By.XPATH,"//div[@id='ember722']//h1[@class='bankFlow__subTitle bankflow__sepearator']")
    ans= (By.XPATH,"//input[@id='anwser-question']")
    click= (By.XPATH,"//button[@data-ember-action='951']")
    searchicon = (By.XPATH,"//img[@src='images/search-ico.png']")
    nextpageUrl="http://portal-demo.vopay.com/#/login"
    retrylogin= (By.XPATH,"//button[contains(text(),'Retry Login')]")
    incorrectcredentails =(By.XPATH,"//p[contains(text(),'Credentials incorrect')]")
    verifyyouridentity =(By.XPATH,"//div[@id='ember722']//p[contains(text(),'Verify your identity')]")
    retryinsecurity =(By.XPATH,"//button[contains(text(),'Retry Question')]")
    selectcheque= (By.XPATH,"//div[@class='bank__radioButton bankflow__radioButton']")
    continuebtn= (By.XPATH,"//div[@id='ember790']//button[contains(text(),'Continue')]")
    selectotherbank =(By.XPATH,"//button[contains(text(),'Select other bank')]")
    addbankmanually =(By.XPATH,"//div[@class='bankListContainer--right bankListContainer--nobankList ']//button[contains(text(),'Add Bank Account Manually')]")
    institutionnumber =(By.XPATH,"//input[@id='institution-number']")
    transitnumber =(By.XPATH,"//input[@id='transit-number']")
    accountnumber =(By.XPATH,"//input[@id='account-number']")
    manualacceptterms = (By.XPATH,"//input[@id='ember852']")
    bankinfotext =(By.XPATH,"//p[contains(text(),'Add your Bank Information')]")
    servermsg= (By.XPATH,"//div[@id='ember771']//p[@class='bankflow__StepsText']")
    termofusechecbox= (By.XPATH,"//input[@id='ember403']")
    banknotlistmsg=(By.XPATH,"//div[@class='bankListContainer--right bankListContainer--nobankList ']/div[1]/h1[1]")
    personalAccount = (By.XPATH, "//span[contains(text(),'Personal Account')]")
    proceedBankinfopage = (By.XPATH, "//button[@data-ember-action='1153']")
    proceedEnableBankInfo = (By.XPATH, "//form[@id='manualBaninkInfo']//button[contains(text(),'Proceed')]")
    termsOfUseBankInfo = (By.XPATH, "//a[@data-ember-action='853']")
    validateaccount=(By.XPATH,"//li[@class='parsley-minlength']")
    changeAccount = (By.XPATH, "//form[@id='manualPersonal']//a[@class='bank__bottomLink']")
    changePersonal =(By.XPATH,"//form[@id='manualBusiness']//a[@class='bank__bottomLink']")
    businessCompanyName = (By.XPATH, "//input[@id='company-name-business']")
    businessFirstName = (By.XPATH, "//input[@id='first-name-business']")
    businessLastName = (By.XPATH, "//input[@id='last-name-business']")
    businessPhone = (By.XPATH, "//input[@id='phone-business']")
    PersonalFirstName = (By.XPATH, "//input[@id='first-name-personal']")
    PersonalLastName = (By.XPATH, "//input[@id='last-name-personal']")
    PersonalPhone = (By.XPATH, "//input[@id='phone-personal']")
    phntextvalidation= (By.XPATH,"//li[@class='parsley-minlength']")
    verifyphn =(By.XPATH,"//form[@id='manualPersonal']//ul[@class='parsley-errors-list filled']")
    PersonalEmail = (By.XPATH,"//input[@id='email-personal']")
    PersonalProceedbtn =(By.XPATH,"//form[@id='manualPersonal']/div[7]/button[1]")
    businessproceedbtn =(By.XPATH,"//form[@id='manualBusiness']/div[7]/button[1]")
    validateemail=(By.XPATH,"//li[@class='parsley-type']")
    tokenprint=(By.XPATH,"//div[@class='token-container']/div[1]/div[1]")
    Addaddressbtn = (By.XPATH,"//form[@id='manualPersonal']/p[@class='bankflow__AddressItem']/a[1]")
    addresstext =(By.XPATH,"//input[@id='address']")
    addressselect =(By.XPATH,"//div[@class='pca']//div[@class='pcaautocomplete pcatext'][2]/div[@class='pca pcalist']/div[3]")
    citytext= (By.XPATH,"//input[@id='city']")
    provincetext = (By.XPATH,"//input[@placeholder='Province']")
    drpprovince =(By.XPATH,"//ul[@class='dropdown-menu form__dropdownMenu ']/li[1]")
    provincelist=(By.XPATH,"//ul[@class='dropdown-menu form__dropdownMenu ']")
    postalcodetext = (By.XPATH,"//input[@id='postalcode']")
    addaddressbtn = (By.XPATH,"//button[contains(text(),'Add Address')]")
    Editbtn=(By.XPATH,"//form[@id='manualPersonal']//a[contains(text(),'Edit')]")
    editaddresstext =(By.XPATH,"//form[@id='manualPersonal']//div[@class='bank__input bank__input--Static']")
    cancelremovebtn= (By.XPATH,"//a[contains(text(),' Cancel/Remove')]")


    def __init__(self, driver1):
        self.driver1= driver1

    @allure.description('Launch outer url')
    def browser_load(self):
        self.driver1.get(self.URL)
        self.driver1.implicitly_wait(150)

    @allure.description('Switch to iframe')
    def switchtoiframe(self):
        time.sleep(6)
        frame= self.driver1.find_element(*self.iframelink)
        self.driver1.switch_to.frame(frame)

    def switchtoInnerIframe(self):
        time.sleep(6)
        self.driver1.switch_to.window(self.driver1.window_handles[1])
        frame= self.driver1.find_element(*self.iframelinkinner)
        self.driver1.switch_to.frame(frame)

    @allure.step('Search Tanger Bank')
    def searchBank(self, bankName):
        time.sleep(3)
        self.driver1.find_element(*self.searchbar).send_keys(bankName)
        time.sleep(4)