from selenium.webdriver.common.by import By
from hrmhelper.selenium_helper import Selenium_Helper

class LoginPage(Selenium_Helper):

    email_ele = (By.XPATH, "//input[@name='username']")
    password_ele = (By.XPATH, "//input[@name='password']")
    login_ele = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, Username, Password):
        """Login to the application."""
        self.webelement_enter(self.email_ele, Username)
        self.webelement_enter(self.password_ele, Password)
        self.webelement_click(self.login_ele)