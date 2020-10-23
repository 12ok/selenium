from selenium.common.exceptions import NoSuchElementException


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def is_displayed(self, xpath_element):
        wd = self.app.wd
        try:
            wd.find_element_by_xpath(xpath_element)
            return True
        except NoSuchElementException:
            return False
