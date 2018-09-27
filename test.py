from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
browser = webdriver.Firefox(executable_path='/home/madisnit/Desktop/selenium/geckodriver')
browser.get("https://login.yahoo.com/config/login?.src=fpctx&.intl=in&.lang=en-IN&.done=https%3A%2F%2Fin.yahoo.com")
ele = browser.find_element_by_id("login-username")
ele.send_keys("m.veeranitesh@yahoo.com")
ele = browser.find_element_by_id("login-signin")
ele.click()
time.sleep(1)
ele = browser.find_element_by_id("login-passwd")
ele.send_keys("Nitesh12#")
ele = browser.find_element_by_id("login-signin").click()
ele = browser.find_element_by_id("uh-mail-link").click()
ele = browser.find_element_by_id("Compose").click()
time.sleep(1)
ele = browser.find_element_by_id("to-field").send_keys("bejjam.manusha@votarytech.com")
time.sleep(1)
ele = browser.find_element_by_id("subject-field").send_keys("test mail")
ele = browser.find_element_by_id("rtetext").send_keys("Hi, please find attachements")
time.sleep(1)
browser.find_element_by_css_selector('.compose .attachments-pane .attachment-button-attach').click()
#browser.find_element_by_xpath("//select[@name='element_name']/option[text()='option_text']").click()
#browser.find_element_by_xpath("//select[@name='element_name']/option[text()='option_text']").click()
#ele.send_keys(Keys.ENTER) 
browser.find_element_by_xpath("//*[@id=':b7']/li/span").click()
#attach_id = browser.find_element_by_id(".menu-attach-file-from-computer .menu-with-icon").click()
#attach_id.send_keys(Keys.CONTROL + Keys.ENTER)
#print attach_id.send_keys(os.getcwd()+"/a.txt")

