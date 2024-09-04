import requests
import json
from bs4 import BeautifulSoup
from openpyxl import Workbook

url_get = requests.get('https://vogu35.ru/sveden/education')


soup_objects = BeautifulSoup(url_get.text, 'html.parser')

pars_table = soup_objects.find_all('table', class_='table-responsive')

pars_table1 = pars_table[6]

eduName = pars_table1.find_all('td', itemprop='eduName')
eduCode = pars_table1.find_all('td', itemprop='eduCode')

print(pars_table1)

# encoding = a.encoding if 'charset' in a.headers.get('content-type', '').lower() else None
# soup_objekts = BeautifulSoup(a.content.decode("utf-16"), 'html.parser', from_encoding=encoding)

# pars_table = soup_objekts.find_all('table', class_='table-responsive')

# Openpyxl
wb = Workbook()
ws = wb.active

for code, name in zip(eduCode, eduName):
    ws.append([code.text, name.text])
    

wb.save("bimbimbambam.xlsx")

# xlsx to Json
