from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts=[]
article_links = []

for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)
largest_number = max(article_upvotes)
largest_num_index = article_upvotes.index(largest_number)

print(article_texts[largest_num_index])
print(article_links[largest_num_index])
