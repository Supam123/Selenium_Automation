from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'C:\Users\supam\Desktop\Automate\chromedriver.exe')
driver.get('https://www.messenger.com/t/2051580281603511')
time.sleep(2)

#********** LOG IN *************

username = driver.find_element_by_xpath("//*[@id='email']")
password = driver.find_element_by_xpath("//*[@id='pass']")

username.send_keys('#################') # Enter Your Username 
password.send_keys('#################') # Facebook Password
time.sleep(2)

submit = driver.find_element_by_xpath("//*[@id='loginbutton']").click()
time.sleep(4)
driver.get('https://www.messenger.com/t/100001938212952') # friend you wanna text to
time.sleep(4)

for i in range(0,2):
        textbox = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div')
        textbox.send_keys('test')
        send = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div")
        send.click()
