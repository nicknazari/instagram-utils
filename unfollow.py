#!/usr/bin/env python3
import time
import login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

numToRemove = 11 
# max num to remove is 11 right now, will debug later

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(2)

username = login.username
password = login.password 

usernamebox = driver.find_element_by_name("username")
passwordbox = driver.find_element_by_name("password")
usernamebox.send_keys(username)
passwordbox.send_keys(password, Keys.ENTER)

time.sleep(2)

driver.get("https://www.instagram.com/" + login.username)
followinglink = driver.find_element_by_partial_link_text('following')
followinglink.click()

time.sleep(1)

for i in range(1,numToRemove + 1):
    followingUser = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/ul/div/li[" + str(i) + "]/div/div[3]/button")
    followingUser.click()

    print(i)

    confirmUnfollow = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")
    confirmUnfollow.click()

time.sleep(1)
driver.quit()
