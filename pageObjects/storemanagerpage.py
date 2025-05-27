from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class storemanagerpage:
    email_id="/html/body/header/div/div/div[2]/div[2]/div/p"
    close_tab="//*[@id='chairmanclubEntryModal']/div/div/div/button/span"
    close_addreach_tab="//*[@id='AdReachEntryModal']/div/div/div[1]/button"
    profile_icon_dropdown ="/html/body/header/div/div/div[2]/div[3]"
    drop_down_option = "/html/body/header/div/div/div[2]/div[3]/ul"
    logout="//*[@id='logoutUser']"
    chairmanclub="//*[@id='AdReachEntryModal']/div/div"
    adreach="//*[@id='chairmanclubEntryModal']/div/div"

    def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)
            # add more initialization if needed

    def verify_email_id(self):
        # Wait for the element that contains the store manager title
        email_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.email_id)))

        # Get and return the title text
        return email_element.text

    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException

    def close_icon_tab(self):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.chairmanclub)))
            dropdown_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.close_tab)))
            dropdown_element.click()
        except Exception as e:
            print(f"Failed to click dropdown icon: {e}")

    def close_addreach_icon(self):
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.adreach)))
            dropdown_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.close_addreach_tab)))
            dropdown_element.click()
        except Exception as e:
            print(f"Failed to click dropdown icon: {e}")

    def click_icon_dropdown(self):
        dropdown_element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.profile_icon_dropdown))
        )
        dropdown_element.click()

    def click_logout(self):
        # Wait until the dropdown logout option is visible
        logout_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.logout))
        )

        # Scroll it into view (in case it’s off-screen)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_element)

        # Click using JavaScript (in case normal click fails)
        self.driver.execute_script("arguments[0].click();", logout_element)

    #
    #
    # def __init__(self, driver):
    #     self.driver = driver
    #     self.wait = WebDriverWait(driver, 10)
    #
    # def click_login_btn(self):
    #     login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))
    #     login_button.click()
    #
    # def click_login_email(self):
    #     email_login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.email_btn)))
    #     # self.driver.execute_script("arguments[0].scrollIntoView(true);", email_login_button)
    #     email_login_button.click()
    #
    #
    # def input_email(self):
    #     email_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.email_input)))
    #     email_field.clear()
    #     email_field.send_keys("demoseller@droom.in")
    #
    # def input_password(self):
    #     password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.password_input)))
    #     password_field.clear()
    #     password_field.send_keys("Droom@123")
    #
    # def click_continue_btn(self):
    #     continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))
    #     continue_button.click()
    #
    #
    # def click_cancel_btn(self):
    #     continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.close_pop_up)))
    #     continue_button.click()
