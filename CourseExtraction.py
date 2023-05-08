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