import smtplib
import os
from email.mime.text import MIMEText

# Retrieve secrets from the environment variables set in the YAML
to_email = os.environ.get('BLOGGER_EMAIL')
from_email = os.environ.get('SENDER_EMAIL')
password = os.environ.get('SENDER_PASSWORD')

# Your Blog Content
subject = "My First Automated Post"
body = "This post was sent automatically from GitHub Actions!"

# Set up the email
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

# Send via Gmail SMTP
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
    print("Post successfully sent to Blogger!")
except Exception as e:
    print(f"Error: {e}")
