from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class loginpage:
    login_btn = "/html/body/div[1]/div/div/div[2]/div[6]/div/div/div[1]/div/a"
    email_btn = "//button[@id='loginWithEmail']"
    email_input = "//*[@id='email']"
    password_input = "//*[@id='password']"
    continue_btn = "//*[@id='continueEmail']"
    close_pop_up="// *[ @ id = 'Layer_1']"
    drop_down_icon = "/html/body/header/div/div/div[2]/div[3]"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_login_btn(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))
        login_button.click()

    def click_login_email(self):
        email_login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.email_btn)))
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", email_login_button)
        email_login_button.click()


    def input_email(self,email):
        email_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.email_input)))
        email_field.clear()
        email_field.send_keys("demoseller@droom.in")

    def input_password(self,password):
        password_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.password_input)))
        password_field.clear()
        password_field.send_keys("Droom@123")

    def click_continue_btn(self):
        continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue_btn)))
        continue_button.click()


    def click_cancel_btn(self):
        continue_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.close_pop_up)))
        continue_button.click()


    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.drop_down_icon).is_displayed()
        except:
            return False
