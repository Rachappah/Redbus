'''
Created on 06-May-2019

@author: racha
'''
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from lib2to3.tests.support import driver
from selenium.webdriver.support.ui import Select
import time


driver=webdriver.Firefox()
driver.get("https://www.redbus.in/bus-tickets/")
driver.maximize_window()
time.sleep(4)
driver.find_element_by_id("txtSource").send_keys("Bangalore (All Locations)")
time.sleep(4)
driver.find_element_by_id("txtDestination").send_keys("Kukatpally, Hyderabad")

datefield = driver.find_element_by_id('txtOnwardCalendar')
datefield.click()
datefield.send_keys("11052019")

time.sleep(5)

datefield = driver.find_element_by_id('txtReturnCalendar')
datefield.click()
datefield.send_keys("12052019")

time.sleep(5)

elem = driver.find_element_by_xpath("//button[@class='search-btn searchBuses']")
time.sleep(3)
elem.click()
time.sleep(4)
driver.back()

driver.refresh()

#select the filteration checkbox
time.sleep(4)
driver.find_element_by_xpath("//li[@id='4330974']//div[@class='button view-seats fr'][contains(text(),'View Seats')]").click()
time.sleep(4)
driver.find_element_by_xpath("//ul[@class='list-chkbox']//li[1]//label[1]").click()
time.sleep(4)
driver.find_element_by_xpath("//ul[@class='list-chkbox']//li[2]//label[1]").click()
time.sleep(4)
driver.find_element_by_xpath("//ul[@class='list-chkbox']//li[3]//label[1]").click()
time.sleep(4)
driver.find_element_by_xpath("//ul[@class='list-chkbox']//li[4]//label[1]").click()

time.sleep(4)
driver.find_element_by_xpath("//ul[@class='dept-time at-time-filter']//li[4]//label[1]").click()

#scroll down page
time.sleep(4)
driver.execute_script("window.scrollTo(0, 500);")

time.sleep(4)
driver.find_element_by_xpath("//input[@placeholder='BOARDING POINT']").click()
time.sleep(4)
driver.find_element_by_xpath("//div[@class='overlay']//li[3]//label[1]").click()
time.sleep(4)
driver.find_element_by_xpath("//div[@class='button btn-apply bp-apply']").click()

time.sleep(4)
driver.execute_script("window.scrollTo(0, 500);")

time.sleep(4)
driver.find_element_by_xpath("//input[@placeholder='DROPPING POINT']").click()
time.sleep(4)
driver.find_element_by_xpath("//li[5]//label[1]").click()
time.sleep(4)
driver.find_element_by_xpath("//div[@class='button btn-apply dp-apply']").click()


