import requests
import json
from bs4 import BeautifulSoup
baslangic = 1
bitis = 16
liste = []
for i in range(baslangic, bitis):
    headers = {"Content-Type": "text/html"}
    r = requests.get("https://www.zingat.com/besiktas-kiralik-daire?page="+str(i)+"&page_size=21&locationId=156&fromPage=true", headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    result = soup.find_all("div", {"class": "property-size"})
    result_price = soup.find_all("div", {"class": "price"})
    for div in result_price:
        if float(div.text.replace(" TL", "")) <= 5.000:
            liste.append(div.text.replace(" TL", ""))
            print(liste)
        #liste.append(div.text.replace(" m²", ""))

    if i == 15:
        dosya = open('zingatistanbulbesiktas.txt', 'w+')
        dosya.writelines(str(liste))
        dosya.close()

#for div2 in result_price:
   # print(div2.text.replace(" TL", ""))
