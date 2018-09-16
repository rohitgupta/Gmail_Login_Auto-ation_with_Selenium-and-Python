#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 19:10:02 2018
This code is used to automate of Gmail login Page.
Selenium webdriver and Python is used for Development.
We have used Spyder as an IDE which is available under Anaconda. 

Enter Email Id:user@gmail.com

Enter Password:*********
Opened Gmail
Email Id entered
Next Button clicked
Start : Sun Aug 19 11:57:17 2018
End : Sun Aug 19 11:57:18 2018
Password Entered
Next button click and gmail is login successfully.
Start : Sun Aug 19 11:57:18 2018
End : Sun Aug 19 11:57:23 2018
Gmail Login
logo reached
@author: rohit
"""

from selenium import webdriver
import time
loginname=input('Enter Email Id:') 
gmailpassword=input('Enter Password:') 
#emailid = input('Enter email id to search:.')

driver= webdriver.Chrome()
driver.get('http://www.gmail.com/')
print ("Opened Gmail")

emailid=driver.find_element_by_id("identifierId")
emailid.send_keys(loginname)
print ("Email Id entered:.")

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
time.sleep(5)
driver.find_element_by_xpath("//span[@class='gb_9a gbii']").click()
print ('Google Account click successful.')
time.sleep(5)
driver.find_element_by_css_selector('#gb_71').click()
print('Gmail Sign Out Successfull.')                                    
'''
logo = driver.find_element_by_xpath('//span[@class="gb_Wa gb_ec"]')
print ('logo reached')
time.sleep(5)

driver.find_element_by_id("//div[@class='aoq']").click()
print('Search Box click Successfully.')
time.sleep(5)
driver.find_element_by_css_selector('#:kr').send_keys(emailid)
print('Email id Entered Successfully.')
time.sleep(5)
driver.find_element_by_xpath("//button[@class='gb_cf gb_mf']//*[@focusable='false']]/button[4]/svg").click()
'''