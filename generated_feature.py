```python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_whatsapp_message(name, msg, count):
    try:
        driver = webdriver.Chrome()
        driver.get('https://web.whatsapp.com/')
        input("Click any random key after scanning QR code...")

        user_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'X7YrQ')))
        user_element.click()

        msgbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, '_3u328')))

        for _ in range(count):
            msgbox.send_keys(msg)
            send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '_3M-N-')))
            send_button.click()

    except NoSuchElementException as e:
        print(f"Element not found: {e}")
    except ElementClickInterceptedException as e:
        print(f"Element click intercepted: {e}")
    except ElementNotInteractableException as e:
        print(f"Element not interactable: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()


if __name__ == "__main__":
    try:
        name = input('Whom to send message to? ')
        msg = input('Enter the message: ')
        count = int(input('Number of times to send message: '))
        send_whatsapp_message(name, msg, count)
    except ValueError:
        print("Invalid input. Please enter a valid number for the message count.")
    except KeyboardInterrupt:
        print("Operation interrupted by user.")

```
