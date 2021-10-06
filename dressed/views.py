from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


from .forms import SignUpForm
from .models import Category, Product, Imagecollection
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

@login_required
def product (request, category_slug, product_slug):
    product = Product.objects.get(category__slug=category_slug
            , slug= product_slug)
    image = Imagecollection.objects.filter(collectionpresent=product, draft=False)
    return render(request, 'product.html', {'product' : product, 'image' : image})



def teach (request):
    return render(request, 'teach.html')


# User
def signUpView(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			signup_user = User.objects.get(username= username)
			user_group = Group.objects.get(name= 'User')
			user_group.user_set.add(signup_user)
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})

def loginView (request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect ('home')
            else:
                return redirect('signap')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signoutView(request):
    logout(request)
    return redirect('login')