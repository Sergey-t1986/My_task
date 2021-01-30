from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in")
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_xpath("//h3[contains(., 'Selenium Ruby')]").click()
driver.find_element_by_xpath("//a[contains(., 'Review')]").click()
driver.find_element_by_css_selector(".star-5").click()
driver.find_element_by_id("comment").send_keys("Nice book!")
driver.find_element_by_id("author").send_keys("Sergey")
driver.find_element_by_id("email").send_keys("test@ya.com")
driver.find_element_by_id("submit").click()
driver.quit()




