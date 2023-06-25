import requests
from bs4 import BeautifulSoup
import csv
import re


# headers={
#     "Accept": "application/font-woff2;q=1.0,application/font-woff;q=0.9,*/*;q=0.8",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
# }
# url="http://megainvest.com.ua/strojmaterialy/"

# req=requests.get(url, headers=headers)
# src= req.text
# # print(src)
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

class Webpars:
    def __init__(self, src, kateg):
        self.src= src
        self.kateg= kateg
   
    def kategoris(self, kateg):
        soup= BeautifulSoup(self.src ,"lxml")
        kateg=soup.find(class_="inav").find_all("a")
        print("\n Ссылки на категории \n")
        for kat in kateg:
            kateg_norm=kat.text
            kat_irl=kat.get("href")
            print(f"{kateg_norm}: {kat_irl}")

    def tovar(self):
        soup= BeautifulSoup(self.src ,"lxml")
        all_prod=soup.find_all(class_="product-thumb")
        print("\n Товары \n")
        for tov in all_prod:
            a= re.sub("^\s+|\n|\r|\t|\s+$", '', tov.text) 
            # tov_alt=tov.get("h4")
            # tov_a=tov.get("span")
            # tov_hr=tov.get("href")
            print(a)
    
    def downfile(self):
        with open("data.csv","w", encoding="cp1251", newline="") as file:
            writer=csv.writer(file)
            writer.writerow(("Категории", "Товар"))

        for dat in self.kateg:
            with open("data.csv", "a", encoding="cp1251") as file:
                writer=csv.writer(file)
                writer.writerows(dat)


with open("prs/index.html", encoding="utf-8") as file:
    src=file.read()

soup= BeautifulSoup(src ,"lxml")
kateg=soup.find(class_="inav").find_all("a")

pars=Webpars(src, kateg)
pars.kategoris(kateg)
pars.tovar()
pars.downfile()

# re.sub("^\s+|\n|\r|\s+$", '', )
# 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# class Onetimescraper:
#     results = []
    
#     def fetch(self, url):
#         print('HTTP GET request to URL: %s' % url, end='')
#         res = requests.get(url)
#         print(' | Status code: %s' % res.status_code)
        
#         return res
    
#     def to_html(self, html):
#         with open('res.html', 'w') as html_file:
#             html_file.write(html)
    
#     def from_html(self):
#         html = ''
        
#         with open('res.html', 'r') as html_file:
#             for line in html_file.read():
#                 html += line
        
#         return html
    
#     def to_csv(self):
#         with open('results.csv', 'w') as csv_file:
#             writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
#             writer.writeheader()
            
#             for row in self.results:
#                 writer.writerow(row)
        
#         print('"results.csv" has been written successfully!')

