from selenium import webdriver

driver = webdriver.Chrome('./driver/chromedriver.exe')

driver.get('https://forms.gle/YYMczBF6x9MNWEP57')

name_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name_field.send_keys('Rajesh Berwal')

email_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_field.send_keys('irajeshberwal@gmail.com')

twitter_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
twitter_field.send_keys('imrajeshberwal')

comment_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
comment_field.send_keys('Just do it.')

btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
btn.click()