from selenium import  webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome(executable_path="//Users//kousrikanth//Documents//chromedriver")
driver.get("http://webdriveruniversity.com/")
driver.find_element_by_xpath("//h1[text()='BUTTON CLICKS']").click()

handles = driver.window_handles
for i in handles:
    driver.switch_to.window(i)
    clk1 = driver.find_element_by_id("button1").click()
driver.close()