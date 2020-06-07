from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
myHeadlines = soup.find_all("div", class_="css-debyuq e1voiwgp1")


for x in myHeadlines:
    print(x.text)


