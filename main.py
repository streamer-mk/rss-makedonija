from rss_generator.scraper import fetch_articles
from rss_generator.rss_builder import build_rss
from wordpress_publisher.publisher import publish_to_wordpress

if __name__ == "__main__":
    articles = fetch_articles()
    rss_feed = build_rss(articles)
    if articles:
        publish_to_wordpress(articles[0])