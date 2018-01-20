from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, Http404 ,HttpResponseForbidden
from .models import UserProfile, GameSwitch, Stock, StockPurchased
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib import auth
from django.db import IntegrityError
from django.contrib.auth.models import User
import json
from django.core import serializers



def index(request):
	return HttpResponse("Ayeh!")

def BuyStocks(request):
	current_user = UserProfile.objects.get(user = request.user)
	transaction_form = BuyStockForm(request.POST)
	if request.method == 'POST':
		if transaction_form.is_valid():
			data = transaction_form.cleaned_data
			#data will have two fields: the stock-name of purchase and the number of units
			current_stock = StockPurchased.objects.filter(owner=current_user).filter(stockid=data['stockname'])
			stock_info = Stock.objects.get(product_name=data['stockname'])
			current_user.balance-= (data['units']*stock_info.stock_price)
			current_stock.number_of_stocks+= data['units']
			current_stock.save()
			current_user.save()			
	#I havent renderred any template. This view is only for pinging and sending data

def SellStocks(request):
	current_user = UserProfile.objects.get(user = request.user)
	transaction_form = BuyStockForm(request.POST)
	if request.method == 'POST':
		if transaction_form.is_valid():
			data = transaction_form.cleaned_data
			#data will have two fields: the stock-name of sale and the number of units
			current_stock = StockPurchased.objects.filter(owner=current_user).filter(stockid=data['stockname'])
			stock_info = Stock.objects.get(product_name=data['stockname'])
			current_user.balance+= (data['units']*stock_info.stock_price)
			current_stock.number_of_stocks-= data['units']
			current_stock.save()
			current_user.save()			
	#I havent renderred any template. This view is only for pinging and sending data


def UserPrimaryDetails(request): #this view will give you all info of the user! Check out the fields.
	current_user = UserProfile.objects.get(user = request.user)
	resp={
		'username': current_user.name ,
		'email-id': current_user.mail_id ,
		'user_balance': current_user.balance ,
	}
	return HttpResponse(json.dumps(resp), content_type = "application/json")
	#I havent renderred any template. This view is only for pinging and sending data

def UserStockDetails(request):
	current_user = UserProfile.objects.get(user = request.user)
	UserStocks = StockPurchased.objects.filter(owner=current_user)
	StocksData = []
	for this_stock in UserStocks:
		stock_data = { this_stock.name : this_stock.number_of_stocks }
		#this will send the name of the stock along with the number of units the user is currently owning
		StocksData.append(stock_data)

	return HttpResponse(json.dumps(StocksData), content_type = "application/json")

def StocksPrimaryData(request):
	All_stocks = Stock.objects.all()
	StocksData = []

	for this_stock in All_stocks:
		stock_data = { this_stock.product_name : this_stock.stock_price }
		StocksData.append(stock_data)

	return HttpResponse(json.dumps(StocksData), content_type = "application/json")










