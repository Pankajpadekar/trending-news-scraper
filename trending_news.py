from bs4 import BeautifulSoup
from os import link
import requests


url = "https://timesofindia.indiatimes.com/topic/trending"
page = requests.get(url)
htmlContent = page.content
# print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')

latest = soup.find('div', {'class': 'crmK8'})
# print(latest)


counter = 0
title = soup.find_all('div', {'class': 'uwU81'})
if (counter < 10):
    for item in title:
        x = item.find('span')
        counter = counter + 1
        print(str(counter) + ":-" + x.text.strip())

counter = 0
for link in latest.find_all('a'):
    if (counter < 10):
        linkText = " :-  " + \
            (link.get('href')) + link.text
        counter = counter + 1

        print((str(counter) + linkText))

