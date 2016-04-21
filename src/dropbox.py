# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import selenium.webdriver.chrome.service as service
import time
import random
import string
#'AZNqR2vd',
referelUrls = ['dhyZBwpY']

def registerUser(val):
	domain = ''.join(random.choice(string.ascii_lowercase) for i in range(8));
	uname = ''.join(random.choice(string.ascii_lowercase) for i in range(4));
	driver = webdriver.Chrome()
	wait = ui.WebDriverWait(driver,10)
	driver.get("https://db.tt/"+val)
	print(driver.current_url)
	wait.until(lambda driver: driver.find_elements_by_class_name('login-form-container'))

	print("Login form in now available")
	elem = driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/input')
	elem.send_keys("test")
	elem = driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/div[2]/div/div/form/div[3]/div[2]/input')
	elem.send_keys("test")
	elem = driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/div[2]/div/div/form/div[4]/div[2]/input')
	elem.send_keys(uname+"@"+domain+".com")
	elem = driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/div[2]/div/div/form/div[5]/div[2]/input')
	elem.send_keys("testing")
	checkboxes = driver.find_elements_by_xpath("/html/body/div[13]/div[2]/div/div[2]/div/div/form/div[6]/input")
	for checkbox in checkboxes:
	    checkbox.click()
	elem.send_keys(Keys.RETURN)
	time.sleep(5)
	driver.close()
	return uname+"@"+domain+".com"

for i, val in enumerate(referelUrls):
	target = open(val+".txt", 'w')

	for i in range(10):
		#time.sleep(5)
		uname = registerUser(val)
		target.write(uname)
		target.write("\n")

	print("And finally, we close it.")
	target.close()