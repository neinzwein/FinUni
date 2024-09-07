import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class MessengerTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8081/login")

    def test_successful_login(self):
        driver = self.driver
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "Password")
        login_button = driver.find_element(By.NAME, "login")

        username_field.send_keys("FirstName@gmail.com")
        password_field.send_keys("Password")
        login_button.click()

        logged_in_element = driver.find_element(By.ID, "loggedIn")
        self.assertIsNotNone(logged_in_element)

    def test_unsuccessful_login(self):
        driver = self.driver
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.NAME, "login")

        username_field.send_keys("invalidUsername")
        password_field.send_keys("invalidPassword")
        login_button.click()

        error_message = driver.find_element(By.ID, "errorMessage")
        self.assertIsNotNone(error_message)

    def test_send_message(self):
        driver = self.driver
        self.test_successful_login()

        message_field = driver.find_element(By.NAME, "message")
        send_button = driver.find_element(By.NAME, "Отправлять")

        message_field.send_keys("Hello, world!")
        send_button.click()

        chat_message = driver.find_element(By.XPATH, "//div[@class='chat-message' and text()='Hello, world!']")
        self.assertIsNotNone(chat_message)

    def test_send_empty_message(self):
        driver = self.driver
        self.test_successful_login() 

        message_field = driver.find_element(By.NAME, "message")
        send_button = driver.find_element(By.NAME, "Отправлять")

        message_field.send_keys("")
        send_button.click()

        error_message = driver.find_element(By.ID, "errorMessage")
        self.assertIsNotNone(error_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
