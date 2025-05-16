import feedparser

def build_rss(articles):
    # Dummy RSS builder
    return f"<rss><channel>{''.join(f'<item><title>{a['title']}</title><link>{a['link']}</link></item>' for a in articles)}</channel></rss>"