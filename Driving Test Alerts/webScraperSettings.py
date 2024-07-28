from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class webScrape:
    def __init__(self, choiceOfTest, drivingID, date, location, cooldown):
        self.testType = choiceOfTest
        self.drivingLicenseID = drivingID
        self.preferredTestDate = date
        self.postCode = location
        self.scriptCooldown = cooldown
        
    #website functions
        
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
        
    
    
        
