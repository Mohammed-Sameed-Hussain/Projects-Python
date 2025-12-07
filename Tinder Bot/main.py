from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from time import time, sleep

# --- Configuration & Credentials ---
# Note: Ideally, store these in environment variables rather than hardcoding.
tinder_url = "https://tinder.com"
my_gmail = "example@gmail.com"
my_password = "a2135345fd34fd23"
phone_number = '1546701344'

# --- WebDriver Setup ---
chrome_options = webdriver.ChromeOptions()
# Keeps the browser open after the script finishes
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open Tinder
driver.get(tinder_url)

# Setup explicit wait (will wait up to 10 seconds for elements to appear)
wait = WebDriverWait(driver, 10)

# --- Handle Cookie Consent ---
# Wait for the cookie banner to appear and click 'I Accept/Allow'
# Note: XPaths are fragile and may change if Tinder updates their UI.
cookies = wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="q1388376490"]/div/div[2]/div/div/div[1]/div[2]/button')))
cookies.click()

# --- Initiate Login ---
# Click the main "Log In" button on the homepage
login = driver.find_element(By.XPATH, value='//*[@id="q1388376490"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/header/div/div[2]/div[2]/a')
login.click()

gmail_login = False

try:
    print("Looking for Google iframe!")
    # The 'Sign in with Google' button is often inside an iframe.
    # We must find the iframe first.
    iframe = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//iframe[contains(@src,"https://accounts.google.com/gsi/button")]')))

    # Switch Selenium's context INTO the iframe to interact with elements inside it
    driver.switch_to.frame(iframe)

    # Click the "Continue with Google" button (German text "Weiter mit Google")
    google_login = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//span[contains(text(), "Weiter mit Google")]/parent::div/parent::div')))
    google_login.click()

    gmail_login = True

    # Switch context back to the main page (default content)
    driver.switch_to.default_content()

    print("Clicked! Now handling the popup window...")

except TimeoutException:
    print("Can't login via google! Iframe or button not found.")


# --- Handle Google Popup Window ---
if gmail_login:
    # Google login usually opens a new popup window. We need to switch control to it.
    new_window = None
    base_window = driver.current_window_handle
    
    # Loop through all open windows to find the new one
    for handle in driver.window_handles:
        print(handle)
        if handle != base_window:
            new_window = handle
            break

    if new_window:
        driver.switch_to.window(new_window)
        print("Switched to google login window!")
    else:
        print("Could not find the Google popup window!")
        exit()  # Stop execution if we didn't find the window

    # --- Enter Credentials ---
    # Input Email
    email = wait.until(EC.presence_of_element_located((By.ID, 'identifierId')))
    email.send_keys(my_gmail)

    # Click Next
    next_button = wait.until(EC.element_to_be_clickable((By.ID, "identifierNext")))
    next_button.click()

    # Input Password
    password = wait.until(EC.element_to_be_clickable((By.NAME, 'Passwd')))
    password.send_keys(my_password)

    # Click Next (Login)
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"Next")]/parent::button')))
    next_button.click()

    # --- Return to Main Window ---
    # Wait for the popup to close (window count goes back to 1)
    wait.until(EC.number_of_windows_to_be(1))
    driver.switch_to.window(base_window)

    # --- Phone Verification ---
    # Tinder often asks for phone verification even after Google login
    number = wait.until(EC.element_to_be_clickable((By.ID, 'phone_number')))
    number = driver.find_element(By.ID, value='phone_number')
    number.send_keys(phone_number)

    # Click Next to send SMS code
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Next")]/ancestor::button')))
    next_button.click()
    
    # Note: The script likely stops here or fails due to CAPTCHA/SMS verification manually needed.
