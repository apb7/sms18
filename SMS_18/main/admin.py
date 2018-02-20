from django.contrib import admin
from .models import UserProfile,StockPurchased,Stock,GameSwitch,NewsPost, ConversionRate
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(StockPurchased)
admin.site.register(Stock)
admin.site.register(GameSwitch)
admin.site.register(NewsPost)
admin.site.register(ConversionRate)