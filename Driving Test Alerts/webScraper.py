import requests
from bs4 import BeautifulSoup

class webScrape:
    def __init__(self):
        self.testType = ""
        self.drivingLicenseID = ""
        self.preferredTestDate = ""
        self.scriptCooldown = 0
        