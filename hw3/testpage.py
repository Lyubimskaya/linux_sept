from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_BANNER = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_BLOG = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CREATE_POST_BTN = (By.CSS_SELECTOR, "#create-btn")
    LOCATOR_NEW_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_NEW_POST_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_NEW_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_NEW_POST_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_CREATED_POST_TITLE = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_DOWNLOAD_IMAGE = (By.XPATH, """//input[@type = 'file']""")
    LOCATOR_CONTACT_LINK = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACTUS_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACTUS_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACTUS_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACTUS_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")
    LOCATOR_CONTACTUS_LABEL_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/span""")



class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_banner = self.find_element(TestSearchLocators.LOCATOR_ERROR_BANNER, time=3)
        text = error_banner.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_BANNER[1]}")
        return text

    def get_blog_text(self):
        blog_text = self.find_element(TestSearchLocators.LOCATOR_BLOG)
        text = blog_text.text
        logging.info(f"We find text {text} in title site {TestSearchLocators.LOCATOR_BLOG[1]}")
        return text

    def click_create_post_button(self):
        logging.info("Click create post (+) button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def enter_title(self, post_title):
        logging.info(f"Send {post_title} to element {TestSearchLocators.LOCATOR_NEW_POST_TITLE[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_TITLE)
        title_field.send_keys(post_title)

    def enter_description(self, post_description):
        # logging.info()
        description_field = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_DESCRIPTION)
        description_field.send_keys(post_description)

    def enter_content(self, post_content):
        # logging.info()
        content_field = self.find_element(TestSearchLocators.LOCATOR_NEW_POST_CONTENT)
        content_field.send_keys(post_content)

    def click_save_button(self):
        # logging.info("Some text")
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_SAVE_BTN).click()

    def get_post_title(self):
        post_title = self.find_element(TestSearchLocators.LOCATOR_CREATED_POST_TITLE)
        text = post_title.text
        return text

    def download_image(self):
        download_img = self.find_element(TestSearchLocators.LOCATOR_DOWNLOAD_IMAGE)
        download_img.send_keys(r"C:\Users\Дмитрий\Desktop\2023-04-30_22-31-39.png")

    """
    Функции для работы с локаторами страницы /contact
    """
    def click_contact_link(self):
        logging.info('Click "contact" link')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_LINK).click()

    def enter_name_contact(self, contact_name):
        logging.info(f"Send {contact_name} to element {TestSearchLocators.LOCATOR_CONTACTUS_NAME_FIELD[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_CONTACTUS_NAME_FIELD)
        title_field.send_keys(contact_name)

    def enter_email_contact(self, contact_email):
        logging.info(f"Send {contact_email} to element {TestSearchLocators.LOCATOR_CONTACTUS_EMAIL_FIELD[1]}")
        description_field = self.find_element(TestSearchLocators.LOCATOR_CONTACTUS_EMAIL_FIELD)
        description_field.send_keys(contact_email)

    def enter_content_contact(self, contact_content):
        logging.info(f"Send {contact_content} to element {TestSearchLocators.LOCATOR_CONTACTUS_CONTENT_FIELD[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTACTUS_CONTENT_FIELD)
        content_field.send_keys(contact_content)

    def click_contactus_button(self):
        logging.info('Click "CONTACT US" button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACTUS_BTN).click()

    def get_allert_text(self):
        alert_text = self.switch_to_alert().text
        logging.info(f'We find text {alert_text} in title alert on site "Contact Us"')
        return alert_text

    def get_email_label_color(self):
        email_label_color = self.get_element_property(TestSearchLocators.LOCATOR_CONTACTUS_LABEL_EMAIL, "color")
        logging.info(f'We find err color label {email_label_color} when entered not valid email')
        return email_label_color