from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import pandas as pd
# import requests

# Bagian memanggil top level url nya, tempat mengekstrak banyak url lain yang berkaitan dengan berita pilpress
try:
	html = urlopen("https://www.liputan6.com/pilpres").read()
	soup = BeautifulSoup(html,"lxml")
except HTTPError as he:
	print(he)
	exit()

# Bagian mencari semua url dalam top populer yang spesifik pada pilpres. 
# indeksPilpres = soup.find(class_="aside-list popular").find_all('a', href = re.compile('https://www\.liputan6\.com/pilpres')) #Find All menghasilkan list
indeksPilpres = soup.find(class_="aside-list popular").find_all('a', href = re.compile('https://www\.liputan6\.com/pilpres'))

urlPilpres = []	#list Kosong menampung url yang dikomposisi dari find all

# # Bagian dekomposisi url

for a in indeksPilpres:
	urlPilpres.append(a['href'])
# 	# print(a)
	
# print(urlPilpres)

# Karena dalam satu web terdapat url yang sama maka kita hapus url yang berduplikat
def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

urlPilpres = remove(urlPilpres)

#list-list kosong
nama_judul  = [] 
isi = []
# print(urlPilpres)

#Bagian membuka tiap tiap url
# # #Bagian membuka tiap tiap url
for b in urlPilpres:
	urls = urlopen(b).read()	
	buka = BeautifulSoup(urls,'lxml')
	
	judul = buka.find({'title': True}).get_text() #menemukan letak judul pada tag <\title>
	konten = buka.find(class_='article-content-body__item-content').find_all('p') #menemukan letak konten pada tag id=isi dan menampung semua tag <p>

	nama_judul.append(judul)	#Ambil bagian Judul URL
	konten_teks = ',' #Untuk Menampung semua tag <p>
	for p in konten:
		konten_teks +=''.join(p.find_all(text = True))

	isi.append(konten_teks)

# # Bagian memasang judul dan artikel kedalam data frame
data_tuples = list(zip(nama_judul,isi))
df = pd.DataFrame(data_tuples,columns = ['Judul','Konten'])

# bagian menyimpan kedalam csv
df.to_csv("liputan6.csv",sep = ',', encoding='utf-8') #separator menggunakan tab karena dalam paragraf banyak koma

