#request ve beautifulSoup Modülü
import requests
from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=ankara"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

#print(soup.prettify())
#print(soup.find_all("p")) #p etiketinş buldu

"""for i in soup.find_all("p"):
#    print(i.get("style"))
    print(i.text)
#    print(i)
    print("****************************************************")

"""
print(soup.find_all("div",{"class":"yp-poi-box-2"})) #sözlük verdik class ı yp-boi olan classları almak istiyorum diyoruz
