import requests
import json
from bs4 import BeautifulSoup


baslangic = 1
bitis = 2
liste = []
for i in range(baslangic, bitis):
    r = requests.get("https://www.emlakjet.com/kiralik-daire/istanbul-besiktas/sahibinden/"+str(i))
    soup = BeautifulSoup(r.content, "html.parser")
    result_price = soup.find_all("div", {"class": "_3NCDx"})
    for div in result_price:
        if div.text.replace(" TL", "") <= '5.000':
            liste.append(div.text.replace(" TL", ""))
        #print(liste)
    if i == 1:
        dosya = open('emlakjetistanbulbesiktas.txt', 'w+')
        dosya.writelines(str(liste))
        dosya.close()