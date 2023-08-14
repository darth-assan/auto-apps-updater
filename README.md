# applications-updater: Homebrew Update Script with Twilio Notifications

This script automates the process of updating outdated Homebrew apps on your macOS system and sends an SMS notification using Twilio. It ensures your software is up-to-date while keeping you informed of the changes. Follow these steps to install and run the script on your system.

## Prerequisites

- Python 3.x installed on your system
- A Twilio account with the necessary credentials (account SID, auth token, and phone numbers)
- Homebrew installed on your macOS system

## Installation

Clone the Repository:

```bash
git clone https://github.com/darth-assan/applications-updater.git
cd applications-updater
```

## Install Dependencies:

Use pip to install the required Python libraries. Run this command in your terminal:

```bash
pip3 install -r requirements.txt
```

## Create Environment Variables:

Create a .env file in the script directory with the following content:

```env
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
RECIPIENT_PHONE_NUMBER=your_recipient_phone_number
```

> Replace your_twilio_account_sid, your_twilio_auth_token, your_twilio_phone_number, and your_recipient_phone_number with your actual Twilio credentials and phone numbers.

## Run the Script:

Open your terminal, navigate to the script directory, and run the script:

```bash
python script_name.py
```

The script will update outdated Homebrew apps and send an SMS notification via Twilio.

## Usage

Running the script will check for outdated Homebrew apps, update them, and send an SMS notification with the update details using Twilio.

> You can create a cronjob to automatically run the script the script.
