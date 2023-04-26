'''
Quickly find or access any article or information
'''

import requests
from bs4 import BeautifulSoup

req = requests.get('https://foysalcodeio.github.io/hot-gadgets/')

soup = BeautifulSoup(req.content, "html.parser")

#print(soup.prettify())
res = soup.title # whatever you want just .[anyname]
print(res.prettify())

for link in soup.find_all('a'):
    print(link.get('href'))




