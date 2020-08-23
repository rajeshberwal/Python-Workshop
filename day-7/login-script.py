from selenium import webdriver
from getpass import getpass

username = input('username: ')
passwd = getpass('password: ')

driver = webdriver.Chrome('./driver/chromedriver.exe')

driver.get('https://www.codechef.com/')


usr_field = driver.find_element_by_xpath('//*[@id="edit-name"]')
usr_field.send_keys(username)

pass_field = driver.find_element_by_xpath('//*[@id="edit-pass"]')
pass_field.send_keys(passwd)

btn = driver.find_element_by_xpath('//*[@id="edit-submit"]')
btn.click()
