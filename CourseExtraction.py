from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import csv,sys

username = sys.argv[1]
password = sys.argv[2]


path="C:\\Users\\miche\\Downloads\\chromedriver_win32\\chromedriver.exe"
service= Service(executable_path=path)
driver=webdriver.Chrome(service=service)
url="https://myportal.lau.edu.lb/Pages/studentPortal.aspx"
driver.get(url)

username_input=driver.find_element("xpath","//input[@type='text' and @id='username' and @name='username']")

password_input=driver.find_element("xpath","//input[@type='password' and @id='password']")

button_input=driver.find_element("xpath","//input[@type='submit' and @value='Log In']")

username_input.send_keys(username)
password_input.send_keys(password)
button_input.click()