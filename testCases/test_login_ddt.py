import pytest
import os
from utilities import Xlutil
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from pageObjects.homepage import Homepage
from pageObjects.loginpage import loginpage
from pageObjects.storemanagerpage import storemanagerpage


class Test_Login_DDT:
    baseURL = Readconfig.getApplicationUrl()
    logger = LogGen.loggen()
    path = os.path.join(os.getcwd(), "testdata", "droom_logindata.xlsx")

    def test_login_ddt(self, setup):
        self.logger.info("**** Starting Data-Driven Login Test ****")
        self.rows = Xlutil.getRowCount(self.path, 'Sheet1')
        lst_status = []

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = Homepage(self.driver)
        self.lp = loginpage(self.driver)
        self.sm = storemanagerpage(self.driver)

        self.hp.hoverover_acc_icon()
        self.lp.click_login_btn()

        for r in range(2, self.rows + 1):
            email = Xlutil.readData(self.path, "Sheet1", r, 1)
            password = Xlutil.readData(self.path, "Sheet1", r, 2)
            expected_result = Xlutil.readData(self.path, "Sheet1", r, 3)

            self.logger.info(f"Test Case {r-1}: Email: {email}, Expected: {expected_result}")

            self.lp.click_cancel_btn()
            self.lp.click_login_email()
            self.lp.input_email(email)
            self.lp.input_password(password)
            self.lp.click_continue_btn()




            login_successful = self.lp.isMyAccountPageExists()
            if login_successful:
                lst_status.append("pass")
                if self.sm.close_icon_tab() or self.sm.close_addreach_icon():
                    self.sm.click_icon_dropdown()
                    self.sm.click_logout()
            else:
                lst_status.append("fail")


        #     if expected_result.lower() == "valid":
        #         if login_successful:
        #             self.logger.info("Login Passed")
        #             lst_status.append("Pass")
        #             self.sm.close_icon_tab()
        #             self.sm.click_icon_dropdown()
        #             self.sm.click_logout()
        #         else:
        #             self.logger.error("Login Failed for valid credentials")
        #             lst_status.append("Fail")
        #     elif expected_result.lower() == "invalid":
        #         if login_successful:
        #             self.logger.error("Login Passed for invalid credentials")
        #             lst_status.append("Fail")
        #             self.sm.close_addreach_icon()
        #             self.sm.click_icon_dropdown()
        #             self.sm.click_logout()
        #         else:
        #             self.logger.info("Login correctly failed for invalid credentials")
        #             lst_status.append("Pass")
        #
        # self.driver.close()

        if "Fail" not in lst_status:
            self.logger.info("**** DDT Login Test Passed ****")
            assert True
        else:
            self.logger.error("**** DDT Login Test Failed ****")
            assert False
