from selenium import  webdriver

driver = webdriver.Chrome(executable_path="//Users//kousrikanth//Documents//chromedriver")
driver.get("https://www.goibibo.com")
#goibibo logo
#driver.find_element_by_css_selector("#root > div > div.xayxd-0.bkpnzL > div > header > a > span").click()
#signin or login 
#driver.find_element_by_id("get_sign_in").click()
#hotels
driver.find_element_by_xpath("//a[text()='hotels']").click()
#flights
driver.find_element_by_xpath("//a[text()='trains']").click()
#cabs
driver.find_element_by_xpath("//a[text()='cabs']").click()
# round trip
driver.find_element_by_xpath("//span[text()='Round-trip']").click()
#From
driver.find_element_by_xpath("//span[text()='From']").click()
#To
driver.find_element_by_xpath("//span[text()='To']").click()
#faretype Student
driver.find_element_by_xpath("//span[text()='student']").click()
#view all products
driver.find_element_by_xpath("//a[text()='VIEW ALL PRODUCTS']").click()