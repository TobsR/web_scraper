import requests


class Scraper:
    def __init__(self):
        self.url = str(input('Input the URL:'))
        self.r = None

    def get(self):
        self.r = requests.get(url=self.url)
        if self.r.status_code != 200:
            print('Invalid quote resource!')
        else:
            try:
                print(self.r.json()["content"])
            except KeyError:
                print('Invalid quote resource!')


my_request = Scraper()
my_request.get()
