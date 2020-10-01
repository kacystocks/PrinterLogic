###########################################
# Automated tests written for Printer Logic
# Login Page ##############################
# Kacy Stocks #############################
# 9/28-10/1/2020 ##########################
###########################################
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import page
from config import *

ChromeDriver = "C:\Program Files (x86)\chromedriver.exe"
PrinterLogicWebsite = "https://snowrentalstest.printercloud.com/admin/index.php"

class Test_Printer_Logic(unittest.TestCase):

    # runs before every test, opens the browser
    # and navigates to the website
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriver)
        self.driver.get(PrinterLogicWebsite)
    
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
        correct_login_result_page = page.TriggeredResults(self.driver)
        assert correct_login_result_page.correct_login_results()

    # test to ensure not logged in users cannot access acount content
    def test_not_logged_in(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_login_button()
        not_logged_in_change_security_settings = page.TriggeredResults(self.driver)
        assert not_logged_in_change_security_settings.fail_change_security()

    # test to ensure false information lost password does not work
    def test_false_lost_password(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_lost_password()
        mainPage.click_email()
        email = self.driver.find_element_by_id("email")
        email.send_keys(FAKEEMAIL)
        email.send_keys(Keys.RETURN)

        false_email_reset = page.TriggeredResults(self.driver)
        assert false_email_reset.fail_change_security()        

    # test to ensure privacy policy works
    def test_privacy_policy(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_privacy_policy()

        self.driver.switch_to.window(self.driver.window_handles[1])
    
        priv_page_loaded = page.TriggeredResults(self.driver)
        assert priv_page_loaded.privacy_policy_loads()

    # test to ensure ui widget overlay works properly
    # by testing that it adjusts height and covers whole screen
    # even when the screen size is changed
    def test_ui_overlay_covers_screen(self):
        dialog = self.driver.find_element_by_class_name("ui-widget-overlay")
        before = dialog.size
        self.driver.set_window_size(1920, 1080)
        after = dialog.size
        assert before != after

    # test to ensure ui dialog adjusts center when in logging in ? IT DOESN'T
    def test_ui_dialog_centered(self):
        dialog = self.driver.find_element_by_class_name("ui-dialog")
        before = dialog.location
        self.driver.set_window_size(1920, 1080)
        after = dialog.location
        assert before != after

    # runs after every test and quits the browser and pipe
    def tearDown(self):
        self.driver.quit()
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    # unittest.main()
