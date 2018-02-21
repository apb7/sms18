from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) #extending user model
	name = models.CharField(max_length=100)	#username as per the db
	mail_id=models.CharField(max_length=100) #will get from app so no checks are required
	balance=models.IntegerField(default=100) #this will contain the current balance throughout 
	net_worth=models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Stock(models.Model):
	product_name = models.CharField(max_length=100) #from manforce to mrf, anything in between xD
	stock_price = models.IntegerField(default=0) #Stock price at any instant
	market_type = models.CharField(max_length=10, null=False, choices=(("BSE",'"BSE"'),("NYM",'"NYM"')),default="BSE")
	price_trend = models.IntegerField(default=0)
	initial_price = models.IntegerField(default = 0)
	#first two digits will be ones and tens representatives... others decimal

	def __str__(self):
		return self.product_name

class StockPurchased(models.Model):
	owner = models.ForeignKey('UserProfile' , on_delete=models.CASCADE) #stock purchased by which user
	stockid = models.ForeignKey('Stock' , on_delete=models.CASCADE) #which stock purchased by user
	number_of_stocks = models.IntegerField(default=0) #how many stocks were purchased
	# TODO: Average stock price: Call the Stock with stock_id, calculate the total and then avg. price.
	average_price = models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.number_of_stocks)


class GameSwitch(models.Model):
	switch_name=models.CharField(null=False,max_length=10) #We will have only one switch called 'Main'
	game_status= models.CharField(null=False, choices=(("live",'"live"'),("closed",'"closed"')),max_length=100,default="closed") 

	def __str__(self):
		return self.switch_name

class NewsPost(models.Model):
	post_text=models.CharField(null=False,max_length=4000)
	time_of_post=models.DateTimeField(default=datetime.now, blank=True)


		
class ConversionRate(models.Model):
	var_name = models.CharField(null=False,max_length=100,default="main")
	conversion_rate = models.IntegerField(default=0)

	def __str__(self):
		return self.var_name