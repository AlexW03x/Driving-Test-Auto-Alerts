class webScraperSettings:
    def __init__(self, choiceOfTest, drivingID, date, location, getEmails, cooldown):
        self.testType = choiceOfTest
        self.drivingLicenseID = drivingID
        self.preferredTestDate = date
        self.postCode = location
        self.receiveEmails = getEmails
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
    
    def getEmails(self):
        return self.receiveEmails
    
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
        
    def changeGetEmail(self, email):
        self.receiveEmails = email
        
    def changeCooldown(self, cooldown):
        self.scriptCooldown = cooldown
        
    
    
        
