import newspapergrabber
import newssources
import psycopg2
from dateutil import parser
# import types
# import importlib.util
#
# spec = importlib.util.spec_from_file_location('sentiment', '../usent/sentiment.py')
# mod = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(mod)
try:
    conn = psycopg2.connect("dbname=fulcrum user=james host=localhost password=james")
    cur = conn.cursor()
except psycopg2.Error:
    print(Error.args)

this_rss = newssources.get_news_sources()

feed_array = []
for feed in this_rss:
    feed_array.append(newspapergrabber.grab(feed))

for feed in feed_array:
    for article in feed:
        dt = parser.parse(article.publish_date)
        try:
            cur.execute("""INSERT INTO newsarticles (title,article,topimage,url,publish_date,compscore) VALUES (%(title)s, %(article)s, %(topimage)s, %(url)s, %(publish_date)s, %(compscore)s) ON CONFLICT (url) DO UPDATE SET title=%(title)s, article=%(article)s, topimage=%(topimage)s, publish_date=%(publish_date)s, compscore=%(compscore)s WHERE (newsarticles.article) != %(article)s;""", {'title': article.title, 'article': article.text, 'topimage': article.top_image, 'url': article.url, 'publish_date': dt, 'compscore': 0})

        except psycopg2.Error:
            print(Error.args)
        conn.commit()
print('finished gathering news sources!')
