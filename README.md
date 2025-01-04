# Mass Vaccine Scraper
A Python script that monitors the Massachusetts vaccine finder website for available appointments at specific locations and sends SMS notifications when slots become available. Currently configured for the Marshfield vaccination site.

## Features
- Automated monitoring of vaxfinder.mass.gov
- Real-time appointment availability checking
- SMS notifications via email-to-text service
- Configurable refresh rate (default: 15 seconds)
- Stops after first availability is found
- Data persistence to prevent duplicate notifications

## Requirements
```
Python 3.x
beautifulsoup4
requests
lxml
```

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/mass-vaccine-scraper.git
cd mass-vaccine-scraper
```

2. Install dependencies:
```bash
pip install beautifulsoup4 requests lxml
```

3. Create a text file named `MassvacScraperDocMarsh.txt` in the project directory (empty file is fine)

## Configuration
Before running the script, you need to configure the following:

1. Email Settings (for SMS notifications):
   - Replace `<your email>` with your Gmail address
   - Replace `<email password>` with your email password or app-specific password
   - Replace `<phone number @ carrier email to text service>` with your carrier's email-to-text address
     - Example formats:
       - Verizon: `number@vtext.com`
       - AT&T: `number@txt.att.net`
       - T-Mobile: `number@tmomail.net`

2. Location Settings:
   - Current URL is set to Marshfield location
   - Modify the URL in the `Marshfield()` function to monitor different locations

## Usage
Run the script:
```bash
python vaccine_scraper.py
```

The script will:
1. Check the Marshfield vaccination site every 15 seconds
2. Compare new data with previous data to detect changes
3. Send SMS notification when vaccines become available
4. Automatically stop after sending the first notification

## Project Structure
```
mass-vaccine-scraper/
├── vaccine_scraper.py
├── MassvacScraperDocMarsh.txt
└── README.md
```

## Security Notes
- It's recommended to use an app-specific password for Gmail rather than your main password
- Consider storing sensitive information (email, password) in environment variables
- Be mindful of website terms of service regarding scraping frequency

## Known Issues
- Gmail may require "Less secure app access" or app-specific passwords
- Some email providers may block automated emails
- Website structure changes may break the scraper

## Future Improvements
- Support for multiple locations simultaneously
- Configuration file for easier setup
- More robust error handling
- Command line arguments for configuration
- Support for different notification methods

## Disclaimer
This tool is for educational purposes only. Be sure to comply with all website terms of service and local regulations regarding automated access to vaccination information.
