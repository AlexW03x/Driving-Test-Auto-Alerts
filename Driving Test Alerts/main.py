from webScraperSettings import *
from webScraperScript import *

global scraperSettings #Public class object call
scraperSettings = webScraperSettings("car (manual and automatic)", "", "", "", "")
        
def main():
    print("Welcome to Alex's Driving Test Availability Reader!")
    print("---------------------------------------------------")
    print("Please enter the details that will be prompted.")
    
    [licenseID, date, postcode, cooldown] = inputUserSettings()

    scraperSettings.changeID(licenseID)
    scraperSettings.changeDate(date)
    scraperSettings.changeLocation(postcode)
    scraperSettings.changeCooldown(cooldown)
    
    
    
    

def inputUserSettings():
    licenseID = ""
    date = ""
    postcode = ""
    cooldown = 0
    while(licenseID == "" and date == "" and postcode == "" and cooldown == 0):
        try:
            if(licenseID == ""):
                licenseID = str(input("Driving License ID: "))
            if(date == ""):
                date = str(input("Preferred Test Date (dd/mm/yy): "))
            if(postcode == ""):
                postcode = str(input("Post code, Example ABC DEF: "))
            if(cooldown ==  0):
                cooldown = 5 * 60 #5 minutes per entry requests 
        except:
            pass
        
    return [licenseID, date, postcode, cooldown]
    
    
    
if __name__ == "__main__":
    main() 

    
