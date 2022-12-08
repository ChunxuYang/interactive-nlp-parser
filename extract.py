from newspaper import Article

from models.rss import RSS


def extract(url: str) -> RSS:
    article = Article(url)
    article.download()
    article.parse()
    return RSS(url, article.title, article.text)
