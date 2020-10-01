###########################################
# Automated tests written for Printer Logic
# Login Page ##############################
# Kacy Stocks #############################
# 9/28-30/2020 ############################
###########################################
from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):

    def __set__(self, obj, value):  # anytime we use this object- use this functionality
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))   # anonymous function, returns true or false
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))   # anonymous function, returns true or false
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
