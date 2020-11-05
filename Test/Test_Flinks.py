import time
import allure
from Vopay_pages import iframe
from Vopay_pages.Flinkspages import Flinkspages
from Vopay_pages.Iframe1 import Iframe1
from Vopay_pages.VisaPage import VisaPage
from Vopay_pages.iframe import Iframe
from resources.variables import *
from selenium import webdriver

"""Vopay Iframe"""

"""Outer Html page"""

@allure.suite('Vopay Iframe')
@allure.title('Launch vopay iframe outer page(Vopay Outer)')
def test_cases_VopayOuterfirefox(browser1):
    global launch
    launch= Iframe1(browser1)
    launch.browser_load()
    launch.switchtoiframe()
#
# @allure.suite('Vopay Iframe')
# @allure.title('To loadmore banks and get counts of all bank(Vopay Outer)')
# def test_countbank_VopayOuter(browser):
#     assert launch.verify_loadMore()==False,"Proceed not displayed"
#     launch.showall_banklist()

@allure.suite('Vopay Iframe')
@allure.title('User is able to search and select bank(Vopay Outer)')
def test_selectbank_VopayOuter1(browser1):
    global launch1
    launch1 = Flinkspages(browser1)
    launch.searchBank(bankName)
    # assert launch1.selectBankClick()==True,"bank not displayed"
