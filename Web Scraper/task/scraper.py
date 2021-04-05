# import json
import os
import requests
from bs4 import BeautifulSoup
import string

article_types = {'Article': 'c-article-body', 'Book Review': 'article__body cleared',
                 'Books & Arts': 'article__body cleared', 'Books Received': '',
                 'Correspondence': 'article__body cleared', 'Editorial': 'article__body cleared',
                 'Erratum': '', 'Letter': 'c-article-body', 'Matters Arising': '',
                 'Miscellany': '', 'News': 'article__body cleared', 'News & Views': 'article__body cleared',
                 'News Feature': 'article__body cleared', 'News in Brief': 'entry-content',
                 'Obituary': 'article__body cleared', 'Opinion': 'c-article-body',
                 'Research Highlight': 'article-item__body', 'Review Article': 'c-article-body',
                 'Scientific Correspondence': 'c-article-section', 'Supplement to Nature': ''}


class WebScrapper:
    def __init__(self, url):
        self.url = url + '/nature/articles'
        self.request = requests.get(self.url)
        self.list_articles = []
        self.pages_akt = 0
        self.pages_n = int(input('Enter number of pages to search: '))
        self.article_types = input('Enter the article type: ')
        if self.article_types not in article_types:
            exit()

    def __str__(self):
        return f"Saved articles: {self.list_articles}"

    def get_info(self):

        global article_types

        head_link = "https://www.nature.com"

        while self.pages_akt < self.pages_n:
            self.pages_akt += 1
            if not os.path.isdir(f'Page_{self.pages_akt}'):
                os.mkdir(f'Page_{self.pages_akt}')

            if self.pages_akt > 1:
                pages_next = soup.find("li", {"data-page": "next"})
                self.url = head_link + pages_next.find("a", class_="c-pagination__link").get("href")
                self.request = requests.get(self.url)

            if self.request:
                soup = BeautifulSoup(self.request.content, "html.parser")
                articles = soup.find_all("article")  # self.article_types

                for article in articles:
                    article_type = article.find("span", class_="c-meta__type").text

                    if article_type == self.article_types:
                        tail_link = article.find("a", {"data-track-action": "view article"}).get("href")

                        hyperlink = requests.get(head_link + tail_link)
                        hyperlink_soup = BeautifulSoup(hyperlink.content, "html.parser")
                        hyperlink_body = hyperlink_soup.find("div", class_=article_types[self.article_types]).text.strip()

                        translator = str.maketrans('', '', string.punctuation)
                        # test = hyperlink_soup.find("title").text
                        # test2 = hyperlink_soup.find("meta", {"property": "og:title"})['content']
                        title = hyperlink_soup.find("meta", {"property": "og:title"})['content'].translate(translator).replace(" ", "_")

                        self.save_to_file(title, hyperlink_body)

            else:
                return f"The URL returned {self.request.status_code}"
        return "Saved all articles."

    def save_to_file(self, filename, hyperlink_body):
        try:
            with open(f'Page_{self.pages_akt}/{filename}.txt', 'w', encoding="UTF-8") as file:
                print(hyperlink_body, file=file)

            self.list_articles.append(f"{filename}.txt")
        except Exception as e:
            return e


if __name__ == '__main__':
    r = WebScrapper("https://www.nature.com")
    print(r.get_info())
    print(r)
