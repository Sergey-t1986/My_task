import keyboard as keyboard
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
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
driver.find_element_by_xpath("//a[contains(., 'Shop')]").click()
driver.find_element_by_xpath("//h3[contains(., 'HTML5 Forms')]").click()
time.sleep(3)
text_title = driver.find_element_by_xpath("//h1[contains(., 'HTML5 Forms')]")
title = text_title.text
assert "HTML5 Forms" in title
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
driver.find_element_by_xpath("//a[contains(., 'Shop')]").click()
time.sleep(3)
driver.find_element_by_xpath("//a[contains(text(),'HTML')]").click()
time.sleep(3)
# self.assertEqual(len(self.driver.find_elements_by_class_name(‘b-offers__info’)), 10)
qty_element = driver.find_elements_by_css_selector(".product")
time.sleep(2)
if len(qty_element)  == 3:
    print("3 book")
else:
    print("Error qty")
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
driver.find_element_by_xpath("//a[contains(., 'Shop')]").click()
time.sleep(3)
textElement = driver.find_element_by_css_selector('[selected="selected"]')
result = textElement.text
if result == 'Sort by price: high to low':
    print('Sort by High to Low')
else:
    print("Items sorting by: "+"\"" + result + "\"")
    time.sleep(3)
S_Pr_desc = driver.find_element_by_css_selector('[name="orderby"]')
select = Select(S_Pr_desc)
select.select_by_value("price-desc")
time.sleep(3)
element = driver.find_element_by_css_selector('[selected="selected"]')

E_txt = element.text

if E_txt == "Sort by price: high to low":
    print("Sort: \"high to low\"")
else:
    print("Sort: " + "\"" + E_txt + "\"")

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
driver.find_element_by_xpath("//a[contains(., 'Shop')]").click()
time.sleep(3)

Guide = driver.find_element_by_css_selector('[class="products masonry-done"] h3')
Guide.click()
element2 = driver.find_element_by_css_selector(".price del")
element_get_text = element2.text
assert str(element_get_text) == "₹600.00"
print("Price = ₹600.00")

element2 = driver.find_element_by_css_selector(".price ins")
element_get_text = element2.text
assert str(element_get_text) == "₹450.00"
print("Price = ₹450.00")

image = driver.find_element_by_css_selector('.images')
image.click()
time.sleep(4)

close = driver.find_element_by_css_selector('.pp_close')
close.click()
time.sleep(2)
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
driver.find_element_by_xpath("//a[contains(., 'Shop')]").click()
time.sleep(3)
HTML5 = driver.find_element_by_css_selector('[data-product_id="181"]')
HTML5.click()
time.sleep(5)

qty = driver.find_element_by_css_selector('[class="cartcontents"]')
result = qty.text
assert result == "1 Item"
print("Qty = \"1 item\"")

price = driver.find_element_by_css_selector('[class="amount"]')
amount = price.text
assert amount == "₹280.00"
print("Price = \"₹280.00\"")

Cart = driver.find_element_by_css_selector('[class="wpmenucart-contents"]').click()
time.sleep(4)

Subtotal = driver.find_element_by_css_selector('[data-title="Subtotal"] span')
Sub = Subtotal.text
assert Sub != ""
print("Subtotal = " + "\"" + Sub + "\"")
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
driver.find_element_by_xpath("//a[contains(., 'Shop')]").click()


HTML5 = driver.find_element_by_css_selector('[data-product_id="181"]')
HTML5.click()

time.sleep(4)

JSD = driver.find_element_by_css_selector('[data-product_id="165"]')
JSD.click()

time.sleep(4)

Basket = driver.find_element_by_css_selector('[class="wpmenucart-contents"]')
Basket.click()
time.sleep(4)

HTML_del = driver.find_element_by_css_selector('[class="product-remove"] a')
HTML_del.click()

time.sleep(5)
HTML_undo = driver.find_element_by_css_selector('[class="woocommerce-message"] a')
HTML_undo.click()

HTML_plus = driver.find_element_by_css_selector('[class="cart_item"]:nth-child(2) input')
HTML_plus.clear()
HTML_plus.send_keys("3")

upb = driver.find_element_by_css_selector('[name="update_cart"]')
upb.click()

expect = driver.find_element_by_css_selector('[class="cart_item"]:nth-child(2) input')
result = expect.get_attribute("value")
assert str(result) == "3"
print("Qty 3")

time.sleep(5)
coupon = driver.find_element_by_css_selector('[name="apply_coupon"]').click()

coupon_text = driver.find_element_by_xpath('//li [text()="Please enter a coupon code."]')

if coupon_text is not None:
    print("Message: \"Please enter a coupon code.\"")
else:
    print("No message: \"Please enter a coupon code.\"")

time.sleep(3)
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
driver.find_element_by_xpath("//a[contains(., 'Shop')]").click()
HTML5 = driver.find_element_by_css_selector('[data-product_id="165"]')
HTML5.click()

Cart = driver.find_element_by_css_selector('[class="wpmenucart-contents"]')
time.sleep(5)
Cart.click()

B_ptc = driver.find_element_by_css_selector('[class="wc-proceed-to-checkout"] a')
time.sleep(5)
B_ptc.click()

T_first_n_txt = "Anton"
T_last_n_txt = "Belyaev"
T_mail_txt = "1234@ya.ru"
T_phone_txt = "89635647235"
T_Country_txt = "Russia"
T_Address_txt = "st.Lenina 45"
T_Town_City_txt = "St.Peterburg"
T_State_County_txt = "St.Peterburg"
T_postcode_txt = "124566"


time.sleep(5)
T_first_n = driver.find_element_by_css_selector('[id="billing_first_name"]')
T_first_n.send_keys(T_first_n_txt)

T_last_n = driver.find_element_by_css_selector('[id="billing_last_name"]')
T_last_n.send_keys(T_last_n_txt)

T_mail = driver.find_element_by_css_selector('[id="billing_email"]')
T_mail.send_keys(T_mail_txt)

T_phone = driver.find_element_by_css_selector('[id="billing_phone"]')
T_phone.send_keys(T_phone_txt)

T_Country = driver.find_element_by_css_selector('[id="s2id_billing_country"]')
T_Country.click()

time.sleep(5)

T_Country2 = driver.find_element_by_css_selector('[id="s2id_autogen1_search"]')
T_Country2.send_keys(T_Country_txt)

keyboard.press('Enter')

T_Address = driver.find_element_by_css_selector('[id="billing_address_1"]')
T_Address.send_keys(T_Address_txt)

T_Town_City = driver.find_element_by_css_selector('[id="billing_city"]')
T_Town_City.send_keys(T_Town_City_txt)

T_State_County = driver.find_element_by_css_selector('[id="billing_state"]')
T_State_County.send_keys(T_State_County_txt)

T_postcode = driver.find_element_by_css_selector('[id="billing_postcode"]')
T_postcode.send_keys(T_postcode_txt)

driver.execute_script("window.scrollBy(0, 600);")

time.sleep(3)
Check_Payments = driver.find_element_by_css_selector('[id="payment_method_cheque"]')
Check_Payments.click()
time.sleep(3)

B_PLACE_ORDER = driver.find_element_by_css_selector('[id="place_order"]')
B_PLACE_ORDER.click()

time.sleep(10)

wait = WebDriverWait(driver, 20).until
wait(EC.presence_of_element_located((By.XPATH, '//p [text() = "Thank you. Your order has been received."]')))
print("Thank you. Your order has been received.")

element = wait(EC.presence_of_element_located((By.XPATH, '//strong [text() = "Check Payments"]')))
print("Payment method showed.")


time.sleep(3)
driver.quit()

