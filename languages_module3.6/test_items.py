from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
button_locator = (By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")


def test_button_availability(browser):
    browser.get(link)
    # time.sleep(30)
    buttons = browser.find_elements(*button_locator)
    assert len(buttons) > 0 and buttons[0].is_enabled(), "The item on the locator [%s] is not available" % str(button_locator)
