from webScraperSettings import *
from webScraperScript import *

global scraperSettings #Public class object call
scraperSettings = webScraperSettings("car (manual and automatic)", "", "", "", "", 0)
        
def main():
    print("Welcome to Alex's Driving Test Availability Reader!")
    print("---------------------------------------------------")
    print("Please enter the details that will be prompted.")
    
    inputUserSettings()
    
    print("The script will now begin!")
    executeScript(scraperSettings.getDrivingLicense(),
                  scraperSettings.getTestDate(),
                  scraperSettings.getTestLocation(),
                  scraperSettings.getEmails(),
                  scraperSettings.getScriptCooldown())
    
    
def inputUserSettings():
    licenseID = ""
    date = ""
    postcode = ""
    email = False
    cooldown = 0
    while(licenseID == "" and date == "" and postcode == "" and email == False and cooldown == 0):
        try:
            if(licenseID == ""):
                licenseID = str(input("Driving License ID: "))
                scraperSettings.changeID(licenseID)
                
            if(date == ""):
                date = str(input("Preferred Test Date (dd/mm/yy): "))
                scraperSettings.changeDate(date)
                
            if(postcode == ""):
                postcode = str(input("Post code, Example ABC DEF: "))
                scraperSettings.changeLocation(postcode)
                
            if(email == False):
                getEmails = str(input("Recieve email alerts to your email? (Y/N): "))
                if("y" in getEmails.lower() or "yes" in getEmails.lower()):
                    email = True
                    scraperSettings.changeGetEmail(email)
                
            if(cooldown ==  0):
                print("Terminal script cooldown per requests: 5 minutes!")
                cooldown = 5 * 60 #5 minutes per entry requests 
                scraperSettings.changeCooldown(cooldown)
        except:
            pass
        
    
    
    
if __name__ == "__main__":
    main() 

    
