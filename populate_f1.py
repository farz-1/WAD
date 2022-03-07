import os
import news_api
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1.settings')

news_api.run()