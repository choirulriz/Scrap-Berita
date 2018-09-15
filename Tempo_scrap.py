from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import pandas as pd

# Bagian memanggil top level url nya, tempat mengekstrak banyak url lain yang berkaitan dengan berita pilpress
try:
	html = urlopen("https://pilpres.tempo.co/").read()
	soup = BeautifulSoup(html,"lxml")
except HTTPError as he:
	print(he)
	exit()

# Bagian mencari semua url dalam web yang spesifik pada pilpress.tempo.co...
indeksPilpres = soup.find_all('a', href = re.compile('https://pilpres\.tempo\.co/')) #Find All menghasilkan list

urlPilpres = []	#list Kosong menampung url yang dikomposisi dari find all

# Bagian dekomposisi url
for a in indeksPilpres:
	urlPilpres.append(a['href'])

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

#Bagian membuka tiap tiap url
for b in urlPilpres:
	buka = BeautifulSoup(urlopen(b).read(),'lxml')
	judul = buka.find({'title': True}).get_text() #menemukan letak judul pada tag <\title>
	konten = buka.find(id='isi').find_all('p') #menemukan letak konten pada tag id=isi dan menampung semua tag <p>

	nama_judul.append(judul)	#Ambil bagian Judul URL
	konten_teks = ', ' #Untuk Menampung semua tag <p>
	for p in konten:
		konten_teks +=''.join(p.find_all(text = True))

	isi.append(konten_teks)

# Bagian memasang judul dan artikel kedalam data frame
data_tuples = list(zip(nama_judul,isi))
df = pd.DataFrame(data_tuples,columns = ['Judul','Konten'])

# bagian menyimpan kedalam csv
df.to_csv("Tempoe4.csv",sep = ',', encoding='utf-8') #separator menggunakan tab karena dalam paragraf banyak koma

