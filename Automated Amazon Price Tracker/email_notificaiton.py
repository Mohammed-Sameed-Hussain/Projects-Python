import smtplib
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve sensitive credentials from environment variables
# (Note: This requires 'import os' to work, which is currently missing in imports)
email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")

# Define the SMTP server address for Gmail
SMPT_ADDRESS = 'smtp.gmail.com'

class sendNotificaiton():
    """
    A class responsible for sending email alerts via SMTP.
    """

    def send_notificaiton(self, message, url):
        
        # Establish a connection to the SMTP server using port 587 (TLS)
        with smtplib.SMTP(SMPT_ADDRESS, port=587) as connection:
            # Secure the connection with Transport Layer Security
            connection.starttls()
            
            # Log in to the email account
            result = connection.login(email, password)
            
            # Send the email
            # The message is encoded in utf-8 to handle special characters (like € or German text)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )
