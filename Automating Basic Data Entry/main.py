from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os

# URL of the Google Form where property data will be submitted
GOOGLE_FORMS = 'https://docs.google.com/forms/d/e/1FAIpQLSfSA9Q1beCfAUB2HVbB4mSAflboIOs7FTabX69AUFl3ynQM_g/viewform?usp=dialog'

# URL of the Zillow clone website being scraped
ZWILLIO_CLONE = 'https://appbrewery.github.io/Zillow-Clone/'


class Scrape():
    def __init__(self):
        # Run scraping immediately when object is created
        self.properties_data = self.scrape_zwillio()

    def scrape_zwillio(self):
        # Headers used to mimic a real browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }

        # Send HTTP GET request to Zillow clone website
        response = requests.get(ZWILLIO_CLONE, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all property listing containers
        properties = soup.find_all(name='div', class_='StyledPropertyCardDataWrapper')
        
        properties_data = []
        properties_dict = {}

        # Loop through each listing found
        for listing in properties:
            try:
                # Extract property link using CSS attribute selector
                property_link = listing.select_one('a[data-test="property-card-link"]')['href'].strip()

                # Extract property address
                address = listing.select_one('address').text.strip()

                # Extract raw price text
                raw_price = listing.select_one('span[data-test="property-card-price"]').text.strip()

                # Use regex to extract only the dollar value at the beginning (e.g., '$2,100+ /mo')
                match = re.match(r"^(\$[0-9,]+)", raw_price)

                if match:
                    price = match.group(1)  # Clean price extracted from group
                else:
                    price = raw_price  # If regex fails, keep raw text

                # Create dictionary for this listing
                properties_dict = {
                    "link": property_link,
                    "address": address,
                    "price": price
                }

                # Add to main list
                properties_data.append(properties_dict)
            
            except AttributeError:
                # If any field is missing, skip this listing
                print("Error Occured retreiving the data of this property. Skipping to the next listing.")
                continue
        
        return properties_data

    def fill_google_form(self):
        # Keep Chrome browser open after script ends
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        # Create Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            # Open Google Form
            driver.get(GOOGLE_FORMS)

            # Wait until form title is visible
            wait = WebDriverWait(driver, 10)
            form_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="heading"]')))

            print("Form loaded successfully!")
            print(f"Form Title: {form_title.text}")

        except TimeoutException:
            # If form does not load on time
            print("The form took too long to load or the element was not found.")
            exit()
    
        except Exception as e:
            # Catch any unexpected errors
            print(f"An error occurred: {e}")
            exit()
        
        # Loop through each scraped property and submit to the form
        for i, listing in enumerate(self.properties_data):
            try:
                # Identify the main form element
                form = driver.find_element(By.XPATH, '//form')

                # Find all input fields inside the form
                inputs = form.find_elements(By.XPATH, './/input[@type="text"]')
                
                # Mapping Google Form fields (ASSUMES FIXED ORDER: address, price, link)
                address = inputs[0]
                price = inputs[1]
                link = inputs[2]

                # Fill fields with scraped data
                address.send_keys(listing['address'])
                price.send_keys(listing['price'])
                link.send_keys(listing['link'])

                # Locate submit button by text (handles multiple languages)
                submit_button = form.find_element(By.XPATH, './/span[contains(text(),"Senden") or contains(text(),"Submit")]')
                
                # Submit the form
                submit_button.click()

                # If this is the last entry, exit loop
                if i + 1 == len(self.properties_data):
                    print("Data Submitted. End of Python Script")
                    break
                else:
                    # After submission, click "submit another response"
                    submit_another_form = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, '//a[contains(text(), "Submit another response") or contains(text(), "Weitere Antwort senden")]')
                    ))
                    submit_another_form.click()

                    # Wait for new blank form to load
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[role="heading"]')))
            
            except (TimeoutException, NoSuchElementException) as e:
                # If submission fails, skip this entry and continue
                print(f"Failed to submit entry {i+1}: {listing['address']}. Error: {e}")
                continue

# Create object → scrape data → submit form
zwillio = Scrape()
zwillio.fill_google_form()

