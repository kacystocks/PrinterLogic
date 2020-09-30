###########################################
# Automated tests written for Printer Logic
# Login Page ##############################
# Kacy Stocks #############################
# 9/28-30/2020 ############################
###########################################
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import page
from Config import *

# main for the login page - this should show number of tests failed
# and output those test results to the user
class Test_Printer_Logic(unittest.TestCase):

    # def test_search_python(self):
    #     mainPage = page.MainPage(self.driver)
    #     assert mainPage.is_title_matches()
    #     mainPage.search_text_element = "pycon"
    #     mainPage.click_go_button()
    #     search_result_page = page.SearchResultPage(self.driver)
    #     assert search_result_page.is_results_found()

    def setUp(self):
        self.driver = webdriver.Chrome(
            "C:\Program Files (x86)\chromedriver.exe")
        self.driver.get(
            "https://snowrentalstest.printercloud.com/admin/index.php")
        
    # test to ensure that the page loads properly
    def test_pl_page_loads(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_lost_password()
        lost_pw_result_page = page.TriggeredResults(self.driver)
        assert lost_pw_result_page.pw_results_found()

    # text to ensure Log in attempt without username and password shows warning
    def test_no_username_or_password(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_login_button()
        false_login_result_page = page.TriggeredResults(self.driver)
        assert false_login_result_page.not_input_login_results()

    # test to ensure enter login failure on wrong password
    def test_login_false_password_fail_enter(self):
        username = self.driver.find_element_by_id("relogin_user")
        password = self.driver.find_element_by_id("relogin_password")
        username.send_keys(USERNAME)
        password.send_keys(FAKEPASSWORD)
        password.send_keys(Keys.RETURN)
        false_login_result_page = page.TriggeredResults(self.driver)
        assert false_login_result_page.false_input_login_results()
    
    # test to ensure submit login failure on wrong password
    def test_login_false_password_fail_submit(self):
        username = self.driver.find_element_by_id("relogin_user")
        password = self.driver.find_element_by_id("relogin_password")
        username.send_keys(USERNAME)
        password.send_keys(FAKEPASSWORD)
        mainPage = page.MainPage(self.driver)
        mainPage.click_login_button()
        false_login_result_page = page.TriggeredResults(self.driver)
        assert false_login_result_page.false_input_login_results()

    # test to ensure login failure on wrong username
    def test_login_false_username_fail(self):
        username = self.driver.find_element_by_id("relogin_user")
        password = self.driver.find_element_by_id("relogin_password")
        username.send_keys(FAKEUSERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.RETURN)
        false_login_result_page = page.TriggeredResults(self.driver)
        assert false_login_result_page.false_input_login_results()

    # test to ensure login success
    def test_login_success(self):
        username = self.driver.find_element_by_id("relogin_user")
        password = self.driver.find_element_by_id("relogin_password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)        
        mainPage = page.MainPage(self.driver)
        mainPage.click_login_button()

        WebDriverWait(self.driver, 100).until(
            lambda driver: driver.find_element_by_link_text("My Company"))
        correct_login_result_page = page.TriggeredResults(self.driver)
        assert correct_login_result_page.correct_login_results()

    # # test to ensure not logged in users cannot access acount
    # def test_not_logged_in(self):
    #     pass

    # # test to ensure false information lost password does not work
    # def test_false_lost_password(self):
    #     pass

    # # test to ensure lost password works
    # def test_lost_password(self):
    #     forgot_password = driver.find_element_by_id(
    #         "forgot-password")
    #     pass

    # # test to ensure privacy policy works
    # def test_privacy_policy(self):
    #     privacy_policy_container = driver.find_element_by_id(
    #         "privacy-policy-container")
    #     pass

    # # test to ensure ui widget overlay works properly
    # # by testing that it adjusts height and covers whole screen
    # def test_ui_overlay_covers_screen(self):
    #     pass

    # # test to ensure user cannot access search without being logged in
    # def test_ui_false_user_cannot_search(self):
    #     pass

    # # test to ensure ui dialog adjusts center when in logging in ????? IT DOESN'T
    # def test_ui_dialog_centered(self):
    #     pass

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
