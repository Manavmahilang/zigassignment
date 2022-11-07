from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

"""def launchbrowser():
    #chromeoptions = webdriver.ChromeOptions() 

    #chromeoptions.add_experimental_option("prefs",{"download.default_directory" : "C:/Users/manav/OneDrive/Desktop/My projects/zig"})

    path='./chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.maximize_window()

    try:
        driver.get("https://www.google.com")
        
        driver.get("https://www.nseindia.com/market-data/securities-available-for-trading")
        time.sleep(2)
        driver.find_element(By.LINK_TEXT  ,"Securities available for Equity segment (.csv)").click()
        
        time.sleep(10)
        
        #driver.close()

    except:
        print("Invalid URL")
    return driver"""


def getbhav():
    path='./chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.maximize_window()
    
    try:
        driver.get("https://www.nseindia.com/all-reports")
        WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//a[@aria-label='Download File']")))
        #driver.find_element(By.ID, "crEquityDailySearch").send_keys("bhavcopy")
        #driver.find_element(By.CLASS_NAME, "pdf-download-link").click()

        
        
        time.sleep(20)
    except:
        print("Invalid URL")
    return driver



#g1=launchbrowser()
g2=getbhav()
