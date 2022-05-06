from selenium import webdriver
from selenium.webdriver.support.ui import Select 
import time

driver = webdriver.Chrome()
driver.get("http://164.100.133.129:82/tutresult/")

input=driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtReg"]')
input.send_keys('19B11000')

input=driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlExam"]')
input.click()

time.sleep(5)

#select the sem which you want and leave it it will click view button auto

input=driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnview"]')
input.click()

