###################################################
# DVSA - Driving Test Script V1.0 + Puzzle Bypass #
# Written By Alex Walker @AlexW03x ~~ Open Source #
###################################################

from time import *
from seleniumbase import SB
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

def executeScript(drivingLicense, dateOfTest, postcode):
    with SB(uc = True) as sb:
        sb.uc_open("https://www.gov.uk/book-driving-test")
        sb.wait_for_element_visible("body", timeout=6)
        sb.scroll_into_view(By.LINK_TEXT, "Start now")
        sleep(0.5)
        sb.click_link("Start now", timeout=3)
        sb.wait_for_element_visible("body", timeout=15)
        sleep(0.5)
        
        #check if the authentication page has popped up -- CURRENTLY WORKING AND BYPASSES PUZZLE EVEN IF FAILS!
        while(sb.get_current_url() == "https://driverpracticaltest.dvsa.gov.uk/application"):
            print("Authentication required!")
            try: #prevent crashes and attempts to reattempt if iframe still visible
                sb.switch_to_frame("#main-iframe")
                sb.click('span:contains("Click to verify")')
            except:
                pass
            try: 
                sb.wait_for_element_visible(".geetest_slider_track", timeout=5) #waits for puzzle slider to become visible
                if(sb.is_element_visible(".geetest_slider_button") == True):
                    print("Puzzle completion required!") #debug
                    slideAction = ActionChains(sb.driver)
                
                    for i in range(0,10): #width from 0 to 100
                        if("execution=" in sb.get_current_url()):
                            break
                        if(sb.is_element_visible(".geetest_slider_button") == False):
                            print("Puzzle disappeared!") #debug
                            break
                        else:
                            slideAction.click_and_hold(sb.find_element(".geetest_slider_button")).move_by_offset(i * 10, 0).release().perform()
                            sleep(2) #ensures that puzzle gets to confirm - has to be equal to or more than 2 seconds to prevent CSS selector bug
                
                    if(sb.is_element_visible(".geetest_radar_tip") == True):
                        sb.click('span:contains("Retry")') #If puzzle fails just reclick to bypass.
            except:
                print("No puzzle or captcha found...")
                pass
            
        #Application Section 1 - Basic Details
        sb.switch_to_default_content()
        sleep(1)
        print(sb.get_current_url()) #debug
        sb.wait_for_element_visible("body", timeout=4)
        print("Now onto the driving test portal!") #debug
        if(sb.is_element_visible("#test-type-car") == True):
            print("Accessing car (manual and automatic) tests...") #debug
            sb.click('#test-type-car')
            sleep(1)

        #Application Section 2 - Driving License Number and Requirements
        print(sb.get_current_url()) #debug
        sb.wait_for_element_visible("body", timeout=4)
        if(sb.is_element_visible("#driving-licence") == True):
            sb.type("#driving-licence", drivingLicense)
            print(f"Typing id='{drivingLicense}' into license field...") #debug
            sleep(0.5)
            sb.click("#extended-test-no") #no extended test requirements
            print("Selecting no extended tests...") #debug
            sleep(0.5)
            sb.click("#special-needs-none") #no special needs requirements
            print("Selecting no special needs...") #debug
            sleep(0.5)
            sb.click("#driving-licence-submit")
            sleep(1)
            
        #Application Section 3 - Preferred Test Date
        print(sb.get_current_url()) #debug
        sb.wait_for_element_visible("body", timeout=4)
        if(sb.is_element_visible("#test-choice-calendar") == True):
            sb.type("#test-choice-calendar", dateOfTest)
            print("Inputting preferred date...") #debug
            sleep(0.5)
            sb.click("#driving-licence-submit")
            sleep(1)
            
        #Application Section 4 - Postcode
        print(sb.get_current_url()) #debug
        sb.wait_for_element_visible("body", timeout=4)
        if(sb.is_element_visible("#test-centres-input") == True):
            sb.type("#test-centres-input", postcode)
            print("Inputting postcode...")
            sleep(0.5)
            sb.click("#test-centres-submit")
            sleep(1)
            
        #Application Section 5 - Availabilities
        print(sb.get_current_url()) #debug
        sb.wait_for_element_visible("body", timeout=4)
        allAvailabilities = sb.find_elements("span.underline h4, span.underline h5") #scrape all text within the table
        for tests in allAvailabilities:
            print(tests.text)
        sleep(2000)
