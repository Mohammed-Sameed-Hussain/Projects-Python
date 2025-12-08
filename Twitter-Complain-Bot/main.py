from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import os

# --- Configuration Constants ---
SPEED_TEST = 'https://www.speedtest.net/'
TWITTER_PAGE = '' # Base URL is handled in the method, this is a placeholder
PROMISED_UPLOAD = 35    # The upload speed (Mbps) your ISP promised
PROMISED_DOWNLOAD = 220 # The download speed (Mbps) your ISP promised

# Twitter Credentials (Make sure to use environment variables in production for safety)
TWITTER_EMAIL = "yourmail"
TWITTER_PASSWORD = 'yourpassword'


class InternetSpeedTwitterBot():
    def __init__(self):
        # Initialize the Chrome driver with custom options
        chrome_options = self.set_chrome_options()
        self.driver = webdriver.Chrome(options=chrome_options)
        
        # Instance variables to store the results of the speed test
        self.up = 0
        self.down = 0 
    
    def set_chrome_options(self):
        """
        Configures Chrome options.
        Sets up a persistent user profile so cookies/sessions *can* be saved 
        (though the script performs login logic every time).
        """
        # Define a path for the Chrome profile in the current working directory
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        
        # Create the directory if it doesn't exist
        if not os.path.exists(user_data_dir):
            os.makedirs(user_data_dir)

        chrome_options = webdriver.ChromeOptions()
        # 'detach' keeps the browser open after the script finishes
        chrome_options.add_experimental_option("detach", True)
        # Apply the persistent profile argument
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        return chrome_options
    
    def test_speed(self):
        """
        Navigates to Speedtest.net and runs the test.
        Returns True if successful, exits if it times out.
        """
        self.driver.get(SPEED_TEST)

        # Initialize a wait driver (10 seconds timeout)
        wait = WebDriverWait(self.driver, 10)

        # --- Handle Cookie Consent Banner ---
        try:
            # Wait for the "Reject All" button (GDPR compliance)
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, 'onetrust-reject-all-handler')))
            cookie_button.click()
        except TimeoutException:
            # If no banner appears (e.g., using persistent profile), continue
            print("No cookie banner found, proceeding...")

        # --- Start the Test ---
        # Locate the "Go" button using XPath and click it
        start_test = wait.until(EC.element_to_be_clickable((By.XPATH,'//span[contains(text(),"Go")]/ancestor::a')))
        start_test.click()
        print("Test running... this will take about 45-60 seconds.")

        # --- THE ROBUST LOGIC (Wait for Completion) ---
        # Instead of a hard sleep, we wait for the URL to change to the results page.
        # Speedtest.net redirects to 'speedtest.net/result/...' when finished.
        wait = WebDriverWait(self.driver, 60) # Increased timeout for the full test duration
        try:
            wait.until(EC.url_contains("/result/"))
            print("Test cycle complete (URL updated).")
        except TimeoutException:
            print("Test took too long or URL didn't change.")
            print("Try again")
            exit() # Stop script if test fails

        TEST_SUCCESSFULL = False

        try:
            # --- Extract Data ---
            # Locate the results elements. They are usually visible after the URL change.
            down_speed = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
            up_speed = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

            print("--------------------------------")
            print(f"Download Speed: {down_speed} Mbps")
            print(f"Upload Speed:   {up_speed} Mbps")
            print("--------------------------------")
            
            # Store results in the class instance
            self.down = down_speed
            self.up = up_speed

            TEST_SUCCESSFULL = True
            return TEST_SUCCESSFULL
        
        except Exception as e:
            print(f"Error extracting data: {e}")
            return TEST_SUCCESSFULL

    def complain_tweet_bot(self):
        """
        Logs into Twitter/X and posts a complaint if speeds were low.
        """
        self.driver.get('https://x.com')

        wait = WebDriverWait(self.driver, 10)

        # --- Handle Twitter Cookie Banner ---
        try:
            # Looks for Refuse/Reject/Ablehnen (German support included)
            cookie_xpath = '//span[contains(text(),"Refuse") or contains(text(),"Ablehnen") or contains(text(),"refuse") or contains(text(),"reject") or contains(text(),"Reject")]'
            cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH,cookie_xpath)))
            cookie_button.click()
        except TimeoutException:
            print("No cookie banner found, proceeding...")
        
        # --- Login Flow ---
        # Click 'Sign in'
        sign_in = wait.until(EC.element_to_be_clickable((By.XPATH,'//span[contains(text(),"Sign in")]')))
        sign_in.click()
        
        # Enter Username/Email
        user_name = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@autocomplete="username"]')))
        user_name.send_keys(TWITTER_EMAIL)

        time.sleep(1) # Slight pause for animation stability
        
        # Click Next
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH,'//span[contains(text(),"Next")]')))
        next_button.click()

        # --- Password Entry ---
        print("Entering Password...")
        # Wait for password field to appear
        password = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@autocomplete="password"]')))
        password.send_keys(TWITTER_PASSWORD)
        
        # Press ENTER to log in (more reliable than finding the login button)
        password.send_keys(Keys.ENTER)

        # --- Compose Tweet ---
        print("Login successful. Checking speed criteria...")
        
        # Wait for the tweet text area to be visible (confirms successful login)
        try:
            tweet_box = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="tweetTextarea_0"]')))
        except TimeoutException:
            print("Could not find tweet box. Login might have failed or verify check required.")
            return

        # Format the complaint message
        tweet_message = (
                f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up "
                f"when I pay for {PROMISED_DOWNLOAD}down/{PROMISED_UPLOAD}up?"
            )
            
        # Type the message into the box
        tweet_box.send_keys(tweet_message)
            
        # Click the "Post" button using the stable data-testid attribute
        post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]')))
        post_button.click()
            
        print("Tweet sent successfully!")

        # Keep browser open briefly to visually confirm the tweet
        time.sleep(5)


# --- EXECUTION MAIN LOGIC ---
bot = InternetSpeedTwitterBot()

# Step 1: Run the speed test
if bot.test_speed():
    # Step 2: Compare results against promised speeds
    if bot.down < PROMISED_DOWNLOAD or bot.up < PROMISED_UPLOAD:
        print("Speeds are low. Time to complain.")
        # Step 3: Login and Tweet if speeds are insufficient
        bot.complain_tweet_bot()
    else:
        print("Speeds are good. No complaint needed.")
else:
    print("Speed test failed.")
