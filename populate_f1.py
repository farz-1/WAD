import os
import news_api
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1.settings')

news_api.get_news()  # ensures database is populated before running timed calls
news_api.run()
