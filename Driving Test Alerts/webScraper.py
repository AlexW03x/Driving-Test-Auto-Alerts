import requests
from bs4 import BeautifulSoup

class webScrape:
    def __init__(self, choiceOfTest, drivingID, date, location, cooldown):
        self.testType = choiceOfTest
        self.drivingLicenseID = drivingID
        self.preferredTestDate = date
        self.postCode = location
        self.scriptCooldown = cooldown
        
    def checkWebsiteResponse(websiteURL):
        try:
            web = requests.get(websiteURL)
            web.raise_for_status()
            return web.text
        except:
            return f"Couldn't fetch url: {websiteURL}"
        
    def identifyWebElement(htmlCode, element):
        try:
            return BeautifulSoup(htmlCode, 'html.parser').find(element).get_text(strip=True)
        except:
            return "Error in parsing website!"
        
    def identifyWebElementWithID(htmlCode, element, ID):
        try:
            return BeautifulSoup(htmlCode, 'html.parser').find(element, {"id": ID}).get_text(strip=True)
        except:
            return "Error in parsing website!"
        
        
    #getters
    def getTestType(self):
        return self.testType
    
    def getDrivingLicense(self):
        return self.drivingLicenseID
    
    def getTestDate(self):
        return self.preferredTestDate
    
    def getTestLocation(self):
        return self.postCode
    
    def getScriptCooldown(self):
        return self.scriptCooldown
        
    #setters
    def changeTest(self, choiceOfTest):
        self.testType = choiceOfTest
        
    def changeID(self, drivingID):
        self.drivingLicenseID = drivingID
    
    def changeDate(self, date):
        self.preferredTestDate = date
    
    def changeLocation(self, location):
        self.postCode = location
        
    def changeCooldown(self, cooldown):
        self.scriptCooldown = cooldown
        