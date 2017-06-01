import newspaper
import feedparser

from newspaper import Article

class ThisArticle:
    zero = 0

    def __init__(self, url, title, text, publish_date, top_image):
        self.url = url
        self.title = title
        self.text = text
        self.publish_date = publish_date
        self.top_image = top_image


def grab(rssaddress):

    article_array = []

    this_rss = feedparser.parse(str(rssaddress))

    for post in this_rss.entries:
        try:

            url = post.link
            publish_date = post.published
            title = post.title

            article = Article(url)
            article.download()
            article.parse()

            text = article.text
            top_image = article.top_image


            article_array.append(ThisArticle(url, title, text, publish_date, top_image))
        except:
            pass

    return article_array
