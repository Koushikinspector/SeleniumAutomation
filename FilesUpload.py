from selenium import  webdriver
from selenium.webdriver import Keys

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="//Users//kousrikanth//Documents//chromedriver")
driver.get("http://webdriveruniversity.com/")
driver.find_element_by_xpath("//h1[text()='FILE UPLOAD']").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)

chooseFile = driver.find_element_by_xpath("//input[@type='file']")
chooseFile.send_keys("//Users//kousrikanth//Downloads//color1.webp")
driver.find_element_by_id("submit-button").click()

