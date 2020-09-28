from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('trade/', views.trade, name="trade"), 
    path('login/', views.get_login, name="login"),
    path('register/', views.get_registration, name="register"),
    path('register/<str:newuser>/confirm/', views.deposit, name="confirm-user")
]