###########################################
# Automated tests written for Printer Logic
# Login Page ##############################
# Kacy Stocks #############################
# 9/28-10/1/2020 ##########################
###########################################
from locator import *
from element import BasePageElement
from config import *

class LostPasswordTextElement(BasePageElement):
    locator = "forgot-password"

class UsernamePassword(BasePageElement):
    locator = "Please enter your username and password:"

class UserMenu(BasePageElement):
    locator = "user-menu"

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):


    def is_title_matches(self):
        return "PrinterLogic" in self.driver.title

    def click_lost_password(self):
        element = self.driver.find_element(
            *MainPageLocators.LOST_PW)
        element.click()

    def click_login_button(self):
        element = self.driver.find_element(
            *MainPageLocators.GO_BUTTON)
        element.click()

    def click_email(self):
        element = self.driver.find_element(
            *MainPageLocators.EMAIL_FIELD)
        element.click()

    def click_privacy_policy(self):
        element = self.driver.find_element(
            *MainPageLocators.PRIVACY_POLICY)
        element.click()

class TriggeredResults(BasePage):

    def pw_results_found(self):
        return "forgot-password-form" in self.driver.page_source

    def not_input_login_results(self):
        return UsernamePassword.locator in self.driver.page_source

    def false_input_login_results(self):
        return USERNAME not in self.driver.page_source and FAKEUSERNAME not in self.driver.page_source

    def correct_login_results(self):
        return UserMenu.locator in self.driver.page_source

    def fail_change_security(self):
        return "Security" not in self.driver.page_source

    def fail_reset_false_email(self):
        return "We can't find a user with that email address." in self.driver.page_source

    def privacy_policy_loads(self):
        return "PrinterLogic takes data privacy seriously and is committed to managing your personal data" in self.driver.page_source
