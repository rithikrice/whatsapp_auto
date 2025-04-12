```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def initialize_driver():
    return webdriver.Chrome()

def get_user_inputs():
    name = input('Whom to send message to? ')
    msg = input('Enter the message: ')
    while True:
        try:
            input2 = int(input('Number of times to send message: '))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return name, msg, input2

def scan_qr_code():
    input('Click any random key after scanning QR code: ')

def find_user_and_send_message(driver, name, msg, input2):
    try:
        user = driver.find_element(By.CLASS_NAME, 'X7YrQ')
        user.click()
        msgbox = driver.find_element(By.CLASS_NAME, '_3u328')
        for i in range(input2):
            msgbox.send_keys(msg)
            button = driver.find_element(By.CLASS_NAME, '_3M-N-')
            button.click()
    except NoSuchElementException:
        print("Element not found. Check class names and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    driver = initialize_driver()
    driver.get('https://web.whatsapp.com/')
    name, msg, input2 = get_user_inputs()
    scan_qr_code()
    find_user_and_send_message(driver, name, msg, input2)
    driver.quit()

if __name__ == "__main__":
    main()

```
