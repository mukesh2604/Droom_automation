from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage:
    account_icon = "/html/body/div[1]/div/div/div[2]/div[6]/div/img"  # Replace with appropriate attribute
    login_tab = "//span[text()='Login to get your dream vehicle']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def hoverover_acc_icon(self):
        # Wait for account icon to be visible
        hover_account_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.account_icon))
        )

        # Hover over the account icon
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_account_element).perform()

        # Wait for the login tab to appear after hover
        login_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.login_tab))
        )

        return login_element.text
