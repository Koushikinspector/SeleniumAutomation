from selenium import  webdriver

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="//Users//kousrikanth//Documents//chromedriver")
driver.get("http://webdriveruniversity.com/")
driver.find_element_by_xpath("//h1[text()='AUTOCOMPLETE TEXTFIELD']").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
driver.find_element_by_name("food-item").send_keys("Donuts")
driver.find_element_by_id("submit-button").click()
driver.close()