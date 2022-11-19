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
            text = elem.text
            text_p = text.strip().split("\n")
            assert len(text_p) >= 6
            break
        except:
            sleep(1)
            i += 1
    if i == 10:
        raise Exception("Could not find flight details")
    # get the text
    
    
    output = {"Flight Number":flight_number}

    #assert output[0].lower() == "altitude"
    output["Altitude"] = text_p[1]

    #assert output[2].lower() == "latitude"
    output["Latitude"] = text_p[3]

    #assert output[4].lower() == "longitude"
    output["Longitude"] = text_p[5]
    
    print(output)
    return output

def get_bearing(lat1, lon1, lat2, lon2):
    # Given two points, return the bearing between them
    import math

    # Bearing = atan2(X, Y)

    # X = cos θb * sin ∆L

    # Y = cos θa * sin θb – sin θa * cos θb * cos ∆L

    x = math.cos(lat2) * math.sin(lon2 - lon1)
    y = (math.cos(lat1) * math.sin(lat2)) - (math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1))
    bearing = math.atan2(x, y)
    bearing_degrees  = math.degrees(bearing) - 180
    return bearing_degrees
