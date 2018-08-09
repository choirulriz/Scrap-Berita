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
listBerita=[] #list link berita
for link in indeks:
	# print (link.find('a').get('href'))
	# if 
	listBerita.append(link.find('a').get('href'))

# def bukaUrlWeb(urlWeb):
# 	buka = urlopen(urlWeb).read()
# 	sup = BeautifulSoup(buka,"lxml")
# 	konten = sup.find_all("article")
# 	for i in konten:
# 		print (i.find("h1").get_text())

	# print(sup.prettify()[1:100])

for url in listBerita:
	print (url)
	# bukaUrlWeb(url)
	# print(sup.prettify()[1:1000])
	
