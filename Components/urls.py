from django.urls import path
from django.utils.regex_helper import next_char
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('contact/', views.contact_view, name='contact'),
    path('shop/', views.shop_view, name='shop'),
    path('cart/', views.cart_view, name='cart'),
    path('about/', views.about_view, name='about'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('thank/', views.thank_view, name='thank'),
    path('single/<pk>/', views.single_view, name='single'),
    path('sell/', views.sell_view, name='sell')
]
