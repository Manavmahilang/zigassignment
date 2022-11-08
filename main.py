from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
from jugaad_data.nse import bhavcopy_save
from jugaad_data.holidays import holidays
from datetime import date
from random import randint
import os,time
import pandas as pd


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

    data_path=os.path.join('C:',os.sep,'Users','manav','OneDrive','Desktop','My projects','zig','bhavdata')
    bhavcopy_save(date(2022,11,8),data_path)
    date_range=pd.bdate_range(start= '8/10/2022',end='08/11/2022',freq='C',holidays=holidays(2022))

    dates_2022=[x.date() for x in date_range]
    for dates in dates_2022:
        try:
            bhavcopy_save(dates, data_path)
            time.sleep(randint(1,4)) #adding random delay of 1-4 seconds
        except (ConnectionError, requests.exceptions.ReadTimeout) as e:
            time.sleep(10) #stop program for 10 seconds and try again.
            try:
                bhavcopy_save(dates, data_path)
                time.sleep(randint(1,4))
            except (ConnectionError, requests.exceptions.ReadTimeout) as e:
                print(f'{dates}: File not Found')


#g1=launchbrowser()
g2=getbhav()
