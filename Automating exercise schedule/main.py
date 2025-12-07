from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import datetime

# --- Configuration ---
# Store user credentials and target URL in constants for easy modification.
ACCOUNT_EMAIL = "sameedhussain202@gmail.com"
ACCOUNT_PASSWORD = "Qz34tgf!@3*Cob()l"
FULL_NAME = "Sameed Hussain"
GYM_URL = "https://appbrewery.github.io/gym/"

# --- Setup Driver ---
# Create a persistent directory for the Chrome profile.
# This prevents having to log in manually every single time if cookies are saved.
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
if not os.path.exists(user_data_dir):
    os.makedirs(user_data_dir)

chrome_options = webdriver.ChromeOptions()
# 'detach' keeps the browser open after the script finishes.
chrome_options.add_experimental_option("detach", True) 
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

# --- Define a centralized Waiter ---
# We reuse this everywhere instead of creating new ones.
# It defines a standard timeout of 10 seconds for locating elements.
wait = WebDriverWait(driver, 10)

# --- Phase 1: Attempt Login ---
print("--- Phase 1: Attempting Login ---")

# Wait for and click 'Join Today' to reach the auth page.
join_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/gym/login/'] button")))
join_btn.click()

# Wait for the email field to ensure the form has loaded into the DOM.
email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))

# Fill Login Form with predefined credentials.
driver.find_element(By.ID, 'email-input').send_keys(ACCOUNT_EMAIL)
driver.find_element(By.ID, 'password-input').send_keys(ACCOUNT_PASSWORD)
driver.find_element(By.ID, 'submit-button').click()

# --- Phase 2: Check for Failure (Linear Check) ---
login_failed = False

try:
    # We wait briefly (3s) to see if an error pops up. 
    # If it does, we set our flag to True.
    error_element = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.ID, "error-message")) # or CLASS_NAME if ID fails
    )
    print(f"Login Error Caught: {error_element.text}")
    login_failed = True

except TimeoutException:
    # If 3 seconds pass and no error appears, we assume Login might be good.
    print("No error message appeared. Proceeding...")

# --- Phase 3: Registration (Only if Login Failed) ---
# This block acts as a fallback mechanism. If the login failed, 
# it assumes the user does not exist and attempts to create an account.
if login_failed:
    print("--- Phase 3: Switching to Registration ---")
    
    # Switch Toggle from "Login" to "Register"
    driver.find_element(By.ID, 'toggle-login-register').click()
    
    # Wait for Name field (confirms switch happened)
    name_input = wait.until(EC.visibility_of_element_located((By.ID, "name-input")))
    
    # Re-fill form (Inputs often clear on toggle switch)
    name_input.send_keys(FULL_NAME)
    # Note: Email and Password might remain filled or need re-filling depending on site behavior.
    # driver.find_element(By.ID, 'email-input').send_keys(ACCOUNT_EMAIL)
    # driver.find_element(By.ID, 'password-input').send_keys(ACCOUNT_PASSWORD)
    
    driver.find_element(By.ID, 'submit-button').click()

# --- Phase 4: Final Success Verification ---
# We do this ONCE at the end. It covers both Login and Registration scenarios.
print("--- Phase 4: Verifying Success ---")

try:
    # Verify we have been redirected to the main schedule page.
    wait.until(EC.visibility_of_element_located((By.ID, "schedule-page")))
    print("SUCCESS: We have landed on the Schedule Page!")
except TimeoutException:
    print("FAILURE: Could not verify login/registration. Still on form page?")

# --- Date Logic Setup ---
today = datetime.date.today()
# 2. Format it to get the full day name (e.g., "Monday", "Tuesday")
day_name = today.strftime("%A")


# --- Dynamic Element Selection ---
# The website changes the ID of the columns based on the current day.
# E.g., if today is Monday, Monday's column ID is 'day-title-today'.
# This logic ensures we grab the correct 'Tuesday' and 'Thursday' columns
# regardless of what the actual current day is.

if day_name == 'Monday':
    # If Mon: Tuesday is "Tomorrow", Thursday is standard.
    tuesday_ = driver.find_element(By.CSS_SELECTOR,value='div[id^="day-title-tomorrow-"]')
    tuesday_classes = tuesday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')


    thursday_ = driver.find_element(By.CSS_SELECTOR,value='div[id^="day-group-thu"]')
    thursday_classes = thursday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')


