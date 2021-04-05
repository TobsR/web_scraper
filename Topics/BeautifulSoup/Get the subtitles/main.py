import requests

from bs4 import BeautifulSoup

index = int(input())
html = str(input())

r = requests.get(html)
if r.status_code != 200:
    print('Error')
soup = BeautifulSoup(r.content, 'html.parser')
p1 = soup.find_all('h2')
print(p1[index].text)
