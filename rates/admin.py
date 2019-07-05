from django.contrib import admin
from .models import *

class CurrencyAdmin(admin.ModelAdmin):

    list_display = ('h10_id', 'country_name','currency_name')

admin.site.register(Currency, CurrencyAdmin)

class RateAdmin(admin.ModelAdmin):

    list_display = ('currency', 'rate_date','per_dollar')

admin.site.register(Rate, RateAdmin)

