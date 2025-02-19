from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_add_to_basket_button(browser):
    browser.get(link)
    # time.sleep(10)

    buttons = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert len(buttons) > 0, "Кнопка добавления в корзину не найдена"
    assert len(buttons) == 1, "Найдено несколько кнопок добавления в корзину"