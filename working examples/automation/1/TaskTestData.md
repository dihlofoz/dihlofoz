```markdown
# Выполнение тестовой задачи взятой отсюда https://clck.ru/3NyX6V

## Ex №1
```

```python
import unittest

class DiscountCalculatorPage:
    def __init__(self):
        pass

    def calculate_discount(self, points):
        if points <= 100:
            return 1
        elif points <= 200:
            return 3
        elif points <= 500:
            return 5
        else:
            return 10


class TestDiscountCalculation(unittest.TestCase):
    def setUp(self):
        self.calculator = DiscountCalculatorPage()
    
    def test_zero_points(self):
        result = self.calculator.calculate_discount(0)
        self.assertEqual(result, 1)
    
    def test_fifty_points(self):
        result = self.calculator.calculate_discount(50)
        self.assertEqual(result, 1)
    
    def test_hundred_points(self):
        result = self.calculator.calculate_discount(100)
        self.assertEqual(result, 1)
    
    def test_one_hundred_and_one_points(self):
        result = self.calculator.calculate_discount(101)
        self.assertEqual(result, 3)
    
    def test_three_hundred_points(self):
        result = self.calculator.calculate_discount(300)
        self.assertEqual(result, 5)
    
    def test_five_hundred_and_one_points(self):
        result = self.calculator.calculate_discount(501)
        self.assertEqual(result, 10)
    
if __name__ == '__main__':
    unittest.main()
```
```markdown
## Ex №2
```

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Открываем одновременно и нужную страницу и окно входа в аккаунт
browser = webdriver.Firefox()
browser.get('https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1#login')
sleep(4)

# Заходим в аккаунт
login = browser.find_element(By.CSS_SELECTOR, 'input[data-marker="login-form/login/input"]')
password = browser.find_element(By.CSS_SELECTOR, 'input[data-marker="login-form/password/input"]')

# Подставить свои данные
login.send_keys('')
password.send_keys('')

log_in_button = browser.find_element(By.CSS_SELECTOR, 'button[data-marker="login-form/submit"]').click()

# Ввод капчи самостоятельно эх.....
sleep(30)

# Выбор первого попавшегося объявления
first_advert = browser.find_element(By.CSS_SELECTOR, 'a[class="iva-item-sliderLink-kra4e"]').click()
sleep(3)

# Покупаем с доставочкой
buy_with_del = browser.find_element(By.CSS_SELECTOR, 'button[class="QaQVm oPsQJ hWoW8 w5X9L"]').click()
sleep(3)

# Проверяем, пустое ли поле телефона
phone_field = browser.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
if phone_field.get_attribute('value').strip() == '':
    print("Поле 'Телефон' пустое.")
else:
    print(f"В поле 'Телефон' введены данные: {phone_field.get_attribute('value')}")

# Закроем браузер
browser.quit()
```