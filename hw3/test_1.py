import time
from testpage import OperationsHelper
import logging
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

def test_positive(browser):
    # Проверка алерта с валидными данными contact us
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_contact_link()
    time.sleep(2)

    testpage.enter_name_contact(testdata["contact_name"])
    testpage.enter_email_contact(testdata["contact_email"])
    testpage.enter_content_contact(testdata["contact_content"])
    testpage.click_contactus_button()
    time.sleep(2)
    assert testpage.get_allert_text() == "Form successfully submitted"

def test_neg1(browser):
    # Проверка алерта с пустыми полями contact us
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_contact_link()
    time.sleep(2)

    testpage.click_contactus_button()
    time.sleep(2)
    assert testpage.get_allert_text() != "Form successfully submitted"

def test_neg2(browser):
    # Проверка отправки формы с невалидными данными contact us
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_contact_link()
    time.sleep(2)

    testpage.enter_name_contact("test")
    testpage.enter_email_contact("test")
    testpage.enter_content_contact("test")
    testpage.click_contactus_button()
    time.sleep(1)
    email_label_color = testpage.get_email_label_color()
    assert email_label_color == 'rgba(183, 28, 28, 1)'