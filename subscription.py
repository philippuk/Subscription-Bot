# import selenium webdriver
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
# set browser / browser options
from selenium.webdriver.chrome.options import Options

df = pd.read_csv("subscription.csv", usecols=[1])


options = Options()
driver_path = '/usr/local/bin/chromedriver'
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options, executable_path = driver_path)
stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
    )
# get page
driver.get("https://www.google.com")
time.sleep(30)

for channel in df["Channel Url"]:  
    try: 
        driver.get(channel)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/tp-yt-paper-button').click()
    except:
        continue
    
