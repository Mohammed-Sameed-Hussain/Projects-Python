import os
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.


class NotificationManager:
    """
    This class handles sending notifications (SMS and WhatsApp) via the Twilio API.
    """

    def __init__(self):
        """
        Initialize the Twilio Client using credentials from environment variables.
        """

        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        
        Args:
            message_body (str): The text content of the SMS message to be sent.
        """

        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)

    
    def send_whatsapp(self, message_body):
        """
        Sends a WhatsApp message through the Twilio Sandbox.
        
        Args:
            message_body (str): The text content of the message.
        """

        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)