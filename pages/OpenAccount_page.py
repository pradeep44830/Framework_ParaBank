from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Projects.Framework.Parabank.pages.base_page import BasePage


class OpenAccountPage(BasePage):
    open_acc_loc = (By.PARTIAL_LINK_TEXT,"New Account")
    page_val_loc = (By.XPATH, "//h1[@class='title']")
    acc_type_loc = (By.ID, "type")
    acc_no_loc = (By.XPATH, "//select[@id='fromAccountId']")
    submit_loc = (By.XPATH, "//input[@type='button']")
    result_loc = (By.XPATH, "//div[@id='openAccountResult']/p")
    Acc_no_loc = (By.CSS_SELECTOR, "#newAccountId")
    logout_loc = (By.LINK_TEXT,"Log Out")

    def open(self):
        self.click(self.open_acc_loc)
        assert "New Account" in self.get_text(self.page_val_loc)
        self.select_dropdown_by_text(self.acc_type_loc, "SAVINGS")
        self.click(self.submit_loc)
        print(self.get_text(self.result_loc))
        print("Account No: ",self.get_text(self.Acc_no_loc))

