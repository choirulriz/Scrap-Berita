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


indeksPilpres = soup.find_all('a', href = re.compile('https://pilpres\.tempo\.co/'))

urlPilpres = []

for a in indeksPilpres:
	urlPilpres.append(a['href'])
	# print (a['href'])

def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

urlPilpres = remove(urlPilpres)
# print(urlPilpres)


for b in urlPilpres:
	buka = BeautifulSoup(urlopen(b).read(),'lxml')
	konten = buka.find_all(['title','p'])
	for p in konten:
		print(p.get_text())
	

