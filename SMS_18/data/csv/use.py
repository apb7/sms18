import json
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SMS_18.settings")
import django
django.setup()
from main.models import Stock
import time
import random

with open('day1.json') as jsonfile:
    dictionary=json.load(jsonfile)
    print(dictionary)
    
j = 0    
for i in range(len(dictionary[list(dictionary.keys())[0]])):    
    for key in dictionary:
        print(key)
        stock = Stock.objects.get(product_name__iexact=key)
        stock.stock_price = dictionary[key][j]
        stock.save()
    j += 1
    time.sleep(5)
       
