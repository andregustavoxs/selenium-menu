import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


"""
CT.003.001 - Show All Items

Objective:
As long as the user is logged in
And be on any of the routes after the 'Login' route
When the user clicks on the menu
And in the "All Items" option
Then the user should be redirected to the 'Inventory' route
And the system must check whether the URL displayed in the browser matches the expected URL"""

# Prevent Webdriver instance from closing automatically
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.maximize_window()

browser.get('https://www.saucedemo.com/')

# Part 1 - Login
browser.find_element(By.ID, 'user-name').send_keys('standard_user')
time.sleep(1)
browser.find_element(By.ID, 'password').send_keys('secret_sauce')
time.sleep(1)
browser.find_element(By.ID, 'login-button').click()
time.sleep(1)

# Part 2 - Clicking On The Cart Icon
browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
time.sleep(1)

# Part 3 - Opening Menu and Clicking in the Button "ALl Items"
browser.find_element(By.ID, 'react-burger-menu-btn').click()
time.sleep(1)
browser.find_element(By.ID, 'inventory_sidebar_link').click()
time.sleep(3)

# Part 4 - Condition of the Route /inventory
current_url = browser.current_url
expected_url = 'https://www.saucedemo.com/inventory.html'

if current_url == expected_url:
    browser.execute_script("alert('The user is in the correct route.')")
else:
    browser.execute_script("alert('The user is not in the correct route.')")

time.sleep(3)
browser.quit()