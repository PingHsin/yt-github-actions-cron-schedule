# import smtplib, ssl
# import os


# port = 465
# smtp_server = "smtp.gmail.com"
# USERNAME = os.environ.get('USER_EMAIL')
# PASSWORD = os.environ.get('USER_PASSWORD')
# message = """\
# Subject: GitHub Email Report

# This is your daily email report.
# """

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(USERNAME,PASSWORD)
#     server.sendmail(USERNAME,USERNAME,message)

import smtplib, ssl
import os
import requests

# Weather information URL (free, no API key required)
weather_url = "http://wttr.in/Seattle?format=3"  # Gets weather in a simple format

# Get the current weather
response = requests.get(weather_url)
weather_data = response.text.strip()  # Extract the weather data as plain text

# Email configuration
port = 465  # SSL port for Gmail
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')  # Your Gmail address from environment variable
PASSWORD = os.environ.get('USER_PASSWORD')  # Your Gmail app password from environment variable

# Email message
message = f"""\
Subject: Seattle Weather Report

Current weather in Seattle:
{weather_data}
"""

# SSL context for secure connection
context = ssl.create_default_context()

# Sending the email
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, USERNAME, message)  # Send email to yourself (or modify as needed)
