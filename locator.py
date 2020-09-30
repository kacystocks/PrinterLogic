###########################################
# Automated tests written for Printer Logic
# Login Page ##############################
# Kacy Stocks #############################
# 9/28-30/2020 ############################
###########################################
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, "admin-login-btn")
    LOST_PW = (By.ID, "forgot-password")

class LoggedInPageLocators(object):
    USER_MENU = (By.ID, "user-menu")
