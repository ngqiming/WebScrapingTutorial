import requests
from bs4 import BeautifulSoup
import pandas as pd
# crate a page object from the webpage
page = requests.get(
    "https://weather.com/weather/tenday/l/000f7cfcac72fc6924220b6f7ecfe615220cc7c2682aad7244e47d4206563a01")
# create a beautiful soup object
soup = BeautifulSoup(page.content, 'html.parser')

# Create a dayitem for finding days
dayItem = soup.find_all('span',{'class':'date-time'})
# Create a list to store all days
allDays = []
for item in dayItem:
    allDays.append(item.get_text())

# Create  a des item for finding all description
Items = soup.find_all('td',{'class':'description'})
desItem = []
for item in Items:
    desItem.append(item.find('span').get_text())

# Create a deg item for finding a degrees
temp = []
degItem = soup.find_all('td',{'class':'temp'})

for i in range(len(degItem)):
    val = degItem[i].find_all('span')
    temp.append(val[0].text)

# Create precip item for precip
precip = []
preItem = soup.find_all('td',{'class':'precip'})

for i in range(len(preItem)):
    val = preItem[i].find_all('span')
    precip.append(val[2].text)


# Create Wind item for find wind speed
speed = []
windItem = soup.find_all('td',{'class':'wind'})
for item in windItem:
    speed.append(item.find('span').get_text())


# Create humid item for humidity
humidity = []
huItem = soup.find_all('td',{'class':'humidity'})

for i in range(len(huItem)):
    val = huItem[i].find_all('span')
    humidity.append(val[1].text)

# Put all data obtained into a table
weatherToday = pd.DataFrame(
    {'Day': allDays,
     'Description': desItem,
     'Temperature': temp,
     'Precip': precip,
     'Wind': speed,
     'Humidity': humidity
     }
)
print(weatherToday)
# Convert to csv
weatherToday.to_csv('Weather_Today.csv')







