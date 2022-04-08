import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/91714422#tab=reviews"
response = requests.get(url)
# print(response.status_code) #

page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select("div.js_product-review")
opinion = opinions.pop(0)
opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").get_text().strip()
print(author)

recommendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
print(recommendation)

stars = opinion.select_one("span.user-post__score-count").get_text()
print(stars)

content = opinion.select_one("div.user-post__text").get_text()
print(content)

pros = opinion.select_one("div.review-feature__item").get_text()
print(pros)

useful = opinion.select_one("button.vote-yes > span").get_text().strip()
useless = opinion.select_one("button.vote-no > span").get_text().strip()
print(useful)
print(useless)

publish_date = opinion.select_one("span.user-post__publlished > time:nth-child(1)")["datetime"]
print(publish_date)