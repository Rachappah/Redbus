'''
Created on 06-May-2019

@author: racha
'''

from selenium import webdriver
import  time
from lib2to3.tests.support import driver
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.get("https://www.redbus.in/bus-tickets/")
time.sleep(5)
# Maximize page 
driver.maximize_window()
time.sleep(3)
# Scroll down page 
driver.execute_script("window.scrollTo(0, 1500);")
time.sleep(5)
#Drop down option selection 
select = Select(driver.find_element_by_id('sourceDrop'))
select.select_by_visible_text('Chennai')
select.select_by_value(2)
#time.sleep(5)
#driver.find_element_by_xpath("//*[@id='time-btn5']").click()