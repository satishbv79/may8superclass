#selenium facebook registration
from selenium import webdriver
from selenium.webdriver.support import select

browser='ie'

if(browser=='chrome'):
    driver=webdriver.Chrome(executable_path="C:/Users//Downloads/chromedriver.exe")
elif(browser=='ff'):
    driver=webdriver.Firefox(executable_path="C:/Users//Downloads/")
elif(browser=='ie'):
driver=webdriver.chrome(executable_path="C:")

driver.get("http://www.facebook.com")
driver.implicitly_wait(5)
driver.find_element_by_name("firstname").send_keys("harish")
driver.find_element_by_name("lastname").send_keys("qspiders")
driver.find_element_by_xpath("//input[contains(@aria-label,'Mobile number')]").send_keys("321654")
driver.find_element_by_xpath("//input[@value='2']").click()
driver.find_element_by_name("websubmit").click(())
