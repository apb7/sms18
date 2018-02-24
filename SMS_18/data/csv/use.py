import json
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SMS_18.settings")
import django
django.setup()
from main.models import UserProfile, Stock
import time
import random

#with open('Day3.json') as jsonfile:
#    dictionary=json.load(jsonfile)
    #print(dictionary)

#j = 0
up = UserProfile.objects.all()
for x in up:
    p = (x.name, x.mail_id)
    print (p)
#    print ('/n')
#    for key in dictionary:
#        stock = Stock.objects.get(product_name__iexact=key)
#        stock.initial_price = dictionary[key][0]
#        stock.stock_price = dictionary[key][j]
#        change_price = stock.stock_price
#        print(key, change_price)
#        stock.save()
#        stock.price_trend = stock.stock_price - stock.initial_price
#        stock.save()
#    j += 1
#    time.sleep(60)

