import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

r = requests.get(url)

soup = BeautifulSoup(r.text)

text = soup.find_all("div", class_="grid--item body body__container article__body grid-layout__content")

for elements in text:
    print(elements.text)