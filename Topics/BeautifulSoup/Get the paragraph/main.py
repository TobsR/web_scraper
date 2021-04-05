import requests

from bs4 import BeautifulSoup

word = str(input())
html = str(input())

r = requests.get(html)
if r.status_code != 200:
    print('Error')
soup = BeautifulSoup(r.content, 'html.parser')
p1 = soup.find_all('p')
for i in p1:
    if word in i.text:
        print(i.text)
        break
