from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game$', views.game , name='game'),
    url(r'^buystocks/(?P<id>\d+)$', views.BuyStocks , name='BuyStocks'),
	url(r'^buy/(?P<id>\d+)$', views.buy, name='buy'),
    url(r'^sellstocks/(?P<id>\d+)$', views.SellStocks , name='SellStocks'),
	url(r'^sell/(?P<id>\d+)$', views.sell, name='sell'),
    url(r'^userprimarydetails$', views.UserPrimaryDetails , name='UserPrimaryDetails'),
    url(r'^userstockdetails$', views.UserStockDetails , name='UserStockDetails'),
    url(r'^stocksprimarydata$', views.StocksPrimaryData , name='StocksPrimaryData'),
    url(r'^stockdata/(?P<id>\d+)$', views.StockData , name='StockData'),
    url(r'^leaderboard$', views.leaderboard , name='leaderboard'),
    url(r'^lbdata$', views.LBdata , name='LBdata'),
    url(r'^createProfile$', views.createProfile , name='createProfile'),
    url(r'^profile$', views.profile , name='profile'),
    url(r'^register$', views.register , name='register'),
    url(r'^login$', views.login , name='login'),
    url(r'^logout$', views.logout , name='logout'),
]
