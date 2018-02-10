from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, Http404 ,HttpResponseForbidden, HttpResponseRedirect
from .models import UserProfile, GameSwitch, Stock, StockPurchased
from django.shortcuts import redirect, render_to_response
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import auth
from django.db import IntegrityError
from django.contrib.auth.models import User
import json
from .forms import TransactionForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from algoscript import algo

key = "9bBo3YmHufzvSYWjbtkURd" 

def index(request):#just a render view
    if not request.user.is_authenticated():
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    return redirect('auth:form')

def test(request):
	algo()
	return HttpResponse("Cool")

def game(request):#just a render view
    if not request.user.is_authenticated():
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    return render(request, 'main/gamepage.html')

def leaderboard(request):#just a render view
    if not request.user.is_authenticated():
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    return render(request, 'main/leaderboard.html')

def buy(request, id):#just a render view
    if not request.user.is_authenticated():
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    return render(request, 'main/buy.html', {'id':id})

def sell(request, id):#just a render view
    if not request.user.is_authenticated():
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    return render(request, 'main/sell.html', {'id':id})

def profile(request):#just a render view
    if not request.user.is_authenticated():
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    return render(request, 'main/profile.html')

def international(request):#just a render view
    if not request.user.is_authenticated():
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    return render(request, 'main/international.html')



# Register and login functions not working!

def register(request):
    if request.method == 'POST':
        data = request.POST
        try:
            obj = User.objects.get(username=data['username'])
            return redirect('main:index')
        except User.DoesNotExist:
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            user.save()
            userProf = UserProfile.objects.create(user=user, name=data['username'], mail_id=data['email'])
            userProf.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            django_login(request,user)
            return redirect('main:game')
    return redirect('main:index')

