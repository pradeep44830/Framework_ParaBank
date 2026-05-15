from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # To open the link
    def open_main_page(self, url : str):
        self.driver.get(url)

    # call type function anywhere when there is send key need to perform
    def type(self, location: tuple, text : str):
        element = self.driver.find_element(*location)
        element.send_keys(text)

    def alert(self):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        print("Alert text:", alert.text)
        alert.accept()

    # Where evere there an click opertaion
    def click(self, locator: tuple):
        self.driver.find_element(*locator).click()

    def get_text(self, locator: tuple):
        txt = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(locator))
        return txt.text

    def select_dropdown_by_text(self, location, text):
        dropdown = Select(self.driver.find_element(*location))
        dropdown.select_by_visible_text(text)

    def logout(self, locator):
        self.driver.find_element(*locator).click()

