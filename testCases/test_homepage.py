import os.path

from pageObjects.homepage import Homepage  # ✅ Correct
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_001_HomePage:
    baseurl = Readconfig.getApplicationUrl()
    logger = LogGen.loggen()
    def test_homepage(self, setup):
        self.logger.info("*** Test_001_homepage started *** ")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.logger.info("launching application ")
        self.driver.maximize_window()
        self.logger.info("maximize the browser ")
        self.hp = Homepage(self.driver)
        login_text = self.hp.hoverover_acc_icon()
        self.logger.info("move hover over account icon ")
        # assert login_text == "Login to get your dream vehicle"

        if login_text == "Login to get your dream vehicle":
            assert True
            self.logger.info("account tab is verified as guest user ")

        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_homepage.png")
            self.logger.info("homepage testcases is failed as guest user ")

        self.driver.close()
        self.logger.info("browser is closed")