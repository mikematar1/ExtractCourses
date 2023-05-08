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
banner=driver.find_element("xpath","//a[@href='https://banweb.lau.edu.lb/' and @target='_blank']")
banner.click()
driver.switch_to.window(driver.window_handles[1])
student_services=driver.find_element("xpath", "//a[@href='/prod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu']")
student_services.click()
registration_input=driver.find_element("xpath","//a[@href='/prod/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu']")
registration_input.click()
look_up_input=driver.find_element("xpath","//a[@href='/prod/bwskfcls.p_sel_crse_search']")
look_up_input.click()
dropdown_path=driver.find_element("xpath","//select[@name='p_term']")
dropdown_menu=Select(dropdown_path)
dropdown_menu.select_by_value('202410')
dropdown_button=driver.find_element("xpath","//input[@type='submit' and @value='Submit']")
dropdown_button.click()
advance_s_but=driver.find_element("xpath","//input[@type='submit' and @name='SUB_BTN' and @value='Advanced Search']")
advance_s_but.click()
subject_path=driver.find_element("xpath","//select[@name='sel_subj' and @size='10']")
subject_menu=Select(subject_path)
subject_menu.select_by_value('CSC')