from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://practice.automationtesting.in")
driver.find_element_by_xpath("//a[contains(., 'My Account')]").click()
driver.find_element_by_id("reg_email").send_keys("testFrm@mai.com")
time.sleep(3)
driver.find_element_by_id("reg_password").send_keys("vfdbdbd44ty5hfthrt")
driver.find_element_by_name("register").click()
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in")
driver.find_element_by_xpath("//a[contains(., 'My Account')]").click()
driver.find_element_by_id("username").send_keys("testFrm@mai.com")
time.sleep(3)
driver.find_element_by_id("password").send_keys("vfdbdbd44ty5hfthrt")
driver.find_element_by_name("login").click()
time.sleep(3)
text_log_out = driver.find_element_by_xpath("//a[contains(., 'Sign out')]")
sign_out = text_log_out.text
assert "Sign out" in sign_out
driver.quit()