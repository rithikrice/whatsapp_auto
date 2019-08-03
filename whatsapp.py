from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')
name = input('whom to send message??')
msg = input('Enter the message')
input2 = int(input('no.of times to send message'))

input('click any random key after scanning')

user = driver.find_element_by_class_name('X7YrQ')
user.click()

msgbox = driver.find_element_by_class_name('_3u328')

for i in range (input2):
    msgbox.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()