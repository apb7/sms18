import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SMS_18.settings")
import django
django.setup()
from main.models import Stock
import time
import random

def algo():
	time_total = 60
	minutes = 0
	while(minutes<=time_total):
		minutes+=1
		time.sleep(60)#sleep for this many seconds
		all_stocks = Stock.objects.all()
		for this_stock in all_stocks:
			random_number = random.randint(-101,101)
			this_stock.stock_price = (this_stock.initial_price + (((this_stock.final_price - this_stock.initial_price)/time_total)*minutes))*(1-random_number/10000)
			this_stock.save()
