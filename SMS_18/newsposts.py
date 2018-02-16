import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SMS_18.settings")
import django
django.setup()
from main.models import NewsPost,StoredNews
import time
import datetime
import random
import pause

#pause.until(datetime(2015, 8, 12, 2))
#this function is needed to be called when the event starts!
def news_timer():
	time_total = 1000000
	all_posts = StoredNews.objects.all()
	for this_post in all_posts:
		time.sleep(this_post.minutes_interval)
		new_newspost = NewsPost()
		new_newspost.corresponding_stock = this_post.corresponding_stock
		new_newspost.post_text = this_post.post_text
		new_newspost.time_of_post = datetime.now()
		new_newspost.save()

