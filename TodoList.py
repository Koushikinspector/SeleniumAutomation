from selenium import  webdriver
from selenium.webdriver import Keys

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="//Users//kousrikanth//Documents//chromedriver")
driver.get("http://webdriveruniversity.com/")
driver.find_element_by_xpath("//h1[text()='TO DO LIST']").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
driver.find_element_by_xpath("//input[@placeholder='Add new todo']").send_keys("hi good evening",Keys.ENTER)

