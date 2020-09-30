###########################################
# Automated tests written for Printer Logic
# Login Page ##############################
# Kacy Stocks #############################
# 9/28-30/2020 ############################
###########################################
from locator import *
from element import BasePageElement
from Config import *

class LostPasswordTextElement(BasePageElement):
    locator = "forgot-password"


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    username_text_element = LostPasswordTextElement()

    def is_title_matches(self):
        return "PrinterLogic" in self.driver.title

    def click_lost_password(self):
        element = self.driver.find_element(
            *MainPageLocators.LOST_PW)
        # print("clicking " + element.text)
        element.click()

    def click_login_button(self):
        element = self.driver.find_element(
            *MainPageLocators.GO_BUTTON)
        # print("clicking " + element.text)
        element.click()

    def click_username(self):
        element = self.driver.find_element(
            *LoggedInPageLocators.USER_MENU)
        # print("clicking " + element.text)
        element.click()


class TriggeredResults(BasePage):

    def pw_results_found(self):
        return "forgot-password-form" in self.driver.page_source

    def not_input_login_results(self):
        return "Please enter your username and password:" in self.driver.page_source

    def false_input_login_results(self):
        return USERNAME not in self.driver.page_source and FAKEUSERNAME not in self.driver.page_source

    def correct_login_results(self):
        return USERNAME in self.driver.page_source
