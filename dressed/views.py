
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, ProfileEditForm
from .models import *


# Страницы веб-приложения

def home (request):
    return render(request, 'home.html')

def getdressed (request, category_slug=None):
    category_page = None
    products = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=
            category_slug)
        # извлекать товары по категориям
        products = Product.objects.filter(category=category_page, draft=False)
    else:
        products = Product.objects.all().filter(draft=False)
    return render(request, 'getdressed.html', {'category':category_page,
                'products' : products} )

def product (request, category_slug, product_slug):
    product = Product.objects.get(category__slug=category_slug
            , slug= product_slug)
    image = Imagecollection.objects.filter(collectionpresent=product, draft=False)
    return render(request, 'product.html', {'product' : product, 'image' : image})

def teach (request):
    teach  = Course.objects.all()
    return render(request, 'teach.html', {'teach' : teach})

@login_required
def addavatar (request):
    if request.method == "POST":
        profile = ProfileEditForm(initial={'user': request.user})
        form = ProfileEditForm (request.POST, instance=profile)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('/', pk=post.pk)
            except:
                form.add_error(None, 'Can try again')
            
        else:
            form = ProfileEditForm()
    else:
        form = ProfileEditForm(initial={'user': request.user})
    return render(request, 'addavatar.html', {'form': form})

# User
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
 return render(request,'dashboard.html')