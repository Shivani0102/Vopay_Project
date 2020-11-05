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


class Iframe:
    URL= "https://vopay-testing.com/iframe/new/outer.html"
    innerurl = "https://vopay-testing.com/iframe/new/inner.html"
    jsurl = "https://vopay-testing.com/iframe/new/js.html"
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
    manualBank = (By.XPATH, "//div[@class='bankListContainer desktopOnly']//span[contains(text(),'Connect my Bank Manually')]")
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


    def __init__(self, driver):
        self.driver= driver

    @allure.description('Launch outer url')
    def browser_load(self):
        self.driver.get(self.URL)
        self.driver.implicitly_wait(150)

    @allure.description('Switch to iframe')
    def switchtoiframe(self):
        time.sleep(6)
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)

    def switchtoInnerIframe(self):
        time.sleep(6)
        self.driver.switch_to.window(self.driver.window_handles[1])
        frame= self.driver.find_element(*self.iframelinkinner)
        self.driver.switch_to.frame(frame)

    @allure.description('Click on LoadMore button')
    def verify_loadMore(self):
        time.sleep(3)
        load =self.driver.find_element(*self.loadmore)

        # load.click()
        try:
            for x in range(0, 6):
                # load.click()
                display = self.driver.find_element(*self.loadmore).is_displayed()
                if display==True:
                    load.click()

        except:
            return False

    @allure.step('Show all counts of bank')
    def showall_banklist(self):
        time.sleep(2)
        list= self.driver.find_elements(*self.banklist)
        bank= len(list)
        print(bank)

    @allure.step('Search Tanger Bank')
    def searchBank(self, bankName):
        time.sleep(3)
        self.driver.find_element(*self.searchbar).send_keys(bankName)
        time.sleep(4)

    @allure.description('Select Tanger Bank and click proceed button')
    def selectBankClick(self):
        self.driver.find_element(*self.selectBank).click()
        time.sleep(2)
        self.driver.find_element(*self.proceedButton).click()

    @allure.description('Verify msg for Manualbank page')
    def verify_manualmsg(self):
        manualmsg= self.driver.find_element(*self.manualmsg).text
        print(manualmsg)
        return manualmsg


    def selectbankmethod_online(self):
        online= self.driver.find_element(*self.onlinelBank)
        online1= online.is_displayed()
        time.sleep(3)
        online.click()
        # time.sleep(3)
        return online1

    @allure.description('Click on CoonectbankOnline link')
    def redirect_onlinebank(self):
        time.sleep(3)
        actionchains=ActionChains(self.driver)
        actionchains.send_keys(Keys.PAGE_DOWN).perform()
        actionchains.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        redirect= self.driver.find_element(*self.connectonlinelBank).text
        self.driver.find_element(*self.connectonlinelBank).click()
        time.sleep(3)
        return redirect


    def verify_manualBank(self):
        manual= self.driver.find_element(*self.manualBank)
        manualbank= manual.is_displayed()
        manual.click()
        time.sleep(3)
        return manualbank

    @allure.description('Accept Vopay Terms and policy')
    def AcceptVopayTerms(self):
        data = self.driver.find_element(*self.acceptTerms)
        time.sleep(2)
        try:
            checkbox = data.is_selected()
            if checkbox==False:
                data.click()

        except:
            print("checkbox not selected")


    def click_VopayTermslink(self):
        Terms = self.driver.find_element(*self.VopayTermslink).text
        time.sleep(2)
        self.driver.find_element(*self.VopayTermslink).click()
        time.sleep(3)
        self.driver.find_element(*self.crossbutton).click()
        try:
            checkbox = self.driver.find_element(*self.acceptTerms)
            data= checkbox.is_selected()
            if data==False:
                checkbox.click()
        except:
            data1=False
        return Terms


    @allure.description('Verify msg for bankOnlinepage')
    def verify_msg(self):
        change= self.driver.find_element(*self.verifyonlinemsg).text
        print(change)
        # change1 = change.is_displayed()
        return change


    @allure.description('enter password and click proceed in bankOnlinepage')
    def LoginTransit(self,pwd):
        actionchains = ActionChains(self.driver)
        self.driver.find_element(*self.passTransit).send_keys(pwd)
        time.sleep(2)
        # self.driver.find_element(*self.loginclick).click()

        try:
            login = self.driver.find_element(*self.loginclick)
            data= login.is_enabled()
            if data == True:
                # self.driver.find_element(*self.loginclick).click()
                return True

        except:
            # data= False
            self.driver.find_element(*self.acceptTerms).click()
            return False
            # self.driver.find_element(*self.loginclick).click()
        self.driver.implicitly_wait(300)
        time.sleep(10)

    @allure.description('click proceed in bankOnlinepage and verify login succesfully or not')
    def Login_procced(self):
        try:
            login = self.driver.find_element(*self.loginclick)
            data= login.is_enabled()
            if data == True:
                self.driver.find_element(*self.loginclick).click()
        except:

            self.driver.find_element(*self.acceptTerms).click()
            self.driver.find_element(*self.loginclick).click()
        self.driver.implicitly_wait(180)



    def retrylogin_incorrect(self):
        time.sleep(10)
        text=self.driver.find_element(*self.incorrectcredentails).text
        print(text)
        time.sleep(5)
        self.driver.find_element(*self.retrylogin).click()
        return text

    def invalid_insecurity(self):
        time.sleep(5)
        text = self.driver.find_element(*self.verifyyouridentity).text
        print(text)
        value= self.driver.find_element(*self.ans)
        value.send_keys(Keys.CONTROL + "a")
        value.send_keys(Keys.DELETE)
        value.send_keys("Vopay")
        time.sleep(2)
        self.driver.find_element(*self.loginclicksecurit).click()
        time.sleep(6)
        invalidsecurity= self.driver.find_element(*self.retryinsecurity)
        verify= invalidsecurity.is_displayed()
        invalidsecurity.click()
        return verify


    def Verifysecurity_answer(self):
        time.sleep(4)
        # text = self.driver.find_element(*self.verifyyouridentity).text
        # print(text)
        value= self.driver.find_element(*self.Ques1).text
        print(value)
        time.sleep(3)
        string = str(value)
        get= string.split(" ")
        print(get[1])
        print(get[4])
        ans1= str("shape")
        ans2 = str("country")
        if str(get[1])==str(ans1):
            print("first")
            ans1 = self.driver.find_element(*self.ans)
            ans1.send_keys(Keys.CONTROL + "a")
            ans1.send_keys(Keys.DELETE)
            time.sleep(2)
            ans1.send_keys("Triangle")
        elif str(get[4]) == str(ans2):
            print("second if")
            ans1 = self.driver.find_element(*self.ans)
            ans1.send_keys(Keys.CONTROL + "a")
            ans1.send_keys(Keys.DELETE)
            time.sleep(2)
            ans1.send_keys("Canada")
        else:
            print("else con")
            ans1 = self.driver.find_element(*self.ans)
            ans1.send_keys(Keys.CONTROL + "a")
            ans1.send_keys(Keys.DELETE)
            time.sleep(2)
            ans1.send_keys("Montreal")
        self.driver.find_element(*self.loginclicksecurit).click()
        time.sleep(4)
        success=self.driver.find_element(*self.selectcheque).is_displayed()
        return success

    def selectcheque_continue(self):
        time.sleep(10)
        self.driver.find_element(*self.selectcheque).click()
        time.sleep(2)
        btn=self.driver.find_element(*self.continuebtn).is_enabled()
        time.sleep(2)
        self.driver.find_element(*self.continuebtn).click()
        return btn

    @allure.description('Open new tab and launch Vopay inner url')
    def switchwindow(self):
        time.sleep(2)
        self.driver.implicitly_wait(60)
        self.driver.execute_script("window.open('https://vopay-testing.com/iframe/new/inner.html','new window')")
        print("open in new tab")
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        get= self.driver.current_url
        print(get)
        return get

    def backarrow_inner(self):
        time.sleep(4)
        self.driver.get(*self)
        self.driver.refresh()
        self.driver.implicitly_wait(100)


    def backarrow_js(self):
        time.sleep(4)
        # url = str("https://vopay-testing.com/iframe/new/inner.html")
        # get =self.driver.current_url
        self.driver.refresh()
        self.driver.implicitly_wait(100)

    @allure.description('Open new tab and launch Vopay js url')
    def switchagain_jsbrowser(self):
        time.sleep(4)
        self.driver.execute_script("window.open('https://vopay-testing.com/iframe/new/js.html','new window1')")
        time.sleep(3)
        print("open in new tab2")
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(3)
        get= self.driver.current_url
        print(get)
        return get

    def verify_changemybank(self):
        actionchains=ActionChains(self.driver)
        actionchains.send_keys(Keys.PAGE_DOWN).perform()
        actionchains.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        self.driver.find_element(*self.changemybank).click()
        time.sleep(5)



    def changebank_differpage(self):
        self.driver.find_element(*self.chngbank).click()
        search= self.driver.find_element(*self.searchicon).is_displayed()
        self.driver.find_element(*self.selectBank).click()
        time.sleep(2)
        self.driver.find_element(*self.proceedButton).click()
        time.sleep(3)

    def Accept_manualterms(self):
        try:
            checkbox = self.driver.find_element(*self.accepttermsamepage)
            data= checkbox.is_selected()
            if data==False:
                checkbox.click()
        except:
            data1=False
        # return Terms
        try:
            cross= self.driver.find_element(*self.crossbutton)
            button = cross.is_displayed()
            if button==True:
                cross.click()
        except:
            print("cross button not displayed")


    @allure.description('Enter Invalid username in FlinkURL')
    def verifyinvalidusername_vopay(self, invalidUser):
        self.driver.implicitly_wait(50)
        user =self.driver.find_element(*self.userTransit)
        user.send_keys(Keys.CONTROL + "a")
        user.send_keys(Keys.DELETE)
        time.sleep(3)
        user.send_keys(invalidUser)


    @allure.description('Enter Valid username in FlinkURL')
    def verifyvalidusername_vopay(self,validuser):
        self.driver.implicitly_wait(50)
        user= self.driver.find_element(*self.userTransit)
        user.send_keys(Keys.CONTROL + "a")
        user.send_keys(Keys.DELETE)
        time.sleep(2)
        user.send_keys(validuser)
        time.sleep(2)


    @allure.description('Enter Invalid password in FlinkURL')
    def verifyinvalidPass_vopay(self, invalidPass):
        self.driver.implicitly_wait(50)
        pwd= self.driver.find_element(*self.passTransit)
        pwd.send_keys(Keys.CONTROL + "a")
        pwd.send_keys(Keys.DELETE)
        time.sleep(2)
        pwd.send_keys(invalidPass)
        time.sleep(2)

    @allure.description('Enter Valid username in FlinkURL')
    def verifyvalidpass_vopay(self,validpass):
        self.driver.implicitly_wait(50)
        pwd = self.driver.find_element(*self.passTransit)
        pwd.send_keys(Keys.CONTROL + "a")
        pwd.send_keys(Keys.DELETE)
        time.sleep(2)
        pwd.send_keys(validpass)
        time.sleep(3)

    def search_flinknamedBank_vopay(self, flinkName):
        time.sleep(5)
        bankname= self.driver.find_element(*self.searchbar)
        bankname.send_keys(Keys.CONTROL + "a")
        bankname.send_keys(Keys.DELETE)
        bankname.send_keys(flinkName)
        time.sleep(4)
        display = self.driver.find_element(*self.flinkbank).is_displayed()
        time.sleep(2)
        self.driver.find_element(*self.flinkbank).click()
        self.driver.find_element(*self.proceedButton).click()
        return display


    def successfullytransactionmsg(self):
        text=self.driver.find_element(*self.servermsg).text
        time.sleep(5)
        return text

    def click_selectotherbank(self):
        time.sleep(3)
        bank= self.driver.find_element(*self.selectotherbank).is_displayed()
        self.driver.find_element(*self.selectotherbank).click()
        time.sleep(2)
        return bank

    def enterbannotlist(self):
        ans= self.driver.find_element(*self.searchbar)
        ans.send_keys(Keys.CONTROL + "a")
        ans.send_keys(Keys.DELETE)
        time.sleep(2)
        ans.send_keys("Fleekvopay")
        actionchains=ActionChains(self.driver)
        actionchains.send_keys(Keys.BACKSPACE).perform()
        time.sleep(2)
        actionchains.send_keys(Keys.BACKSPACE).perform()
        # self.driver.find_element(*self.searchicon).click()
        time.sleep(4)
        manually=self.driver.find_element(*self.banknotlistmsg).text
        self.driver.find_element(*self.addbankmanually).click()
        print(manually)
        return manually

    def enterinstitution(self,institution):
        institute=self.driver.find_element(*self.institutionnumber)
        institute.send_keys(Keys.CONTROL + "a")
        institute.send_keys(Keys.DELETE)
        institute.send_keys(institution)

    def enterTransit(self,Transitno):
        Transit=self.driver.find_element(*self.transitnumber)
        Transit.send_keys(Keys.CONTROL + "a")
        Transit.send_keys(Keys.DELETE)
        Transit.send_keys(Transitno)
        time.sleep(2)

    def enterAccountno(self,Accountno):
        bank =self.driver.find_element(*self.bankinfotext).text
        print(bank)
        account=self.driver.find_element(*self.accountnumber)
        account.send_keys(Keys.CONTROL + "a")
        account.send_keys(Keys.DELETE)
        account.send_keys(Accountno)
        time.sleep(2)
        return bank

    def validationAccountmsg(self):
        accountchar =self.driver.find_element(*self.validateaccount).text
        print(accountchar)
        time.sleep(3)
        account=self.driver.find_element(*self.accountnumber)
        account.send_keys(Keys.CONTROL + "a")
        account.send_keys(Keys.DELETE)
        account.send_keys("12345678")
        return accountchar


    def clickTremofuse_checkbox(self):
        self.driver.find_element(*self.termofusechecbox).click()
        button=self.driver.find_element(*self.proceedBankinfopage)
        try:
            click= button.is_enabled()
            if click==True:
                button.click()
        except:
            print("fill all remaining details")
            self.driver.find_element(*self.termofusechecbox).click()
            time.sleep(2)
            self.driver.find_element(*self.proceedBankinfopage).click()


    def clickpesonalAccount(self):
        account=self.driver.find_element(*self.personalAccount)
        account.click()

    def verifyproceed_enabled(self):
        time.sleep(3)
        # self.driver.find_element(*self.termsOfUseBankInfo).click()
        # self.driver.find_element(*self.crossbutton).click()
        button=self.driver.find_element(*self.proceedEnableBankInfo)
        try:
            click= button.is_enabled()
            if click==True:
                button.click()
                return True
        except:
            print("fill all remaining details")
            self.driver.find_element(*self.termsOfUseBankInfo).click()
            time.sleep(2)
            self.driver.find_element(*self.proceedEnableBankInfo).click()

    def verifyproceedclick(self):
        time.sleep(3)
        actionchains=ActionChains(self.driver)
        actionchains.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        self.driver.find_element(*self.termsOfUseBankInfo).click()
        self.driver.find_element(*self.crossbutton).click()
        button=self.driver.find_element(*self.proceedEnableBankInfo).click()


    def switchAccounttype(self):
        time.sleep(2)
        Business= self.driver.find_element(*self.changeAccount).text
        print(Business)
        time.sleep(3)
        self.driver.find_element(*self.changeAccount).click()
        return Business

    def switchAccountpersonal(self):
        time.sleep(2)
        Personal= self.driver.find_element(*self.changePersonal).text
        print(Personal)
        self.driver.find_element(*self.changePersonal).click()
        return Personal

    def EnterPersonalFirst(self,firstname):
        first = self.driver.find_element(*self.PersonalFirstName)
        first.send_keys(Keys.CONTROL + "a")
        first.send_keys(Keys.DELETE)
        first.send_keys(firstname)
        time.sleep(2)

    def EnterPersonalLast(self,Lastname):
        last = self.driver.find_element(*self.PersonalLastName)
        last.send_keys(Keys.CONTROL + "a")
        last.send_keys(Keys.DELETE)
        time.sleep(2)
        last.send_keys(Lastname)
        time.sleep(2)


    def EnterPersonalEmail(self,Email):
        time.sleep(2)
        email = self.driver.find_element(*self.PersonalEmail)
        email.send_keys(Keys.CONTROL + "a")
        email.send_keys(Keys.DELETE)
        email.send_keys(Email)
        time.sleep(2)

    def EnterPersonalPhone(self, Phone):
        time.sleep(2)
        phone = self.driver.find_element(*self.PersonalPhone)
        phone.send_keys(Keys.CONTROL + "a")
        phone.send_keys(Keys.DELETE)
        phone.send_keys(Phone)
        time.sleep(2)

    def Enabled_PersonalProceedbtn(self):
        proceed= self.driver.find_element(*self.PersonalProceedbtn)
        verify= proceed.is_enabled()
        return verify

    def ValidateEmail(self):
        proceed= self.driver.find_element(*self.PersonalProceedbtn).click()
        # verify= proceed.is_enabled()
        emailmsg=self.driver.find_element(*self.validateemail).text
        print(emailmsg)
        time.sleep(3)
        email = self.driver.find_element(*self.PersonalEmail)
        email.send_keys(Keys.CONTROL + "a")
        email.send_keys(Keys.DELETE)
        email.send_keys("xyz@domain.com")
        time.sleep(2)
        return emailmsg

    def ValidatePhone(self):
        self.driver.find_element(*self.PersonalProceedbtn).click()
        time.sleep(2)
        phone = self.driver.find_element(*self.PersonalPhone)
        phone.send_keys(Keys.CONTROL + "a")
        phone.send_keys(Keys.DELETE)
        phone.send_keys("6523456")
        time.sleep(3)
        button = self.driver.find_element(*self.phntextvalidation).text
        return button


    def ValidatePhone1(self):
        phone = self.driver.find_element(*self.PersonalPhone)
        phone.send_keys(Keys.CONTROL + "a")
        phone.send_keys(Keys.DELETE)
        phone.send_keys("7035896423")
        time.sleep(3)
        try:
            button = self.driver.find_element(*self.verifyphn)
            button2 = button.is_displayed()
            if button2==True:
                return True

        except:
            return False



    def verify_outertoken_vopay(self):
        time.sleep(15)
        # self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        get= self.driver.current_url
        print(get)
        time.sleep(3)
        self.driver.switch_to.default_content()
        time.sleep(2)
        getcountOR =self.driver.find_element(*self.tokenprint).text
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


    def EnterAddresss(self, address):
        text= self.driver.find_element(*self.Addaddressbtn).text
        print(text)
        self.driver.find_element(*self.Addaddressbtn).click()
        time.sleep(2)
        add = self.driver.find_element(*self.addresstext)
        add.send_keys(Keys.CONTROL + "a")
        add.send_keys(Keys.DELETE)
        value1 = add.send_keys(address)
        time.sleep(4)
        drp=self.driver.find_element(*self.addressselect).click()
        time.sleep(2)
        return text

    def CheckProvinceAvaiable(self):
        self.driver.find_element(*self.provincetext).click()
        text=self.driver.find_element(*self.provincelist).is_displayed()
        time.sleep(2)
        province= self.driver.find_element(*self.drpprovince).click()
        time.sleep(2)
        return text


    def adddressbtn_Editadddress(self):
        self.driver.find_element(*self.addaddressbtn).click()
        time.sleep(2)
        self.driver.find_element(*self.Editbtn).click()
        value= self.driver.find_element(*self.editaddresstext).text
        print(value)

    def ClickCancelRemove(self):
        time.sleep(2)
        self.driver.find_element(*self.cancelremovebtn).click()
        text= self.driver.find_element(*self.Addaddressbtn).text
        print(text)
        return text

    def EnterCompany(self,CompName):
        time.sleep(2)
        name=self.driver.find_element(*self.businessCompanyName)
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        name.send_keys(CompName)
        time.sleep(2)

    def BusinessFirst(self, busfirst, buslast):
        name= self.driver.find_element(*self.businessFirstName)
        name.send_keys(Keys.CONTROL + "a")
        name.send_keys(Keys.DELETE)
        name.send_keys(busfirst)
        time.sleep(3)
        name1= self.driver.find_element(*self.businessLastName)
        name1.send_keys(Keys.CONTROL + "a")
        name1.send_keys(Keys.DELETE)
        name1.send_keys(buslast)
        time.sleep(2)

    def ClickProcedBusiness(self):
        btn =self.driver.find_element(*self.businessproceedbtn)
        try:
            click= btn.is_enabled()
            if click==True:
                self.driver.find_element(*self.businessPhone).send_keys("1233455660")
                btn.click()
                return True
        except:
            print(" business proceed btn not enabled")
            return False
        self.driver.implicitly_wait(100)

    def loadurlouter(self):
        time.sleep(2)
        self.driver.get(self.URL)
        self.driver.implicitly_wait(150)


    def loadurljs(self):
        time.sleep(2)
        self.driver.get(self.jsurl)
        self.driver.implicitly_wait(150)


    def loadurlinner(self):
        time.sleep(2)
        self.driver.get(self.innerurl)
        self.driver.implicitly_wait(150)


    def switchwindow_JS(self):
        time.sleep(6)
        # self.driver.back()
        # self.driver.implicitly_wait(100)
        self.driver.switch_to.window(self.driver.window_handles[2])
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)



    def verify_Innertoken(self):
        time.sleep(10)
        # self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        get= self.driver.current_url
        print(get)
        url = str("https://vopay-testing.com/iframe/new/inner.html")
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        time.sleep(4)
        global  innertoken
        innertoken = self.driver.find_element(*self.tokenprint).text
        print(innertoken)
        if str(get) == str(url):
            return True
        else:
            return False

    def verify_Innertokenagain(self):
        time.sleep(10)
        # self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        get= self.driver.current_url
        print(get)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        time.sleep(4)
        getvalue = self.driver.find_element(*self.tokenprint).text
        value = str(print(getvalue))
        if value !="":
            return True
        else:
            return False


    def verify_JStoken_vopayurl(self):
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[2])
        frame= self.driver.find_element(*self.iframelink)
        self.driver.switch_to.frame(frame)
        time.sleep(3)
        html = self.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        text1= self.driver.find_element(*self.tokenprint).text
        print(text1)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(2)
        elem = self.driver.find_element_by_xpath('//input[@id="Token"]')
        value = self.driver.execute_script('return arguments[0].value;', elem)
        token = str(print("{}".format(value)))
        if token !="" and token != None:
            return True
        else:
            return False
        # new_caps = {}
        # new_caps["browserName"] = 'chrome',
        # new_caps["javascriptEnabled"] = True,
        # new_caps["acceptSslCerts"] = True
        #
        # d = DesiredCapabilities.CHROME
        # d['goog:loggingPrefs'] = {'browser': 'ALL'}
        # # d['loggingPrefs'] = {'browser': 'ALL'}
        # # driver = webdriver.Chrome(desired_capabilities=d)
        # time.sleep(3)
        # logs_1 = self.driver.get_log('browser')
        # print("A::", logs_1)
        # time.sleep(4)
        # for entry in self.driver.get_log('browser'):
        #     print(entry)
        # time.sleep(2)

    def JS_Bankvopayurl(self):
        time.sleep(2)
        elem = self.driver.find_element_by_xpath('//input[@id="BankId"]')
        value = self.driver.execute_script('return arguments[0].value;', elem)
        bank= str(print("{}".format(value)))
        if bank !="" and bank != None:
            return True
        else:
            return False

    def JS_AccountName_Vopayurl(self):
        time.sleep(2)
        elem = self.driver.find_element_by_xpath('//input[@id="AccountNumber"]')
        value = self.driver.execute_script('return arguments[0].value;', elem)
        Name= str(print("{}".format(value)))
        if Name !="" and Name != None:
            return True
        else:
            return False

    def JS_institution_vopayurl(self):
        time.sleep(2)
        elem = self.driver.find_element_by_xpath('//input[@id="Institution"]')
        value = self.driver.execute_script('return arguments[0].value;', elem)
        Name= str(print("{}".format(value)))
        if Name !="" and Name != None:
            if len(Name) != 0:
                print(Name)
                print(len(Name))
                print('Not empty String')
            return True
        else:
            return False


    def enterbank_cancel(self):
        time.sleep(2)
        ans= self.driver.find_element(*self.searchbar)
        ans.send_keys(Keys.CONTROL + "a")
        ans.send_keys(Keys.DELETE)
        time.sleep(2)
        ans.send_keys("Scotia")
        time.sleep(3)
        cross=self.driver.find_element(*self.cross)
        icon= cross.is_enabled()
        # cross.click()
        return icon