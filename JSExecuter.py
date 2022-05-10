from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="//Users//kousrikanth//Documents//chromedriver")
driver.get("https://the-internet.herokuapp.com")

driver.find_element_by_xpath("//a[text()='JavaScript Alerts']").click()
cli = driver.find_element_by_xpath("//button[text()='Click for JS Prompt']")
driver.execute_script("arguments[0].click();", cli)

alert = driver.switch_to.alert

alert.send_keys("Hi Koushik")
print(alert.text)
alert.dismiss()
