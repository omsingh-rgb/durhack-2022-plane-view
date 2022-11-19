# Webscrape using selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import requests
    
def main():
    driver = webdriver.Chrome()
    driver.get("https://www.radarbox.com/flight/AC851")
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    driver.close()

def get_flight_details(flight_number:str):
    url = f"https://www.radarbox.com/flight/{flight_number}"
    req = requests.get(url)
    #print(req.text)

    parsing = req.text.split("<script>")
    parsing = [p for p in parsing if "lat" in p and flight_number in p and "lng" in p]
    print(parsing)


if __name__=="__main__":
    # main()
    get_flight_details("AC851")
