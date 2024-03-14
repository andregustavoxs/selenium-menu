import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
CT.003.004 - Reset App State

Objective:
As long as the user is logged in
And stay on any of the post-login routes
And have added at least 2 products to the cart
When the user clicks on the menu
And in the option "Reset application state"
Then all items in the cart must be deleted, regardless of products added or not
And the system must check whether the number of items appears above the cart icon
"""

# Prevent Webdriver instance from closing automatically
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()

browser.get('https://www.saucedemo.com/')
time.sleep(1)

# Part 1 - Login
browser.find_element(By.ID, 'user-name').send_keys('standard_user')
time.sleep(1)
browser.find_element(By.ID, 'password').send_keys('secret_sauce')
time.sleep(1)
browser.find_element(By.ID, 'login-button').click()
time.sleep(1)

# Part 2 - Adding Items
browser.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
time.sleep(1)
browser.find_element(By.ID, 'add-to-cart-sauce-labs-fleece-jacket').click()
time.sleep(1)
browser.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
time.sleep(1)

# Part 3 - Opening Menu and Clicking in the Button "ALl Items"
browser.find_element(By.ID, 'react-burger-menu-btn').click()
time.sleep(1)
browser.find_element(By.ID, 'reset_sidebar_link').click()
time.sleep(1)

# Part 4 - Check if all items were cleared (With Assert)
try:
    badge = browser.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link span.shopping_cart_badge')
    assert not badge.text, "There are still items in the cart."
except NoSuchElementException:
    pass

time.sleep(5)
browser.quit()

# Part 4 - Check if all items were cleared (Without Assert)
# try:
#     badge = browser.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link span.shopping_cart_badge')
#     if not badge.text:
#         browser.execute_script("alert('Items cleared successfully.')")
#         time.sleep(3)
#     else:
#         browser.execute_script("alert('There are still Items in the cart.')")
#         time.sleep(3)
# except NoSuchElementException:
#     browser.execute_script("alert('Items cleared successfully.')")
#     time.sleep(3)