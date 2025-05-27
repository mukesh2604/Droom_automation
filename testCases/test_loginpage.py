from pageObjects.homepage import Homepage
from pageObjects.loginpage import loginpage
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig


class Test_001_LoginPage:
    baseurl = Readconfig.getApplicationUrl()
    email_id = Readconfig.getEmailId()
    password= Readconfig.getpassword()
    logger = LogGen.loggen()

    def test_loginpage(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.hp =Homepage(self.driver)
        self.hp.hoverover_acc_icon()
        self.lp=loginpage(self.driver)
        self.lp.click_login_btn()
        self.lp.click_cancel_btn()
        self.lp.click_login_email()
        self.lp.input_email()
        self.lp.input_password()
        self.lp.click_continue_btn()


