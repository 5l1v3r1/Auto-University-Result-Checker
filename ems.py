from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("http://164.100.133.129:82/tutresult//")

input=driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtReg"]')
input.send_keys('19B11096') #put your reg no

input=driver.find_element_by_css_selector('#ContentPlaceHolder1_ddlExam').click()

time.sleep(2)

dropdown = Select(driver.find_element_by_id("ContentPlaceHolder1_ddlExam"))
dropdown.select_by_value("CBBCAD") #i putted 4th sem vlaue put your required > 1st sem-CBBCAA 2nd sem-CBBCAB 3rd sem-CBBCAC 5th sem-CBBCAE 6th sem-CBBCAF

input=driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnview"]')
input.click()

time.sleep(15)

