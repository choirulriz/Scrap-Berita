from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

try:
	html = urlopen("https://pilpres.tempo.co/").read()
	soup = BeautifulSoup(html,"lxml")
except HTTPError as he:
	print(he)
	exit()
# print(soup.prettify()[1:1000])

indeks = soup.find_all("figure","swiper-slide")
# link = 1
# links=[]
for link in indeks:
	print (link.find('a').get('href'))
	# links.append(link.find('a').get('href'))

# print(links)