def login(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(username=data['username'], password=data['password'])
        django_login(request, user)
        if user is None:
            return redirect('main:index')
        else:
            return redirect('main:game')
    return redirect('main:index')

def logout(request):
    django_logout(request)
    return redirect('main:index')

# TODO: Usage??
def createProfile(request):
    try:
        userProf = UserProfile.objects.get(user=request.user)
    except:
        userProf = UserProfile.objects.create(user=request.user, name=request.user.username, mail_id=request.user.email)
    return redirect('main:game')


### (apb7, priyankjairaj100): Do not change these view functions.
# TODO: Setup a POST method with a key and email_id for user verification.

# TODO(priyankjairaj100): Implement a check on balance (>=0)
@csrf_exempt
def BuyStocks(request, id):
    global key
    user_key = request.POST.get('key')
    if user_key != key:
        resp = {
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")
    email = request.POST.get('email')
    current_user = UserProfile.objects.get(mail_id=email)
    # TODO(apb7): Remove the POST check here and put it at the top.
    if request.method == 'POST':
        data = request.POST
        stock_info = Stock.objects.get(id=id)
        transaction_cost = int(data['units'])*stock_info.stock_price
        if( current_user.balance < transaction_cost ):
            resp={
                'error':'Not sufficient balance to proceed the transaction'
            }
            return HttpResponse(json.dumps(resp), content_type="application/json")
        current_user.balance -= transaction_cost
        current_user.save()

        try:
            current_stock = StockPurchased.objects.get(owner_id=current_user.id, stockid=stock_info)
        except:
            current_stock = StockPurchased.objects.create(owner_id=current_user.id, stockid=stock_info)

        current_stock.number_of_stocks += int(data['units'])
        current_stock.save()
        resp = {
            'message': 'SUCCESS: The user purchased the stock.'
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")
        #return redirect('main:game')


@csrf_exempt
def SellStocks(request, id):
    global key
    user_key = request.POST.get('key')
    if user_key != key:
        resp = {
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")
    email = request.POST.get('email')
    current_user = UserProfile.objects.get(mail_id=email)
    stock_info = Stock.objects.get(id=id)
    try:
        current_stock = StockPurchased.objects.get(owner=current_user.id, stockid=stock_info)
    except StockPurchased.DoesNotExist:
        current_stock = None

    if request.method == 'POST' and current_stock is not None:
        data = request.POST
        stock_info = Stock.objects.get(id=id)
        if current_stock.number_of_stocks >= int(data['units']):
            current_user.balance += int(data['units'])*stock_info.stock_price
            current_user.save()
            #current_stock = StockPurchased.objects.get(owner=current_user.id, stockid=stock_info)
            current_stock.number_of_stocks -= int(data['units'])
            if current_stock.number_of_stocks is 0:
                current_stock.delete()
            else:
                current_stock.save()
            resp = {
                'message': 'SUCCESS: The user sold the stock.'
            }
            return HttpResponse(json.dumps(resp), content_type="application/json")
        else:
            resp = {
                'message': 'FAILURE: The user does not have enough stocks to sell.'
            }
            return HttpResponse(json.dumps(resp), content_type="application/json")
        #return redirect('main:game')
    elif request.method == 'POST' and current_stock is None:
        resp = {
            'error': 'The user does not have any stocks to sell'
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")


# This view will provide details of the user. No template rendered.
@csrf_exempt
def UserPrimaryDetails(request):
    global key
    user_key = request.POST.get('key')
    if user_key != key:
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    email = request.POST.get('email')
    current_user = UserProfile.objects.get(mail_id = email)
    resp={
        'username': current_user.name ,
        'email-id': current_user.mail_id ,
        'user_balance': current_user.balance ,
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def UserStockDetails(request):
    global key
    user_key = request.POST.get('key')
    if user_key != key:
        resp = {
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")
    email = request.POST.get('email')
    current_user = UserProfile.objects.get(mail_id=email)
    UserStocks = StockPurchased.objects.filter(owner=current_user)
    StocksData = []
    for this_stock in UserStocks:
        current_stock = Stock.objects.get(id=this_stock.stockid.id)
        stock_data = {
        "name" : current_stock.product_name,
        "num" : this_stock.number_of_stocks,
        "price" : current_stock.stock_price,
        "market_type":current_stock.market_type
        }
        #this will send the name of the stock along with the number of units the user is currently owning
        StocksData.append(stock_data)
    return HttpResponse(json.dumps(StocksData), content_type="application/json")

@csrf_exempt
def StocksPrimaryData(request):
    global key
    user_key = request.POST.get('key')
    if user_key != key:
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type="application/json")
    All_stocks = Stock.objects.all()
    StocksData = []

    for this_stock in All_stocks:
        stock_data = {
            "id" : this_stock.id,
            "name" : this_stock.product_name,
            "price" : this_stock.stock_price,
        }
        StocksData.append(stock_data)
    return HttpResponse(json.dumps(StocksData), content_type="application/json")


@csrf_exempt
def StockData(request, id):
    global key
    user_key = request.POST.get('key')
    if user_key != key:
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")

    this_stock = Stock.objects.get(id = id)
    num = 0
    try:
        current_stock = StockPurchased.objects.get(owner=UserProfile.objects.get(mail_id = request.POST.get('email'), stockid=this_stock))
        num = current_stock.number_of_stocks
    except:
        pass
    stock_data = {
        "name" : this_stock.product_name,
        "price" : this_stock.stock_price,
        "num" : num
    }
    return HttpResponse(json.dumps(stock_data), content_type = "application/json")


@csrf_exempt
def LBdata(request):
    global key
    user_key = request.POST.get('key')
    if user_key != key:
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    email = request.POST.get('email')
    current_user = UserProfile.objects.get(mail_id = email)
    for this_user in UserProfile.objects.all():
        this_user.net_worth=0
        for this_stock in StockPurchased.objects.filter(owner=this_user):
            this_user.net_worth+=this_stock.number_of_stocks * (this_stock.stockid).stock_price
        this_user.net_worth+=this_user.balance
        this_user.save()
    up = UserProfile.objects.order_by('-net_worth')
    d=[]
    for i in up:
        if i.net_worth>0:
            d.append({
                'name':i.name,
                'net_worth':i.net_worth
                })
            my_pos = d.index({'name':current_user.name,'net_worth':current_user.net_worth}) + 1
    x=20
    n=len(d)
    d = d[:abs(x-n)]
    d.append({'Rank of current_user':my_pos})
    return HttpResponse(json.dumps(d), content_type = "application/json")


# This function will be used to login the user via the app. No template rendered.
@csrf_exempt
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')        
        #password = request.POST.get('password')
        #print (username)
        try:
            obj = User.objects.get(username=username)
            msg = {
                'message': 'The user is already registered.'
            }
            return HttpResponse(json.dumps(msg), content_type="application/json")
        except User.DoesNotExist:
            # This line fills up random password for the user in the backend.
            password = User.objects.make_random_password()
            user = User.objects.create_user(username, email, password)
            user.save()
            userProf = UserProfile.objects.create(user=user, name=username, mail_id=email)
            userProf.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            django_login(request,user)
            msg = {
                'message': 'SUCCESS: The user has been registered.'
            }
            return HttpResponse(json.dumps(msg), content_type="application/json")
    else:
        msg = {
                'message': 'FAILURE: Please make a POST request.'
            }
        return HttpResponse(json.dumps(msg), content_type="application/json")


@csrf_exempt
def userLogout(request):
    pass