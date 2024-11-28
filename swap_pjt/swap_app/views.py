from django.shortcuts import render,get_object_or_404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . models import *
from . forms import *
import stripe
from django.contrib import messages
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def home(request):
    return render(request,'home.html')
def navbar(request):
    return render(request,'navbar.html') 
def footer(request):
    return render(request,'footer.html')
def admin_page(request):
    return redirect('/admin/') 
def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'home.html', {'brands': brands})

def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Success You can Login Now...!')
            return redirect('login')
    return render(request, 'register.html',{'form':form})

def login_page(request):
   if request.method=='POST':
       name=request.POST.get('username')
       pwd=request.POST.get('password')
       user=authenticate(request,username=name,password=pwd)
       if user is not None:
           login(request,user)
           messages.success(request,'Successfully logged in')
           return redirect('/')
       else:
           messages.error(request,'Invalid User name or Password')
           return redirect('login')
   return render(request, 'login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out Successfully')
    return redirect('/')


def brand_model_detail(request, name):
    if request.user.is_authenticated:
        brand = get_object_or_404(Brand, name=name)
        brand_models = BrandModel.objects.filter(model_name=brand)
        return render(request, 'brand_model_detail.html', {
            'brand': brand,
            'brand_models': brand_models,
    })
    else:
        return redirect('login')


def add_brand_model(request):
    if request.method == 'POST':
        form = BrandModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('brand_list') 
    else:
        form = BrandModelForm()
    
    return render(request, 'add_brand_model.html', {'form': form})


def success(request):
    return render(request,'success.html')


def checkout(request):
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'product_data': {
                    'name': 'Swap your Dream car',
                },
                'unit_amount': 500000, 
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'), 
         
    )

    return redirect(checkout_session.url, code=303)