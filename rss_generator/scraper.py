import requests
from bs4 import BeautifulSoup

def fetch_articles():
    url = "https://www.vesti.mk/category/makedonija"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    items = soup.select(".news-item a")
    
    articles = []
    for item in items[:1]:  # only the first article
        title = item.get_text(strip=True)
        link = item.get("href")
        articles.append({"title": title, "link": link})
    return articles