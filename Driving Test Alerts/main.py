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
    #check if the authentication page has popped up
    if(sb.is_element_visible("#main-iframe") == True):
        print("Authentication required!")
        sb.switch_to_frame("#main-iframe")
        sb.click('span:contains("Click to verify")')
        
        try: #prevent crashing errors
            sb.wait_for_element_visible(".geetest_slider_track", timeout=10) #waits for puzzle slider to become visible
            if(sb.is_element_visible(".geetest_slider_button") == True):
                print("Puzzle completion required!") #debug
                slideAction = ActionChains(sb.driver)
                
                for i in range(0,10): #width from 0 to 100
                    if(sb.is_element_visible(".geetest_slider_button") == False):
                        print("Puzzle disappeared!") #debug
                        break
                    else:
                        slideAction.click_and_hold(sb.find_element(".geetest_slider_button")).move_by_offset(i * 10, 0).release().perform()
                        sleep(1.25) #ensures that puzzle gets to confirm
                
                if(sb.is_element_visible(".geetest_radar_tip") == True):
                    sb.click('span:contains("Retry")') #If puzzle fails just reclick to bypass.
        except:
            print("No puzzle or captcha found...")
            pass
            
        sb.switch_to_default_content()
    sleep(1)
    sb.wait_for_element_visible("body", timeout=6)
    try:
        sb.find_element_by_id("test-type-car").click()
    except:
        pass
    sleep(2000)
    

    
