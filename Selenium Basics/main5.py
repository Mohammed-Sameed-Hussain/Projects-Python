from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# --- 1. Browser Setup ---
# Create an instance of ChromeOptions to customize how the browser behaves
chrome_options = webdriver.ChromeOptions()

# The "detach" option keeps the browser open after the script finishes.
# Without this, Selenium automatically closes the window when the program ends.
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the options defined above
driver = webdriver.Chrome(options=chrome_options)

# Navigate the browser to the specific URL containing the form
driver.get("https://secure-retreat-92358.herokuapp.com/")


# --- 2. Locating Elements ---
# Find the 'First Name' input field by looking for the HTML attribute name="fName"
first_name = driver.find_element(By.NAME, value='fName')

# Find the 'Last Name' input field by looking for the HTML attribute name="lName"
last_name = driver.find_element(By.NAME, value='lName')

# Find the 'Email' input field by looking for the HTML attribute name="email"
email = driver.find_element(By.NAME, value='email')


# --- 3. Interacting with Elements ---
# Simulate typing "Bruce" into the identified first name field
first_name.send_keys("Bruce")

# Simulate typing "Lee" into the identified last name field
last_name.send_keys("Lee")

# Simulate typing the email address into the identified email field
email.send_keys('BruceLee@gmail.com')


# --- 4. Submitting the Form ---
# Locate the submit button using a CSS Selector.
# The string 'form button' targets any <button> element inside a <form> element.
button = driver.find_element(By.CSS_SELECTOR, value='form button')

# Simulate a mouse click on the button to submit the form data
button.click()


# --- 5. Cleanup ---
# driver.quit() is commented out so the browser remains open (due to the detach option)
# allowing you to visually verify that the form was submitted.
# driver.quit()