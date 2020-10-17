class AdminHelper:
    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url+'admin/')

    def login(self):
        wd = self.app.wd
        wd.find_element_by_name("username").send_keys(self.app.user)
        wd.find_element_by_name("password").send_keys(self.app.password)
        wd.find_element_by_name("login").click()
