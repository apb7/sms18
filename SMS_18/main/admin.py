from django.contrib import admin
from .models import UserProfile,StockPurchased,Stock,GameSwitch, StockPriceVariation
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(StockPurchased)
admin.site.register(Stock)
admin.site.register(GameSwitch)
admin.site.register(StockPriceVariation)

