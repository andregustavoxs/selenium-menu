import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
CT.003.005 - Hamburguer Menu Itself

Objective:
As long as the user is logged in
And be on any of the routes after the login route
When the user clicks on the menu
And hover over "All About"
Then the system must check if the color has actually changed on the hover of the "All About" button
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

# Part 3 - Opening Menu and checking the Hover of "All About"
browser.get('https://www.saucedemo.com/cart.html')
time.sleep(1)

browser.find_element(By.ID, 'react-burger-menu-btn').click()
about_item = browser.find_element(By.ID, 'about_sidebar_link')
all_items = browser.find_element(By.ID, 'inventory_sidebar_link')
time.sleep(1)

"""
Creates an ActionChains Instance.
ActionChains Class does an automation of the interactions such as mouse movements, mouse button actions, etc.
In this case, we are going to test the hover.
"""

actions = ActionChains(browser)

actions.move_to_element(about_item).perform()
time.sleep(1)
color_before = about_item.value_of_css_property('color')

actions.move_to_element(all_items).perform()
time.sleep(1)
color_after = about_item.value_of_css_property('color')

print(f"Color before hover: {color_before}")
print(f"Color after hover: {color_after}")