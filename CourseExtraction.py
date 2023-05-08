from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import csv
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]

    path = "C:\\Users\\miche\\Downloads\\chromedriver_win32\\chromedriver.exe"
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)

    url = "https://myportal.lau.edu.lb/Pages/studentPortal.aspx"
    driver.get(url)

    username_input = driver.find_element("xpath", "//input[@type='text' and @id='username' and @name='username']")
    password_input = driver.find_element("xpath", "//input[@type='password' and @id='password']")
    button_input = driver.find_element("xpath", "//input[@type='submit' and @value='Log In']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    button_input.click()

    banner = driver.find_element("xpath", "//a[@href='https://banweb.lau.edu.lb/' and @target='_blank']")
    banner.click()
    driver.switch_to.window(driver.window_handles[1])

    student_services = driver.find_element("xpath", "//a[@href='/prod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu']")
    student_services.click()

    registration_input = driver.find_element("xpath", "//a[@href='/prod/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu']")
    registration_input.click()

    look_up_input = driver.find_element("xpath", "//a[@href='/prod/bwskfcls.p_sel_crse_search']")
    look_up_input.click()

    dropdown_path = driver.find_element("xpath", "//select[@name='p_term']")
    dropdown_menu = Select(dropdown_path)
    dropdown_menu.select_by_value('202410')

    dropdown_button = driver.find_element("xpath", "//input[@type='submit' and @value='Submit']")
    dropdown_button.click()

    advance_s_but = driver.find_element("xpath", "//input[@type='submit' and @name='SUB_BTN' and @value='Advanced Search']")
    advance_s_but.click()

    subject_path = driver.find_element("xpath", "//select[@name='sel_subj' and @size='10']")
    subject_menu = Select(subject_path)
    subject_menu.select_by_value('CSC')

    campus_path = driver.find_element("xpath", "//select[@name='sel_camp']")
    campus = Select(campus_path)
    campus_option = campus.options[0]
    driver.execute_script("arguments[0].setAttribute('disabled','disabled')", campus_option)
    campus.select_by_index(2)

    selection_search_but = driver.find_element("xpath", "//input[@type='submit' and @name='SUB_BTN']")
    selection_search_but.click()

    headers = [
        "Select",
        "CRN",
        "Subj",
        "Crse",
        "Sec",
        "Cmp",
        "Cred",
        "Title",
        "days",
        "time",
        "cap",
        "act",
        "rem",
        "WLCap",
        "WLAct",
        "WLRem",
        "XLCap",
        "XLAct",
        "XLRem",
        "Instructor",
        "Date (MM/DD)",
        "Location",
        "Attribute"
    ]

    data = []
    table = driver.find_element("xpath", "//table[contains(@class, 'datadisplaytable')]")
    rows = table.find_elements("xpath", ".//tr")
    for row in rows:
        cells = row.find_elements("xpath", ".//td")
        row_data = []
        for cell in cells:
            row_data.append(cell.text)
        data.append(row_data)

    filename = "classes.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
if __name__ == "__main__":
    main()