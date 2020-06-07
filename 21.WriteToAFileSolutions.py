from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
myHeadlines = soup.find_all("div", class_="css-debyuq e1voiwgp1")


filename = input("File to save to: ")


for x in myHeadlines:
    with open(filename + ".txt", "a+") as file:
        file.write(x.text)
        file.write("\n")
