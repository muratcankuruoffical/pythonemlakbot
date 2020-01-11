import requests
import json
from bs4 import BeautifulSoup
import time
import decimal
from babel.numbers import format_decimal

#for price in result:
	#print(price)


baslangic = 1
bitis = 123

liste = []
for i in range(baslangic, bitis):
	#time.sleep(5)
	url = "https://www.hurriyetemlak.com/besiktas-kiralik?page="+str(i)
	page = requests.get(url, timeout=(10,30))
	soup = BeautifulSoup(page.content, "html.parser")
	result = soup.find("script", type="application/ld+json")
	json_data = json.loads(result.text)
	print(json_data["mainEntity"]['offers']['itemOffered'])
	for item in json_data["mainEntity"]['offers']['itemOffered']:
		#u = item['offers']['price']
		#u = format_decimal(item['offers']['price'], locale='tr_TR')
		if item['offers']['price'] <= 5000:
			liste.append(str(item['offers']['price']))
		print(liste)
	if i == 122:
		dosya = open('hurriyetistanbulbesiktas.txt', 'w+')
		dosya.writelines(str(liste))
		dosya.close()