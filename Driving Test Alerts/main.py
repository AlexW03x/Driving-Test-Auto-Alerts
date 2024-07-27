from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from webScraper import *
from time import *
from seleniumbase import SB
from selenium.webdriver.common.action_chains import ActionChains

#this is to identify all of the components involved in BaseCase and SB
class Scrape(BaseCase):
    def test(self):
        self.uc_open("")
        


#main script we will be running
with SB(uc = True) as sb:
    sb.uc_open("https://www.gov.uk/book-driving-test")
    
    sb.wait_for_element_visible("body", timeout=6)
    sb.scroll_into_view(By.LINK_TEXT, "Start now")
    sleep(1)
    sb.click_link("Start now", timeout=3)
    sb.wait_for_element_visible("body", timeout=15)
    sleep(1)
    #check if the authentication page has popped up -- CURRENTLY WORKING AND BYPASSES PUZZLE EVEN IF FAILS!
    while(sb.is_element_visible("#main-iframe") == True):
        print("Authentication required!")
        try: #prevent crashes and attempts to reattempt if iframe still visible
            sb.switch_to_frame("#main-iframe")
            sb.click('span:contains("Click to verify")')
        except:
            pass
        try: 
            sb.wait_for_element_visible(".geetest_slider_track", timeout=10) #waits for puzzle slider to become visible
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
            
    sb.switch_to_default_content()
    sleep(1)
    print(sb.get_current_url())
    sb.wait_for_element_visible("body", timeout=8)
    print("Now onto the driving test portal!") #debug
    try:
        if(sb.is_element_visible("#test-type-car") == True):
            print("Accessing car (manual and automatic) tests...") #debug
            sb.click('#test-type-car')
            sleep(1)
    except:
        pass
    sleep(2000)
    

    
