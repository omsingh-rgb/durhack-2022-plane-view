from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
    
def get_flight_details(flight_number:str):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.radarbox.com/flight/{flight_number}")
    i = 0
    while i < 10:
        try:
            elem = driver.find_element(By.ID, "fc-details")
            break
        except:
            sleep(1)
            i += 1
    # get the text
    text = elem.text

    text_p = text.strip().split("\n")
    
    output = {"Flight Number":flight_number}

    #assert output[0].lower() == "altitude"
    output["Altitude"] = text_p[1]

    #assert output[2].lower() == "latitude"
    output["Latitude"] = text_p[3]

    #assert output[4].lower() == "longitude"
    output["Longitude"] = text_p[5]
    
    print(output)
    return output