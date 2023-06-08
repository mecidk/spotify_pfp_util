from selenium import webdriver
import time
import urllib.request
import re

profileUrl = ""

profileUrl = input("Enter the profile url: ")

photoXpath = """//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div/div[1]/div[4]/div/div/img"""
nameXpath = """//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div/div[1]/div[5]/span/h1"""

driver = webdriver.Chrome('./chromedriver')

driver.get(profileUrl)

time.sleep(8)

photoElement = driver.find_element_by_xpath(photoXpath)
photoUrl = photoElement.get_attribute("src")

nameElement = driver.find_element_by_xpath(nameXpath)
nameStrRaw = nameElement.get_attribute("innerHTML")
nameStr = re.sub(r'[^a-zA-Z0-9]', '', nameStrRaw).lower()

fileStr = "./images/" + nameStr + ".jpeg"

urllib.request.urlretrieve(photoUrl, fileStr)

driver.quit()