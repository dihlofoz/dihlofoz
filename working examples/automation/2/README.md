## Тестовые задания, оригинал - https://github.com/Hexlet/ru-test-assignments/blob/main/QA/Effective%20Mobile/README.md

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)
![Selenium](https://img.shields.io/badge/Selenium-white?style=for-the-badge&logo=selenium&logoColor=43B02A)

### Installing (For Ex. №1)
Run in cmd
```
pip install selenium
```
### About Ex №1
В данном упражнении мы создаём небольшой скрипт, который поможет проверить сценарий покупки товара на сайте saucedemo.com с использованием Python + Selenium

### Code
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

try:
    # Открываем одновременно и нужную страницу и окно входа в аккаунт
    browser = webdriver.Firefox()
    browser.get('https://www.saucedemo.com/')
    sleep(3)

    # Заходим в аккаунт
    username = browser.find_element(By.CSS_SELECTOR, 'input[id="user-name"]')
    password = browser.find_element(By.CSS_SELECTOR, 'input[id="password"]')

    username.send_keys('standard_user')
    password.send_keys('secret_sauce')
    sleep(3)

    login_button = browser.find_element(By.CSS_SELECTOR, 'input[id="login-button"]').click()
    sleep(3)

    # Добавляем товар в корзину
    shop_item = browser.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-backpack"]').click()
    sleep(3)

    # Переходим в корзину
    shopping_cart = browser.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()

    # Проверяем пустоту корзины
    checkout_empty_shop = browser.find_elements(By.CSS_SELECTOR, 'div[class="cart_item_label"]')
    if len(checkout_empty_shop) > 0:
        print('Контейнер с данным классом присутствует, продолжаем оформление.')
    else:
        raise Exception('Корзина пуста, дальнейшие шаги невозможны!')

    sleep(3)

    # Продолжаем оформление
    checkout_button = browser.find_element(By.CSS_SELECTOR, 'button[id="checkout"]').click()

    # Вводим данные о себе
    first_name = browser.find_element(By.CSS_SELECTOR, 'input[id="first-name"]')
    last_name = browser.find_element(By.CSS_SELECTOR, 'input[id="last-name"]')
    zip_code = browser.find_element(By.CSS_SELECTOR, 'input[id="postal-code"]')

    first_name.send_keys('Bob')
    last_name.send_keys('Big')
    zip_code.send_keys('10909')
    sleep(2)

    # Переход к следующему пункту
    continue_button = browser.find_element(By.CSS_SELECTOR, 'input[id="continue"]').click()
    sleep(2)

    # Завершаем покупку
    finish_button = browser.find_element(By.CSS_SELECTOR, 'button[id="finish"]').click()
    sleep(2)

    # Проверка успешного заказа
    checkout_success = browser.find_elements(By.CSS_SELECTOR, 'div[id="checkout_complete_container"]')
    if len(checkout_success) > 0:
        print('Поздравляю с заказом')
    else:
        raise Exception('Облажался дружок')
    sleep(3)

finally:
    # Закроем браузер
    browser.quit()
```

