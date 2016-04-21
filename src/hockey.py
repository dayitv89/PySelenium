###-
###- Hockey bulk worker single program, single process with Google chrome
###-
###- GauravDS
###- JAMES Selenium Module(b)
###-


### configurations
web_opening_time = 3
json_file_name = 'hockey_apps.json'
platform = 'iOS'
## login details
hockey_user = "<your hockey app email_id>"
hockey_pwd = "<your hockey app password>"
## webhook details
webhook_name = 'iOS Hook'
webhook_url = 'http://xyz.abc'


### read json data from file
import json
def read_file(file_name):
	return json.loads(open(file_name).read())

### sleep the program to wait response
import time
def wait():
	time.sleep(web_opening_time)


### Selenium automation
#- download http://chromedriver.storage.googleapis.com/index.html?path=2.21/
#- details https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver

## Selenium web drivers
driver = None
## load web driver for selenium : chrome
def web_driver_load():
	global driver
	driver = webdriver.Chrome()
## quit web driver for selenium
def web_driver_quit():
	driver.quit()

## actual login in hockey app site
def hockey_login(user_name, password):
	driver.get('https://rink.hockeyapp.net/users/sign_in');
	wait()
	web_obj = driver.find_element_by_id('user_email')
	web_obj.send_keys(hockey_user)
	web_obj = driver.find_element_by_id('user_password')
	web_obj.send_keys(hockey_pwd)
	web_obj.submit()

def webhooks(app_id, wh_name, wh_url):
	final_url = 'https://rink.hockeyapp.net/manage/apps/'+str(app_id)+'/webhooks/new'
	print(final_url)
	driver.get(final_url);
	wait()
	web_obj = driver.find_element_by_id('webhook_name')
	web_obj.send_keys(wh_name)
	web_obj = driver.find_element_by_id('webhook_url')
	web_obj.send_keys(wh_url)
	web_obj.submit()


### Main Method
if __name__ == "__main__":
	web_driver_load()
	hockey_login(hockey_user, hockey_pwd)
	wait()
	apps = read_file(json_file_name)
	for app in apps:
		if app['platform'] == platform:
			print("\nPlatform: " + platform + "\tapp :" + app['title'])
			webhooks(app['id'], webhook_name, webhook_url)
			wait()
	print("Process complete successfully")
	wait()
	web_driver_quit()
