from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_example(app):
    app.wd.get("https://www.google.com/")
    app.wd.find_element_by_name("q").send_keys("selenium")
    app.wd.find_element_by_class_name("gNO89b").click()
    WebDriverWait(app.wd, 5).until(EC.title_is("selenium - Поиск в Google"))
