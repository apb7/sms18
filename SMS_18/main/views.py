from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, Http404 ,HttpResponseForbidden, HttpResponseRedirect
from .models import UserProfile, GameSwitch, Stock, StockPurchased, NewsPost, ConversionRate
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
    if request.user.is_authenticated():
        return redirect('main:game')
    else:
        return redirect('auth:form')
        # resp={
        #     'error':'The user is not registered yet.'
        # }
        # return HttpResponse(json.dumps(resp), content_type = "application/json")

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

def news(request):#just a render view
    if not request.user.is_authenticated():
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    return render(request, 'main/news.html')    



# Register and login functions not working!

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = request.POST
        try:
            obj = User.objects.get(username=data.get('username'))
            return HttpResponse(json.dumps({"status":"fail", "url":reverse('main:index')}), content_type="application/json")
        except User.DoesNotExist:
            user = User.objects.create_user(data.get('username'), data.get('email'), data.get('password'))
            user.save()
            userProf = UserProfile.objects.create(user=user, name=data.get('username'), mail_id=data.get('email'))
            userProf.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            django_login(request,user)
            return HttpResponse(json.dumps({"status":"success", "email":user.email, "url":reverse('main:game')}), content_type="application/json")
    return redirect('main:index')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = request.POST
        print(data.get('username'))
        print(data.get('password'))
        print(data)
        user = authenticate(username=data.get('username'), password=data.get('password'))
        django_login(request, user)
        if user is None:
            return HttpResponse(json.dumps({"status":"fail", "url":reverse('main:index')}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"status":"success", "email":user.email, "url":reverse('main:game')}), content_type="application/json")
    return redirect('main:index')

def logout(request):
    django_logout(request)
    return redirect('main:index')
    del request.session['email']

# TODO: Usage??
def createProfile(request):
    try:
        userProf = UserProfile.objects.get(user=request.user)
    except:
        userProf = UserProfile.objects.create(user=request.user, name=request.user.get_full_name(), mail_id=request.user.email)
    return render(request, 'main/profileCreate.html', {'email': request.user.email, 'url':reverse('main:game')})


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

        new_number = current_stock.number_of_stocks+int(data['units'])
        current_stock.average_price = (current_stock.average_price*current_stock.number_of_stocks+ transaction_cost)/new_number 
        current_stock.number_of_stocks = new_number
        current_stock.save()
        print(current_stock)
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
            transaction_cost = int(data['units'])*stock_info.stock_price
            current_user.balance += transaction_cost
            current_user.save()
            #current_stock = StockPurchased.objects.get(owner=current_user.id, stockid=stock_info)
            new_number = current_stock.number_of_stocks - int(data['units'])
            if new_number is 0:
                current_stock.delete()
            else:
                #current_stock.save()
                # new_number = current_stock.number_of_stocks+int(data['units'])
                #current_stock.average_price = ((current_stock.average_price * current_stock.number_of_stocks) + transaction_cost)/new_number 
                current_stock.number_of_stocks = new_number
                current_stock.save()
            resp = {
                'message': 'SUCCESS: The user sold the stock.'
            }
            return HttpResponse(json.dumps(resp), content_type="application/json")
        else:
            resp = {
                'error': 'FAILURE: The user does not have enough stocks to sell.'
            }
            return HttpResponse(json.dumps(resp), content_type="application/json")
        
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
        print("error")
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
        print(current_stock.price_trend)
        stock_data = {
        "name" : current_stock.product_name,
        "num" : this_stock.number_of_stocks,
        "price" : current_stock.stock_price,
        "market_type":current_stock.market_type,
        "price_trend":current_stock.price_trend,
        "average_price":this_stock.average_price, #todo
        "id": current_stock.id,
        }
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
            "market_type": this_stock.market_type,
            "price_trend": this_stock.price_trend,
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
        "num" : num,
        "market_type": this_stock.market_type,
        "price_trend": this_stock.price_trend
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
            stock_temp = this_stock.stockid
            if(stock_temp.market_type=="NYM"):
                crx=ConversionRate.objects.get(var_name="main")
                this_user.net_worth+=(this_stock.number_of_stocks * (this_stock.stockid).stock_price * (crx.conversion_rate/100))
            else:
                this_user.net_worth+=(this_stock.number_of_stocks * (this_stock.stockid).stock_price)
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
    x=10
    d = d[:x]
    d.append({
        'rank':my_pos, 
        'name':current_user.name,
        'net_worth':current_user.net_worth
    })
    return HttpResponse(json.dumps(d), content_type = "application/json")


# This function will be used to login the user via the app. No template rendered.
@csrf_exempt
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')        
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
                'error': 'FAILURE: Please make a POST request.'
            }
        return HttpResponse(json.dumps(msg), content_type="application/json")


@csrf_exempt
def userLogout(request):
    pass

@csrf_exempt
def getnewspost(request):
    global key
    user_key = request.POST.get('key')
    if user_key != key:
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    newsposts = NewsPost.objects.all()
    d=[]
    for this_post in newsposts:
        d.append({
            'time_of_post':str(this_post.time_of_post),
            'post_text':this_post.post_text,
            })
    return HttpResponse(json.dumps(d), content_type="application/json")

@csrf_exempt
def gameswitchstatus(request):
    global key
    user_key = request.POST.get('key')
    if user_key != key:
        
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    gs = GameSwitch.objects.get(switch_name="main")
    resp={
    "status_of_game":gs.game_status,
    }
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def getconversionrate(request):
    cr = ConversionRate.objects.get(var_name="main")
    global key
    user_key = request.POST.get('key')
    if user_key != key:
        resp={
            'error':'The user is not registered yet.'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    resp={
    'conversion_rate': cr.conversion_rate,
    }
    return HttpResponse(json.dumps(resp), content_type = "application/json")

#key for efa = "sms20188593"
@csrf_exempt
def apiforefa(request):
    key_value = "sms20188593" 
    user_key = request.POST.get('key')
    if user_key != key_value:
        
        resp={
            'error':'The API was requested with an invalid key'
        }
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    try:
        email_id = request.POST.get('email')
    except:
        resp={'code':'no such user with the given mail'}
        return HttpResponse(json.dumps(resp), content_type = "application/json")
    current_user = UserProfile.objects.get(mail_id = email)
    balance_change = request.POST.get('balance_change')
    current_user.balance += balance_change
    current_user.save()
    resp={'code':'The User balance was modified'}
    return HttpResponse(json.dumps(resp), content_type = "application/json")