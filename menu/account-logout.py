import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
CT.003.003 - Account Logout

Objective:
As long as the user is logged in
And be on any of the routes after the login route
When the user clicks on the menu
And in the "Logout" option
Then the user must be logged out and redirected to the Login route
And try to access any of the routes after login to ensure they are no longer accessible
"""

# Prevent Webdriver instance from closing automatically
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(options=options, service=service)
browser.maximize_window()
browser.get('https://www.saucedemo.com/')

# Part 1 - Login
browser.find_element(By.ID, 'user-name').send_keys('standard_user')
time.sleep(1)
browser.find_element(By.ID, 'password').send_keys('secret_sauce')
time.sleep(1)
browser.find_element(By.ID, 'login-button').click()
time.sleep(1)

# Part 2 - User Clicking on Menu and "Logout"
browser.find_element(By.ID, 'react-burger-menu-btn').click()
time.sleep(1)
browser.find_element(By.ID, 'logout_sidebar_link').click()
time.sleep(1)

# Part 3 - Is User Authenticated Test
browser.get('https://www.saucedemo.com/inventory.html')
time.sleep(1)

current_url = browser.current_url
expected_url = 'https://www.saucedemo.com/'

# Part 4 - Without Assert
# if current_url == expected_url:
#     browser.execute_script("alert('User is not authenticated.')")
# else:
#     browser.execute_script("alert('User is still authenticated.')")

# Part 4 - With Assert
assert current_url == expected_url, "User is still authenticated."

time.sleep(5)
browser.quit()
