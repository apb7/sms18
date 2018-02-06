from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) #extending user model
	name = models.CharField(max_length=100)	#username as per the db
	mail_id=models.CharField(max_length=100) #will get from app so no checks are required
	balance=models.IntegerField(default=0) #this will contain the current balance throughout 
	net_worth=models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Stock(models.Model):
	product_name = models.CharField(max_length=100) #from manforce to mrf, anything in between xD
	stock_price = models.IntegerField(default=0) #Stock price at any instant
	initial_price = models.IntegerField(default=0)
	final_price = models.IntegerField(default=0)

	def __str__(self):
		return self.product_name

class StockPurchased(models.Model):
	owner = models.ForeignKey('UserProfile' , on_delete=models.CASCADE) #stock purchased by which user
	stockid = models.ForeignKey('Stock' , on_delete=models.CASCADE) #which stock purchased by user
	number_of_stocks = models.IntegerField(default=0) #how many stocks were purchased

	def __str__(self):
		return self.number_of_stocks


class GameSwitch(models.Model):
	switch_name=models.CharField(null=False,max_length=10) #We will have only one switch called 'Main'
	game_status= models.IntegerField(null=False, choices=((0,'0'),(1,'1'),(2,'2')),default = 0) #0 for before start, 1 fr during game,2 for after game ends

	def __str__(self):
		return self.switch_name

class StockPriceVariation(models.Model):
	stock_id = models.ForeignKey('Stock' , on_delete=models.CASCADE)
	date_and_time = models.DateTimeField(default=datetime.now, blank=True)
	price_at_time = models.IntegerField(null=False,default = 0)
	sequence_id = models.IntegerField(null=False, choices=((1,'1'),(2,'2'),(3,'3')),default = 1)
	#this will store what sequence of price is it for a particular stock

	def __str__(self):
		return self.date_and_time