```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def initialize_driver():
    return webdriver.Chrome()

def wait_for_element(driver, locator_type, locator_value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((locator_type, locator_value))
    )

def get_user_input():
    name = input('Whom to send message? ')
    msg = input('Enter the message: ')
    while True:
        try:
            input2 = int(input('No. of times to send message: '))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return name, msg, input2

def send_whatsapp_message(driver, name, msg, count):
    try:
        search_box = wait_for_element(driver, By.CLASS_NAME, '_13NKt')
        search_box.send_keys(name)
        
        user_element = wait_for_element(driver, By.XPATH, f"//span[@title='{name}']")
        user_element.click()

        msg_box = wait_for_element(driver, By.CLASS_NAME, '_13NKt')

        for _ in range(count):
            msg_box.send_keys(msg)
            send_button = wait_for_element(driver, By.XPATH, "//span[@data-testid='send']")
            send_button.click()

    except NoSuchElementException:
        print("Element not found. Check the name or your internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    driver = initialize_driver()
    driver.get('https://web.whatsapp.com/')
    input('Click any random key after scanning QR code: ')
    name, msg, count = get_user_input()
    send_whatsapp_message(driver, name, msg, count)
    driver.quit()

if __name__ == "__main__":
    main()
```
