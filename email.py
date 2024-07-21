# -*- coding: utf-8 -*-
"""Email.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VBcjBheoON4WpVfEcmcC1ZSeJ46wc_M-
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import json

with open('config.json') as f:
    config = json.load(f)

api_key = config

encoded_data = str(api_key).encode()
decoded_data = encoded_data.decode()

sender_email = decoded_data
password = decoded_data

recipients = [
    "sampurnsandesh@gmail.com"
]

subject = "Test email"
body = """
Hello,

This is a test email sent from Python script.

Best regards,
Your Name

"""

smtp_server = "smtp.gmail.com"
port = 587  # For starttls

def send_email(recipient_email):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

# Add body to email
        msg.attach(MIMEText(body, 'plain'))

                # Connect to the server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Disconnect from the server
        server.quit()

        print(f"Email successfully sent to {recipient_email}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")

# Send emails to all recipients
for recipient in recipients:
    send_email(recipient)