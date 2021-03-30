import requests

from bs4 import BeautifulSoup


pos = int(input())
ref = str(input())
r = requests.get(ref)
if r.status_code != 200:
    print('Error.')
soup = BeautifulSoup(r.content, 'html.parser')
p1 = soup.find_all('a')
print(p1[pos - 1].get('href'))
