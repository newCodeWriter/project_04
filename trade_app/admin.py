from django.contrib import admin
from .models import Account, StockOrder, Watchlist, Position

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'cash_balance')
    list_filter = ('user',)

class StockOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'symbol', 'name', 'price', 'action', 'quantity', 'order_date')
    list_filter = ('user',)


class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'user')
    list_filter = ('user',)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'shares', 'user')
    list_filter = ('user',)


admin.site.register(Account, AccountAdmin)
admin.site.register(StockOrder, StockOrderAdmin)
admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Position, PositionAdmin)