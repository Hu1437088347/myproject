import requests
from bs4 import  BeautifulSoup
url="http://www.cntour.cn/"

response=requests.get(url)
print(response.text)


soup=BeautifulSoup(response.text,'lxml')
data=soup.select("#header > div.shortCut > div > ul.shortCutL.clearfix > li:nth-child(1) > a")
print(data)

for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href')
    }
    print(result)