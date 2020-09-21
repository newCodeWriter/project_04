import matplotlib.pyplot as plt
from matplotlib import style
from datetime import datetime
from django.shortcuts import render
import requests


def home(request):

    url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/news/list"

    querystring = {"id":"stocks"}

    headers = {
        'x-rapidapi-host': "bloomberg-market-and-financial-news.p.rapidapi.com",
        'x-rapidapi-key': "3031e33fd9msh3c73fd1d3122a19p1a03abjsn0397c5598162"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res_dict = response.json()
    headline = res_dict['modules'][0]['stories']
    # title = headline['title']
    # summary = headline['summary']
    # published = headline['published']
    # short_url = headline['shortURL']

    for d in headline:
        dt = datetime.fromtimestamp(d['published']).strftime("%m/%d/%Y")
        d['published'] = dt

    news = {
        'news': headline
    }
    
    return render(request, 'base.html', news)

def portfolio(request):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v3/get-historical-data"

    querystring = {"region":"US","symbol":"AMZN"}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "3031e33fd9msh3c73fd1d3122a19p1a03abjsn0397c5598162"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res_dict = response.json()
    prices = res_dict['prices'][0:10]

    # price_list = []

    for d in prices:
        dt = datetime.fromtimestamp(d['date']).strftime("%m/%d/%Y")
        d['date'] = dt
        d['open'] = "${:,.2f}".format(d['open'])
        d['high'] = "${:,.2f}".format(d['high'])
        d['low'] = "${:,.2f}".format(d['low'])
        d['close'] = "${:,.2f}".format(d['close'])
        d['adjclose'] = "${:,.2f}".format(d['adjclose'])
        d['volume'] = format(d['volume'], ',')


    stock = {
        'prices': prices
    }
    return render(request, 'portfolio.html', stock)

def trade(request):
    return render(request, 'trade.html')

