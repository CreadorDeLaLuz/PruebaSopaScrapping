import requests
import asyncio
from bs4 import BeautifulSoup
import aiohttp
import pandas as pd
import numpy
from openpyxl.workbook import Workbook

def Reporte(a,b,c,d,e):
    Direccion=a
    Etiqueta=b
    Propiedad=c
    Valor=d
    page = requests.get(Direccion)
    soup = BeautifulSoup(page.content,'html.parser')
    result=soup.find_all(Etiqueta,{Propiedad:Valor})
    results=list()
    for i in result:
        results.append(i.text)
    if(e==1):
        for i in results:
            print(i)
    if(e==2):
        return results

Reporte("https://www.netflix.com/ve/browse/genre/839338","span","class","nm-collections-title-name",1)
Campo1=Reporte("https://www.netflix.com/ve/browse/genre/839338","span","class","nm-collections-title-name",2)

page = requests.get("https://www.netflix.com/ve/browse/genre/839338")
soup = BeautifulSoup(page.content,'html.parser')
result=soup.find_all("a",{"class":"nm-collections-title nm-collections-link"})
results=list()
Direcciones=list()
Campo3=list()
Campo4=list()
Campo5=list()
Campo6=list()
Campo7=list()
Campo7aux=list()
for i in result:
    results.append(i)
for i in results:
    print(i.get("href"))
    Direcciones.append(i.get("href"))
j=0

for i in Direcciones:
    Reporte(i,"span","class","maturity-number",1)
    Campo3.append(Reporte(i,"span","class","maturity-number",2))
    j=j+1
    if(j>20):
        break
j=0
for i in Direcciones:
    Reporte(i,"span","class","title-info-metadata-item item-year",1)
    Campo4.append(Reporte(i,"span","class","title-info-metadata-item item-year",2))
    j=j+1
    if(j>20):
        break
j=0
for i in Direcciones:
    Reporte(i,"span","class","test_dur_str",1)
    Campo5.append(Reporte(i,"span","class","test_dur_str",2))
    j=j+1
    if(j>20):
        break
j=0
for i in Direcciones:
    Reporte(i,"a","class","title-info-metadata-item item-genre",1)
    Campo6.append(Reporte(i,"a","class","title-info-metadata-item item-genre",2))
    j=j+1
    if(j>20):
        break
j=0

for i in Direcciones:

    Campo7aux=(Reporte(i,"div","class","episode",2))
    episodios=0
    for k in Campo7aux:
        episodios=episodios+1
    Campo7.append(episodios)
    print(episodios)
    j=j+1
    if(j>20):
        break
j=0
df=pd.DataFrame()
df2=pd.DataFrame()
df3=pd.DataFrame()
df4=pd.DataFrame()
df5=pd.DataFrame()
df6=pd.DataFrame()
df7=pd.DataFrame()
df["Nombres"]=Campo1
df2["Direcciones"]=Direcciones
df3["RestriccionDeEdad"]=Campo3
df4["Anio"]=Campo4
df5["Duracion"]=Campo5
df6["Tipo"]=Campo6
df7["Episodios"]=Campo7
df.to_excel("ScrappingEnNetflix.xlsx")
df2.to_excel("ScrappingEnNetflix2.xlsx")
df3.to_excel("ScrappingEnNetflix3.xlsx")
df4.to_excel("ScrappingEnNetflix4.xlsx")
df5.to_excel("ScrappingEnNetflix5.xlsx")
df6.to_excel("ScrappingEnNetflix6.xlsx")
df7.to_excel("ScrappingEnNetflix7.xlsx")
