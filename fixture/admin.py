from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AdminHelper:
    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url+'admin/')

    def open_page(self, page):
        wd = self.app.wd
        wd.get(page)

    def login(self):
        wd = self.app.wd
        wait = self.app.wait
        wd.find_element_by_name("username").send_keys(self.app.user)
        wd.find_element_by_name("password").send_keys(self.app.password)
        wd.find_element_by_name("login").click()
        wait.until(EC.presence_of_element_located((By.ID, "box-apps-menu-wrapper")))

    def click_menu(self, text):
        wd = self.app.wd
        wait = self.app.wait
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='%s']" % text)))
        wd.find_element_by_xpath("//span[text()='%s']" % text).click()

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

    def get_list_countries(self):
        wd = self.app.wd
        wait = self.app.wait
        wait.until(EC.visibility_of_element_located((By.NAME, 'countries_form')))
        list = []
        for i in wd.find_elements_by_xpath("//tr[@class='row']/td[5]/a"):
            list.append(i.text)
        return list

    def get_list_countries_with_zone(self):
        wd = self.app.wd
        wait = self.app.wait
        wait.until(EC.visibility_of_element_located((By.NAME, 'countries_form')))
        list = {}
        for i in wd.find_elements_by_xpath("//tr[@class='row']"):
            country = i.find_element_by_xpath("./td[5]/a").get_attribute("href")
            zone = int(i.find_element_by_xpath("./td[6]").text)
            if zone > 0:
                list[country] = zone
        return list

    def get_list_zone(self):
        wd = self.app.wd
        list = []
        for i in wd.find_elements_by_xpath("//table[@class='dataTable']//td[3]/input[not(@name='zone[name]')]"):
            list.append(i.get_attribute('value'))
        return list

    def get_country_from_geo_zone(self):
        wd = self.app.wd
        return wd.find_elements_by_xpath("//tr[@class='row']/td[3]/a")

    def get_zone_from_geo_zone(self):
        wd = self.app.wd
        list = []
        for i in wd.find_elements_by_xpath("//td/select[contains(@name, 'zone_code')]/option[@selected]"):
            list.append(i.text)
        return list