from selenium import webdriver

from fixture.admin import AdminHelper


class Application:

    def __init__(self, base_url, user, password):
        self.wd = webdriver.Chrome()
        self.base_url = base_url
        self.user = user
        self.password = password
        self.admin = AdminHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
