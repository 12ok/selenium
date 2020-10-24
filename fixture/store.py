class StoreHelper:
    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def get_list_product(self):
        wd = self.app.wd
        return wd.find_elements_by_xpath("//div[@class='image-wrapper']")

    def get_count_sticker(self, element):
        return len(element.find_elements_by_xpath("./div[contains(@class, 'sticker')]"))
