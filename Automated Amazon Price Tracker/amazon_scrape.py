from bs4 import BeautifulSoup
import requests

class Scrape():
    """
    A class responsible for fetching product details from Amazon.
    """
    def __init__(self):
        # The URL used for the email link (currently set to a practice page)
        self.practice_URL = 'https://appbrewery.github.io/instant_pot/'
        
        # The actual live Amazon.de URL you are scraping (Fujifilm X-T50)
        self.live_url = 'https://www.amazon.de/-/en/74491-FUJIFILM-X-T50-Body-Silver/dp/B0D45MJNM7/ref=sr_1_1?crid=2Q66OJAHV6SJF&dib=eyJ2IjoiMSJ9.-6ah4mIrEtblvNIUNRfDGUIavuugV-_r3ZdI0xDasNDZJI24FR94xZMG1iB9L2y1fljD9PE6ocoOQLWhj6zgf37ZmzTO_O5uSyszsLMoa-picik5R2FLwLiAXJRiAR5RQ_FUvsEcr27l1g4aHF2_qLjbOLAY9ivpJmPqSOr14gbz_taFcwwBy-5vkuAdJl0owr_1p3qSFNS0-jMQAJLmABjmZJLE3z2F8iZcL8xgrTo.FtG1VzdSDRkzNTRWHpguD2tD-GBv8Rzav_WFq2NCdRk&dib_tag=se&keywords=Fujifilm%2BX-T50&qid=1764756514&sprefix=fujifilm%2Bx-t50%2Caps%2C131&sr=8-1&th=1'
        
        # Initialize title as empty string
        self.title = ''
        
        # Automatically fetch and set the price upon initialization
        self.price = self.get_price_title()

    def get_price_title(self):
        """
        Connects to the URL, parses HTML, and extracts the price and title.
        Returns the price as a float.
        """
        
        # Headers are required to mimic a real browser request to avoid 
        # being blocked by Amazon's anti-bot protection.
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
            "Accept-Language": "en-US"
        }
        
        # Send HTTP GET request to the live URL
        response = requests.get(self.live_url, headers=headers)

        # Create BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the HTML span containing the price (using Amazon's specific class name)
        price_str = soup.find('span', class_='a-offscreen').get_text()

        # Clean the price string: remove the Euro symbol (€)
        price = price_str.strip('€')
        
        # Remove commas (used as thousand separators in some formats) to convert to float
        price = float(price.replace(",", ""))

        # Find the product title by ID and strip whitespace
        title = soup.find(id="productTitle").get_text().strip()
        self.title = title
        
        # Debugging prints
        # print(price)
        # print(type(price))

        return price
