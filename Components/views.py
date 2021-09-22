from Components.forms import ProductForm
from django.contrib.auth import forms
from Components.models import Product
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    return render(request, 'Components/index.html', context)

def contact_view(request):
    return render(request, 'Components/contact.html')

def shop_view(request):
    return render(request, 'Components/shop.html')

def cart_view(request):
    return render(request, 'Components/cart.html')

def checkout_view(request):
    return render(request, 'Components/checkout.html')

def thank_view(request):
    return render(request, 'Components/thankyou.html')

def about_view(request):
    return render(request, 'Components/about.html')

def single_view(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        'product': product
    }
    return render(request, 'Components/shop-single.html', context)

def sell_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('something is off')

    context = {
        'form': form
    }            
    return render(request, 'Components/sell.html', context)

class UserLogin(LoginView):
    template_name = 'Components/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')

def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }

    return render(request, 'Components/register.html', context)