#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:10:02 2018
This code is used to automate of Gmail login Page.
Selenium webdriver and Python is used for Development.

@author: rohit
"""

from selenium import webdriver
import time
loginname=input('Enter Email Id:') 
gmailpassword=input('Enter Password:') 

driver= webdriver.Chrome()
driver.get('http://www.gmail.com/')
print ("Opened Gmail")

emailid=driver.find_element_by_id("identifierId")
emailid.send_keys(loginname)
print ("Email Id entered")

driver.find_element_by_xpath('//*[@id="identifierNext"]/content').click()
print ('Next Button clicked')
print ("Start : %s" % time.ctime())
time.sleep(1)
print ("End : %s" % time.ctime())
passw=driver.find_element_by_name('password')
passw.send_keys(gmailpassword)
print ('Password Entered')
signin=driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
signin.click()
print('Next button click and gmail is login successfully.')
print ("Start : %s" % time.ctime())
time.sleep(5)
print ("End : %s" % time.ctime())
print('Gmail Login')
logo = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[1]/div[4]/div/a/img')
print ('logo reached')