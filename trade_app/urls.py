from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from .forms import LoginForm, PasswordChange

urlpatterns = [
    path('', views.home, name="home"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('trade/', views.trade, name="trade"), 
    path('login/', LoginView.as_view(template_name='trade_app/login.html', authentication_form=LoginForm), name="login"),
    path('login/user/', views.user_account, name="useract"),
    path('logout/', LogoutView.as_view(template_name='trade_app/logout.html'), name="logout"),
    path('register/', views.get_registration, name="register"),
    path('register/<str:newuser>/confirm/', views.deposit, name="confirm-user"),
    path('password_change/', PasswordChangeView.as_view(template_name='trade_app/pwd-change.html', success_url='confirmed', form_class=PasswordChange), name="pwd-change"),
    path('password_change/confirmed', views.new_pwd_confirmed, name="pwd_confirmed")

]