from Projects.Framework.Parabank.pages.OpenAccount_page import OpenAccountPage
from Projects.Framework.Parabank.pages.login_page import loginPage

def test_LoginPage(driver):
    login = loginPage(driver)
    login.load()
    result = login.login("pradeep143", "Pradeep@1999")
    print(result)
    openAccount = OpenAccountPage(driver)
    openAccount.open()
    print("Logout Successful")



