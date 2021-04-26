# Problem statement : Open all links on a page in separate browser tabs.

import requests
from bs4 import BeautifulSoup
import webbrowser as wb

response = requests.get('https://www.geeksforgeeks.org/')
soup = BeautifulSoup(response.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
	urls.append(link.get('href'))

for i in urls:
	wb.open(i)
