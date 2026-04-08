import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep




class TestSignInModal(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity"
    modal_xpath = "//app-auth-modal"
    def setUp(self):

        oprions = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=oprions)
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_open_login_modal(self):
        sign_in_selector = ".header_navigation-menu-right-list > .header_sign-in-link"
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, sign_in_selector)
        sign_in_button.click()
        modal = self.driver.find_element(By.XPATH, self.modal_xpath)
        self.assertTrue(modal.is_displayed(), "Login modal is not displayed")


    def test_email_validation(self):
        sign_in_selector = ".header_navigation-menu-right-list > .header_sign-in-link"
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, sign_in_selector)
        sign_in_button.click()
        modal = self.driver.find_element(By.XPATH, self.modal_xpath)
        self.assertTrue(modal.is_displayed(), "Login modal is not displayed")
        email_input = self.driver.find_element(By.ID, "email")
        self.assertTrue(email_input.is_displayed(), "Email input is not displayed")
        email_error_message_id = "email-err-msg"
        email_error = self.driver.find_element(By.ID, email_error_message_id)
        self.assertFalse(email_error.is_displayed(), "Email error message is not displayed")
        email_input.send_keys("invalid-email")
        email_error = self.driver.find_element(By.ID, email_error_message_id)
        self.assertTrue(email_error.is_displayed(), "Email error message is not displayed")
        sleep(3)



if __name__ == "__main__":
    unittest.main()