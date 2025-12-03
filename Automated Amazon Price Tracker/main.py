from amazon_scrape import Scrape
from email_notificaiton import sendNotificaiton

# Constant variable defining the price threshold you are willing to pay
BUY_PRICE = 1100

# Initialize the scraping class to fetch current product data
amazon_web = Scrape()

# Check if the scraped price is lower than your target buy price
if amazon_web.price < BUY_PRICE:
    # Construct the alert message with the product title and current price
    message = f"{amazon_web.title} is on sale for {amazon_web.price}!"
    
    # Initialize the notification manager
    notification_manager = sendNotificaiton()
    
    # Trigger the email. 
    # Note: This passes the 'practice_URL' defined in your scraper, 
    # not necessarily the live product URL.
    notification_manager.send_notificaiton(message=message, url=amazon_web.practice_URL)
