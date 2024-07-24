from webScraper import *

def main():
    # driving class instance called, |Test Type|Driving License ID|Date|Location|ScriptCooldown
    drivingWebsite = webScrape("Car", "WALKE009303AP9SM", "unset", "unset", 30)
    checkDVLA = webScrape.checkWebsiteResponse("https://driverpracticaltest.dvsa.gov.uk/application?execution=e2s1")
    print(f"{checkDVLA}")
    
if __name__ == "__main__":
    main()