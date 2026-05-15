from selenium.webdriver.common.by import By
from .base_page import BasePage


class loginPage(BasePage):
    url = "https://parabank.parasoft.com/parabank/index.htm"
    userName_loc = (By.XPATH, "//input[@type='text']")
    password_loc = (By.XPATH, "//input[@type='password']")
    submit_loc = (By.XPATH, "//input[@type='submit']")
    conf_val = (By.XPATH, "//p[@class='smallText']")

    def load(self):
        self.open_main_page(self.url)

    def login(self, username: str, password: str):
        self.type(self.userName_loc,username)
        self.type(self.password_loc,password)
        self.click(self.submit_loc)
        testSuccess = self.get_text(self.conf_val)
        assert "ParaBank" in self.driver.title
        assert "overview" in self.driver.current_url
        assert "Welcome" in testSuccess
        return "Successfully login..."