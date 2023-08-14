#!/usr/bin/env python3

import os
import subprocess
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime

# Your Homebrew update logic
subprocess.run(["brew", "update"])
outdated_apps = subprocess.run(
    ["brew", "outdated"], capture_output=True, text=True
).stdout.splitlines()

if len(outdated_apps) > 0:
    print("Updating outdated apps...")
    for app in outdated_apps:
        subprocess.run(["brew", "upgrade", app])
    print("Updates complete!")
else:
    print("No outdated apps found.")

# Your Twilio credentials
load_dotenv()
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
recipient_phone_number = os.getenv("RECIPIENT_PHONE_NUMBER")

# Send SMS using Twilio
client = Client(twilio_account_sid, twilio_auth_token)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = f"🚀 Homebrew apps were updated at {current_time}\n{'🔄 Updated apps: ' + ', '.join(outdated_apps) if outdated_apps else '✅ All apps are up to date.'}"


twilio_message = client.messages.create(
    body=message, from_=twilio_phone_number, to=recipient_phone_number
)

print("SMS sent:", twilio_message.sid)
