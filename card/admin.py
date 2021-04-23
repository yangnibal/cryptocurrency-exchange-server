from django.contrib import admin
from .models import Card, Exchange, Crypto, Currency

admin.site.register(Card)
admin.site.register(Exchange)
admin.site.register(Crypto)
admin.site.register(Currency)