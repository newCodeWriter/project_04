from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import requests
# import matplotlib.pyplot as plt
# from matplotlib import style
from datetime import datetime
from .forms import RegisterForm, PasswordChange, PasswordReset
from django.contrib.auth.models import User
from .models import Account
from django.urls import reverse
from django.contrib.auth.views import LoginView


def home(request):
    # # get news headlines
    # news_url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/stories/list"

    # news_query = {"template":"CURRENCY","id":"usdjpy"}

    # bloom_headers = {
    #     'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com",
    #     'x-rapidapi-key': "3031e33fd9msh3c73fd1d3122a19p1a03abjsn0397c5598162"
    # }

    # response = requests.request("GET", news_url, headers=bloom_headers, params=news_query)
    # news_dict = response.json()
    # headline = news_dict['stories'][0:4]

    # for h in headline:
    #     dt = datetime.fromtimestamp(h['published']).strftime("%d %b %Y %H:%M:%S")
    #     dl = datetime.strptime(dt, "%d %b %Y %H:%M:%S")
    #     h['published'] = dl

    # updated_now = datetime.now()

    # # get trending tickers

    # trend_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-trending-tickers"

    # trend_query = {"region":"US"}

    # yahoo_headers = {
    #     'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    #     'x-rapidapi-key': "3031e33fd9msh3c73fd1d3122a19p1a03abjsn0397c5598162"
    # }

    # response = requests.request("GET", trend_url, headers=yahoo_headers, params=trend_query)
    # trend_dict = response.json()
    # latest_trends = trend_dict['finance']['result'][0]['quotes'][0:4]

    # # get popular watchlists

    # pop_url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-popular-watchlists"

    # response = requests.request("GET", pop_url, headers=yahoo_headers)
    # pop_dict = response.json()
    # pop_watch = pop_dict['finance']['result'][0]['portfolios'][0:3]

    # for p in pop_watch:
    #     p['followerCount'] = "{:,}".format(p['followerCount'])
    
    # # get movers

    # movers_url = "https://morning-star.p.rapidapi.com/market/get-movers"

    # movers_query = {"PerformanceId":"0P00001GJH"}

    # morning_headers = {
    #     'x-rapidapi-host': "morning-star.p.rapidapi.com",
    #     'x-rapidapi-key': "3031e33fd9msh3c73fd1d3122a19p1a03abjsn0397c5598162"
    # }

    # response = requests.request("GET", movers_url, headers=morning_headers, params=movers_query)
    # movers_dict = response.json()
    # actives = movers_dict['Top10']['Actives']['Securities'][0:4]
    # gainers = movers_dict['Top10']['Gainers']['Securities'][0:4]
    # losers = movers_dict['Top10']['Losers']['Securities'][0:4]

    # content = {
    #     'news': headline,
    #     'updated': updated_now,
    #     'actives': actives,
    #     'gainers': gainers,
    #     'losers': losers,
    #     'trends': latest_trends,
    #     'popular': pop_watch
    # }
    
    return render(request, 'trade_app/base.html')

def portfolio(request):
    # url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

    # querystring = {"region":"US","symbol":"AMZN"}

    # headers = {
    #     'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    #     'x-rapidapi-key': "3031e33fd9msh3c73fd1d3122a19p1a03abjsn0397c5598162"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    # res_dict = response.json()
    # prices = res_dict['prices'][0:10]

    # # price_list = []

    # for d in prices:
    #     dt = datetime.fromtimestamp(d['date']).strftime("%m/%d/%Y")
    #     d['date'] = dt
    #     d['open'] = "${:,.2f}".format(d['open'])
    #     d['high'] = "${:,.2f}".format(d['high'])
    #     d['low'] = "${:,.2f}".format(d['low'])
    #     d['close'] = "${:,.2f}".format(d['close'])
    #     d['adjclose'] = "${:,.2f}".format(d['adjclose'])
    #     d['volume'] = format(d['volume'], ',')


    # stock = {
    #     'prices': prices
    # }
    return render(request, 'trade_app/portfolio.html')

def trade(request):
    return render(request, 'trade_app/trade.html')

# Forms

def get_registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('confirm-user', args=[request.POST['username']]))
    else:
        form = RegisterForm()

    return render(request, 'trade_app/registration.html', {'form': form})

def deposit(request, newuser):
    add_user = User.objects.get(username=newuser)
    new_user_account = Account(user=add_user, cash_balance=1500)
    new_user_account.save()

    context = {'user': add_user}
    return render(request, 'trade_app/registration-confirmed.html', context)

def user_account(request):
    if request.user.is_authenticated:
        username = request.user.get_username()
    else: 
        username = None

    context = {'user': username}
    return render(request, 'trade_app/user-account.html', context)

def new_pwd_confirmed(request):
    return render(request, 'trade_app/new-pwd-confirmed.html')
