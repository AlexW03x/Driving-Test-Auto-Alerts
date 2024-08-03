# Driving-Test-Auto-Alerts
Finding a driving test in the UK is a struggle and this was a fun project idea given to me by my stepdad. It is a python web-scraping script that will run automatically and send alerts to your email using an SMTP server currently working with gmail and using gmail app passwords.

# Gif Demo
![The program](https://github.com/AlexW03x/Driving-Test-Auto-Alerts/blob/main/Driving%20Test%20Alerts/Screenshots/Demo.gif.gif)

# NOTICE
> The version of this script is a lite edition of a more advanced one that I am working on, this will showcase as a terminal that will have its own runtime and limited functionality, its main job is to allow users to input their details and then the script will run every 5 minutes to alert your email.

## How does it work?
> You will execute main.py to run the script and then it will ask for input fields to be answered: driving license, preferred date, location and recieve emails yes or no, the data inputted isn't collected or transmitted as seen in the code and then the scraper will begin to work with an average run time of 1 minute.

### How To Recieve Email Alerts?
> Within the script file, please change the email server to whatever is necessary to yours or if you use gmail enter your gmail email and then for the gmail password you will need to create an app password rather than using your own password. This can be achieved through: https://myaccount.google.com/apppasswords and then enabling 2FA to allow this to work.

REQUIRED INSTALLS:
```
1. py -m pip install selenium
2. py -m pip install seleniumbase
3. py -m pip install webdriver-manager
4. py -m pip install undetected-chromedriver
```

## Bugs
> Warning: If the imperva puzzle shows a clickable image one please restart the script as it will never get solved for the bypass.

## Programmming Methods
> Written in Python using OOP and external modules for web scraping
> Code kept small and clean for clarity
