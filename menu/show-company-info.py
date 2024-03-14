import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
CT.003.002 - Show Company Info

Objective:
As long as the user is logged in
And be on any of the routes after the 'login' route
When the user clicks on the menu
And in the "About" option
Then the user should be redirected to the website https://saucelabs.com/
And the system must check whether the URL displayed in the browser matches the expected URL
And verify that the redirected page contains specific content that confirms that the user was directed correctly
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

# Part 2 - User Clicking on Menu and "About"
browser.find_element(By.ID, 'react-burger-menu-btn').click()
time.sleep(1)
browser.find_element(By.ID, 'about_sidebar_link').click()
time.sleep(1)

# Part 3 - URL Verification
current_url = browser.current_url
expected_url = 'https://saucelabs.com/'
assert current_url == expected_url, "Redirection was a failure."

# Part 4 - Check the Content (With Assert)
first_content = browser.find_element(By.CLASS_NAME, 'css-1jgtbl0').text
second_content = browser.find_element(By.CSS_SELECTOR, '.MuiTypography-root.MuiTypography-h4.css-18w5klh').text

assert first_content.lower() == 'Sauce Cross-Browser'.lower(), ("Verification of the 'Sauce-Cross Browser' was a failure.")

assert second_content.lower() == 'Trusted by industry leaders'.lower(), ("Verification of the 'Trusted by industry leaders' was a failure")

time.sleep(5)
browser.quit()

"""
When I didn't use assert (commented below), I iterated between the elements of the 'MuiTypography-h4' class, which are just 2:
- Trusted by industry leaders
- Deliver quality software continuously
In this case, in the iteration, I want it to identify only the element with the text "Trusted by industry leaders"
"""

# Part 4 - Check the Content (Without Assert)
# if current_url == expected_url:
#     browser.execute_script("alert('The redirection to the website was a success')")
#     time.sleep(3)
#     first_content = browser.find_element(By.CLASS_NAME, 'css-1jgtbl0').text
#     second_content = browser.find_elements(By.CLASS_NAME, 'MuiTypography-h4')
#
#     if first_content.lower() == 'Sauce Cross-Browser'.lower():
#         browser.execute_script("alert('Verification of the Sauce Cross-Browser was a success.')")
#         time.sleep(3)
#     else:
#         browser.execute_script("alert('Verification of the Sauce Cross-Browser was a failure.')")
#         time.sleep(3)
#
#     for content in second_content:
#         if content.text.lower() == 'Trusted by industry leaders'.lower():
#             browser.execute_script("alert('Verification of the Trusted by [...] was a success.')")
#             time.sleep(3)
#             break
#         else:
#             browser.execute_script("alert('Verification of the Trusted by [...] was a failure.')")
#             time.sleep(3)
# else:
#     browser.execute_script("alert('The redirection to the website was a failure.')")
#     time.sleep(3)