elif day_name == 'Tuesday':
    # If Tue: Tuesday is "Today", Thursday is standard.
    tuesday_ = driver.find_element(By.CSS_SELECTOR,value='div[id^="day-title-today-"]')
    tuesday_classes = tuesday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')

    thursday_ = driver.find_element(By.CSS_SELECTOR,value='div[id^="day-group-thu"]')
    thursday_classes = thursday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')

elif day_name == 'Wednesday':
    # If Wed: Tuesday is standard, Thursday is "Tomorrow".
    tuesday_ = driver.find_element(By.CSS_SELECTOR,value='div[id^="day-group-tue"]')
    tuesday_classes = tuesday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')
    
    thursday_ = driver.find_element(By.CSS_SELECTOR,value='div[id^="day-title-tomorrow-"]')
    thursday_classes = thursday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')

elif day_name == 'Thursday':
    # If Thu: Tuesday is standard, Thursday is "Today".
    tuesday_ = driver.find_element(By.CSS_SELECTOR,value='div[id^="day-group-tue"]')
    tuesday_classes = tuesday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')
    
    thursday_ = driver.find_element(By.CSS_SELECTOR,value='div[id^="day-title-today"]')
    thursday_classes = thursday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')

else:
    # Fri/Sat/Sun: Both Tuesday and Thursday use their standard static IDs.
    tuesday_ = driver.find_element(By.CSS_SELECTOR,value='div[id^="day-group-tue"]')
    tuesday_classes = tuesday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')
    
    thursday_ = driver.find_element(By.CSS_SELECTOR,value='div[id^="day-group-thu"]')
    thursday_classes = thursday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')


# tue_classes = tuesday_.find_elements(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')
# thuT_classes = thursday_.find_element(By.CSS_SELECTOR,value='div[class^="ClassCard_card__"]')


'''
    Find the time element within the current class card element ('class_').
    
    This uses the By.CSS_SELECTOR method, which is highly efficient and flexible.
    The selector 'p[id^="class-time-"]' works as follows:
    
    1. 'p': Targets only <p> (paragraph) elements.
    2. '[...]' : Specifies an attribute selection.
    3. 'id^="class-time-"': Finds elements where the 'id' attribute 
       *starts with* ('^=') the string "class-time-".
       
    This handles dynamic IDs (e.g., "class-time-yoga-2025-12-09-0700") by
    relying on the static, consistent prefix, ensuring the scraper always
    finds the correct time field regardless of the class details.
'''

# --- Booking Logic: Tuesday ---
for class_ in tuesday_classes:
    # Extract time and name
    time_element = class_.find_element(By.CSS_SELECTOR, 'p[id^="class-time-"]')
    # Parsing string format (e.g., splitting "Time: 6:00 PM" to get "6:00PM")
    class_time = time_element.text.strip().split(' ')[1] + time_element.text.strip().split(' ')[2]
    class_name = class_.find_element(By.CSS_SELECTOR,'h3[id^="class-name-"]')

    # Check for target time
    if class_time == '6:00PM':
        book_class =  class_.find_element(By.TAG_NAME,value='button')
        
        # Check button state and perform action
        if book_class.text == 'Booked':
            print(f"Your {class_name.text} is Already Booked")
        elif book_class.text == 'Waitlisted':
            print(f"You are on the waitlist for {class_name.text}")
        elif book_class.text == "Join Waitlist":
            book_class.click()
            print(f"You have joined the waiting list for the {class_name.text} ") 
        else:
            # Default case: The button likely says "Book Now"
            book_class.click()
            print(f"You have successfully booked the class {class_name.text}")

# --- Booking Logic: Thursday ---
# Mirrors the Tuesday logic exactly
for class_ in thursday_classes:
    time_element = class_.find_element(By.CSS_SELECTOR, 'p[id^="class-time-"]')
    class_time = time_element.text.strip().split(' ')[1] + time_element.text.strip().split(' ')[2]
    class_name = class_.find_element(By.CSS_SELECTOR,'h3[id^="class-name-"]')

    if class_time == '6:00PM':
        book_class =  class_.find_element(By.TAG_NAME,value='button')
        
        if book_class.text == 'Booked':
            print(f"Your {class_name.text} is Already Booked")
        elif book_class.text == 'Waitlisted':
            print(f"You are on the waitlist for {class_name.text}")
        elif book_class.text == "Join Waitlist":
            book_class.click()
            print(f"You have joined the waiting list for the {class_name.text} ") 
        else:
            book_class.click()
            print(f"You have successfully booked the class {class_name.text}")

# driver.quit()
