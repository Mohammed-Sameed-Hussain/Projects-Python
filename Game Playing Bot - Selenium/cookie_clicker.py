from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import time, sleep

# ----------------------------
# 1. BROWSER SETUP
# ----------------------------

# Configure Chrome options to keep the browser open after the script finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the specific Cookie Clicker URL
driver.get("https://ozh.github.io/cookieclicker/")

# ----------------------------
# 2. INITIALIZATION & LANGUAGE SELECTION
# ----------------------------

# Handle the initial language selection modal
try:
    # Initialize a WebDriverWait instance with a 10-second timeout
    # This creates an "Explicit Wait" which is better than sleep() because it only waits as long as needed
    wait = WebDriverWait(driver, 10)
    
    # Wait until the English language button is found in the DOM AND is clickable
    language_select = wait.until(
        EC.element_to_be_clickable((By.ID, "langSelect-EN"))
    )
    
    language_select.click()
    print("Language selected successfully!")

except Exception as e:
    # General catch in case the modal doesn't appear or the ID changes
    print(f"Language selection skipped or failed: {e}")

# brief pause to allow the game interface to render and animations to finish
sleep(1)

# Locate the main interaction element: The Big Cookie
# 
cookie_clicker = driver.find_element(By.ID, value='bigCookie')

# ----------------------------
# 3. GAME STRATEGY CONFIGURATION
# ----------------------------

# Set up timing variables
wait_time = 5               # Interval: Check the store for upgrades every 5 seconds
timeout = time() + wait_time # The actual timestamp for the next store check
five_min = time() + 60 * 5   # Total runtime: Stop the bot after 5 minutes

# ----------------------------
# 4. MAIN GAME LOOP
# ----------------------------

while True:
    # Continually click the cookie to generate currency
    cookie_clicker.click()

    # Check if 5 seconds have passed to look for upgrades
    if time() > timeout:
        try:
            # --- A. Analyze Current Resources ---
            
            # Get the current number of cookies (e.g., "150 cookies")
            # We split the text string to isolate the number
            cookies_element = driver.find_element(By.ID, value='cookies')
            current_cookies = cookies_element.text.split(' ')[0].strip()
            
            # --- B. Analyze The Store ---
            
            # Locate the store container
            store = driver.find_element(By.ID, value='products')
            
            # specific CSS Selector explanation:
            # .product -> finds items in the store
            # .unlocked -> finds items that are visible
            # .enabled -> finds items we actually have enough cookies to buy right now
            rewards = store.find_elements(By.CSS_SELECTOR, value='.product.unlocked.enabled')
            
            # --- C. Purchase Strategy ---
            
            # Variable to hold the item we decide to buy
            best_item = None
            
            # We iterate through the available rewards in REVERSE.
            # Why? Because in Cookie Clicker, the most expensive items (at the bottom of the list)
            # generally give the best Return on Investment (ROI) / Cookies Per Second.
            for reward in reversed(rewards):
                best_item = reward
                break # We take the first one (the most expensive one) and stop looking

            if best_item:
                # Get the ID before clicking for the print statement (avoid stale element errors)
                item_id = best_item.get_attribute('id')
                best_item.click()
                print(f"Purchased upgrade: {item_id}")
        
        except (NoSuchElementException, StaleElementReferenceException):
            # Handle cases where the DOM updates while we are trying to read it
            print("Note: Element not found or DOM updated too quickly.")
            
        # Reset the timer for the next 5-second interval
        timeout = time() + wait_time
    
    # ----------------------------
    # 5. END CONDITION
    # ----------------------------
    
    # Check if the total 5-minute runtime has elapsed
    if time() > five_min:
        try:
            # Fetch final score for reporting
            cookies_element = driver.find_element(By.ID, value="cookies")
            print("--- Time's Up! ---")
            print(f"Final Score: {cookies_element.text}")
        except NoSuchElementException:
            print("Could not retrieve final score.")
            
        # Break the While True loop to stop the script
        break

# Optional: driver.quit() closes the browser. 
# It is commented out because we used 'detach=True' to keep it open.
# driver.quit()
