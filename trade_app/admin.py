from django.contrib import admin
from .models import Account, Order, Watchlist, Position

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'cash_balance')
    list_filter = ('user',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'shares', 'paid', 'date', 'user')
    list_filter = ('user', 'date')

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'user')
    list_filter = ('user',)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'shares', 'user')
    list_filter = ('user',)

admin.site.register(Account, AccountAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Position, PositionAdmin)