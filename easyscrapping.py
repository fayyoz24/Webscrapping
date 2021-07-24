import selenium
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from datetime import date, timedelta


options = Options()
options.handless = True
options.headless = True
options.add_argument("--disable-gpu")

url = "https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YPx13Y4zbIU"
driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get(url)
days = []
descriptions = []
dates = []

for i in range(1, 14, 2): #we should take only days
    #weekdays
    day = driver.find_element_by_xpath('//*[@id="detailed-forecast-body"]/div['+str(i)+']/div[1]/b')
    days.append(day.text)
    # a short descriptions
    description = driver.find_element_by_xpath('//*[@id="detailed-forecast-body"]/div['+str(i)+']/div[2]')
    descriptions.append(description.text)

for i in range(1, 8):
    current_day = date.today()
    current_day += timedelta(days=i)
    current_day = str(current_day)
    dates.append(current_day)

wether_weekly = pd.DataFrame(data={"Day_of_the_week":days,
                        "The_date":dates,
                        "Description_of_day":descriptions},
                        index=list(range(1, 8)))
wether_weekly.to_csv("weather.csv")



