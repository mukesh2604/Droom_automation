from pageObjects.homepage import Homepage
from pageObjects.loginpage import loginpage
from pageObjects.storemanagerpage import storemanagerpage
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig


class Test_003_storemanager:
    baseurl = Readconfig.getApplicationUrl()
    email_id = Readconfig.getEmailId()
    password= Readconfig.getpassword()
    logger = LogGen.loggen()

    def test_storemanager(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.hp =Homepage(self.driver)
        self.lp = loginpage(self.driver)
        self.sp = storemanagerpage(self.driver)

        self.hp.hoverover_acc_icon()
        self.lp.click_login_btn()
        self.lp.click_cancel_btn()
        self.lp.click_login_email()
        self.lp.input_email(self.email_id)
        self.lp.input_password(self.password)
        self.lp.click_continue_btn()


        if self.sp.verify_email_id() == "demoseller@droom.in":
            print("pass")
        else:
            print("fail")

        self.sp.click_icon_tab()
        self.sp.click_icon_dropdown()
        self.sp.click_logout()





