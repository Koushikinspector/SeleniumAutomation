from selenium import  webdriver

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="//Users//kousrikanth//Documents//chromedriver")
driver.get("http://webdriveruniversity.com/")
driver.find_element_by_xpath("//h1[text()='DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S)']").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)

##dropdown selection
course = Select(driver.find_element_by_id("dropdowm-menu-1"))
course.select_by_value("python")

ide=Select(driver.find_element_by_id("dropdowm-menu-2"))
ide.select_by_value("maven")

lang=Select(driver.find_element_by_id("dropdowm-menu-3"))
lang.select_by_value("html")

##Radio button
radiobutton = driver.find_elements_by_name("color")
radiobutton[3].click()



## checkboxes
checkboxes = driver.find_elements_by_xpath("//input[@type='checkboxes']")
for checkbox in checkboxes:
    if checkbox.get_attribute("Value") == 'option-2':
        checkbox.click()


