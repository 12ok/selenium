from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AdminHelper:
    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url+'admin/')

    def login(self):
        wd = self.app.wd
        wait = self.app.wait
        wd.find_element_by_name("username").send_keys(self.app.user)
        wd.find_element_by_name("password").send_keys(self.app.password)
        wd.find_element_by_name("login").click()
        wait.until(EC.presence_of_element_located((By.ID, "box-apps-menu-wrapper")))

    def get_main_menu(self):
        wd = self.app.wd
        wait = self.app.wait
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@id='app-']")))
        return wd.find_elements_by_xpath("//li[@id='app-']")

    def get_selected_menu(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//li[@id='app-' and @class='selected']")

    def get_not_selected_podmenu(self):
        wd = self.app.wd
        element = self.get_selected_menu()
        return element.find_elements_by_xpath(".//li[not (@class='selected')]")
