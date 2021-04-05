import requests

from bs4 import BeautifulSoup

html = str(input())

r = requests.get(html)
if r.status_code != 200:
    print('Error')
soup = BeautifulSoup(r.content, 'html.parser')
p1 = soup.find('h1')
print(p1.text)
