import os
import requests
import django
import schedule

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1.settings')
django.setup()

from f1.models import News


def get_news():
    # bad practice having plain API keys in production, however obfuscation is beyond the scope of this project.
    response = requests.get("https://newsapi.org/v2/everything?q=F1&pageSize=100",
                            headers={"X-Api-Key": "adc95a32c802452a845c7dd6e2813993"})
    data = response.json()
    News.objects.all().delete()

    for i in data.get("articles"):
        article = News(title=i['title'],
                       summary=i['description'],
                       imageURL=i['urlToImage'],
                       articleURL=i['url'],
                       published=i['publishedAt'],
                       author=i['author'])
        article.save()
    print("News table updated!")


def run():
    schedule.every(1).hour.do(get_news)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    run()

