from selenium.webdriver.common.by import By

link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    button=browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")

    assert button, 'basket button not found'
