from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game$', views.game , name='game'),
    url(r'^buystocks$', views.BuyStocks , name='BuyStocks'),
    url(r'^sellstocks$', views.SellStocks , name='SellStocks'),
    url(r'^userprimarydetails$', views.UserPrimaryDetails , name='UserPrimaryDetails'),
    url(r'^userstockdetails$', views.UserStockDetails , name='UserStockDetails'),
    url(r'^stocksprimarydata$', views.StocksPrimaryData , name='StocksPrimaryData'),
    url(r'^lbdata$', views.LBdata , name='LBdata'),
]