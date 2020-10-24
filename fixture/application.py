from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from fixture.admin import AdminHelper
from fixture.session import SessionHelper
from fixture.store import StoreHelper


class Application:

    def __init__(self, browser, base_url, user, password):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "opera":
            self.wd = webdriver.Opera()
        self.wait = WebDriverWait(self.wd, 10)
        self.base_url = base_url
        self.user = user
        self.password = password
        self.admin = AdminHelper(self)
        self.session = SessionHelper(self)
        self.store = StoreHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
