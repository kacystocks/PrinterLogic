###########################################
# Automated tests written for Printer Logic
# Login Page ##############################
# Kacy Stocks #############################
# 9/28-10/1/2020 ##########################
###########################################
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, "admin-login-btn")
    LOST_PW = (By.ID, "forgot-password")
    EMAIL_FIELD = (By.ID, "email")
    PRIVACY_POLICY = (By.LINK_TEXT, "Privacy Policy")

class LoggedInPageLocators(object):
    pass
