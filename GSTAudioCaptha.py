from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://services.gst.gov.in/services/audiocaptcha

def getAudioCaptchaLink(driver, pan):
    pan_input = driver.find_element_by_id("for_gstin")
    pan_input.send_keys(pan)
    # fix for the element causing click failure
    wait = WebDriverWait(driver, 10)
    wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME, "dimmer-holder")))
    
    element = driver.find_element_by_xpath("//button[@ng-disabled='playingCap']")
    time.sleep(.5)
    element.click()
    elem = driver.find_element_by_id("audioCap")
    return elem.get_attribute('src')

def main():
    PANNumbers = ['AEYPC1578H', 'AHWPR3876J']
    
    driver = webdriver.Firefox()
    main_link = "https://services.gst.gov.in/services/searchtpbypan"
    driver.get(main_link)

    for pan in PANNumbers:
        audio_captcha_link = getAudioCaptchaLink(driver, pan)
        driver.get(audio_captcha_link)
        # next steps :
        # 1. get the captcha from the audio
        time.sleep(4) # waits on the captcha speaking out link 

        # 2. input the captcha in the captcha field 
        # 3. submit form and get to the new link
        # 4. fetch the gst number and return it

        driver.get(main_link)

    driver.close()

if __name__ == "__main__":
    main()