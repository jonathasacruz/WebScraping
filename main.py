import pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

#for i in items:
#  print(i.find(class_='period-name').get_text())
#  print(i.find(class_='short-desc').get_text())
#  print(i.find(class_='temp').get_text())
#  print ("\n")

period_names = [item.find(class_='period-name').get_text() for item in items]
short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

print(period_names)
print(short_descriptions)
print(temperatures)

wheather_stuff = pd.DataFrame(
  {
    'period': period_names,
    'short_descriptions': short_descriptions,
    'temperatures': temperatures
    })

print(wheather_stuff)

wheather_stuff.to_csv('weather.csv')