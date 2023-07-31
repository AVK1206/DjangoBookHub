import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/"
        self.driver = webdriver.Chrome()

    def test_valid_login(self):
        self.driver.get(self.base_url)
        time.sleep(2)
        login_button = self.driver.find_element(By.ID, "login_button")
        login_button.click()
        time.sleep(5)
        useremail_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        useremail_input.send_keys("some_email")
        password_input.send_keys("some_password")
        time.sleep(5)
        submit_button.click()

        self.assertTrue(
            self.driver.current_url.endswith("main/"))

        time.sleep(5)
        book_app_button = self.driver.find_element(By.NAME, "book")
        book_app_button.click()
        time.sleep(5)
        book_create_button = self.driver.find_element(By.NAME, "create_book")
        book_create_button.click()
        time.sleep(2)

        name_input = self.driver.find_element(By.NAME, "name")
        description_input = self.driver.find_element(By.NAME, "description")

        name_input.send_keys("Selenium")
        description_input.send_keys("Selenium")

        time.sleep(5)

        create_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        create_button.click()
        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        book_list_button = self.driver.find_element(By.NAME, "book_list")
        book_list_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        book_find_by_name_button = self.driver.find_element(By.NAME, "books_by_name")
        book_find_by_name_button.click()

        time.sleep(5)

        book_name_input = self.driver.find_element(By.NAME, "book_name")
        book_name_input.send_keys("test7")

        time.sleep(5)

        search_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()
        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        book_find_by_author_button = self.driver.find_element(By.NAME, "books_by_author")
        book_find_by_author_button.click()

        time.sleep(5)

        author_input = self.driver.find_element(By.NAME, "book_author")
        author_input.send_keys("An")

        search_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        book_find_by_count_button = self.driver.find_element(By.NAME, "books_by_count")
        book_find_by_count_button.click()

        time.sleep(5)

        count_input = self.driver.find_element(By.NAME, "book_count")
        count_input.send_keys("2")

        time.sleep(5)

        search_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)
        author_app_button = self.driver.find_element(By.NAME, "author")
        author_app_button.click()

        time.sleep(5)

        author_add_button = self.driver.find_element(By.NAME, "author_add")
        author_add_button.click()

        time.sleep(5)

        name_input = self.driver.find_element(By.NAME, "name")
        surname_input = self.driver.find_element(By.NAME, "surname")
        patronymic_input = self.driver.find_element(By.NAME, "patronymic")

        name_input.send_keys("John")
        surname_input.send_keys("Wick")
        patronymic_input.send_keys("John")

        time.sleep(5)

        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        authors_list_button = self.driver.find_element(By.NAME, "author_list")
        authors_list_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)
        order_button = self.driver.find_element(By.NAME, "order")
        order_button.click()

        time.sleep(5)

        order_create_button = self.driver.find_element(By.NAME, "order_create")
        order_create_button.click()

        time.sleep(5)

        show_orders_button = self.driver.find_element(By.NAME, "show_orders")
        show_orders_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        back_button = self.driver.find_element(By.CLASS_NAME, "back-button")
        back_button.click()

        time.sleep(5)

        logout_button = self.driver.find_element(By.LINK_TEXT, "Logout")
        logout_button.click()
        time.sleep(5)

        self.assertTrue(self.driver.current_url.endswith(
            "user/login/"))

    def test_invalid_login(self):
        self.driver.get(self.base_url)
        time.sleep(5)
        login_button = self.driver.find_element(By.ID, "login_button")
        login_button.click()
        time.sleep(5)

        useremail_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        submit_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        useremail_input.send_keys("knight@k.com")
        password_input.send_keys("knight12")

        time.sleep(5)
        submit_button.click()
        error_message = self.driver.find_element(By.CSS_SELECTOR, ".error-message").text
        self.assertEqual(error_message,
                         "You must input valid credentials!")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
