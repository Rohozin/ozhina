
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, request
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm,UserRegistrationForm, UserEditForm, ProfileEditForm, OrderEditForm, OrderFormTeach
from .models import Category,Presentation,Product,Imagecollection,Profile,Course,Imagecourse,OrderTeach,Order




# Страницы веб-приложения

def home (request):
    return render(request, 'home.html')

def getdressed (request, category_slug=None):
    category_page = None
    products = None
    present = Presentation.objects.all()
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=
            category_slug)
        # извлекать товары по категориям
        products = Product.objects.filter(category=category_page, draft=False)
    else:
        products = Product.objects.all().filter(draft=False)
    return render(request, 'getdressed.html', {'category':category_page,
                'products' : products, 'present':present} )


def product (request, category_slug, product_slug):
    product = Product.objects.get(category__slug=category_slug
            , slug= product_slug, draft=False)
    image = Imagecollection.objects.filter(collectionpresent=product, draft=False)
    return render(request, 'product.html', {'product' : product, 'image' : image})



def teach (request):
    list = Course.objects.filter(is_published=True)
    collage = Imagecourse.objects.all()
    return render(request, 'teach.html',{'list' : list, 'collage' : collage})   


def political (request):
    return render(request, 'political.html')



@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                        data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'data storage')
        else:
            messages.error(request, 'error updating your data')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        
    return render(request,'addavatar.html',{'user_form' : user_form, 'profile_form' : profile_form})

# Forms
def order_create(request):

    if request.method == 'POST':
        order_form = OrderEditForm(data=request.POST,
                                    files=request.FILES)
        if order_form.is_valid():
            try:
                Order.objects.create(**order_form.cleaned_data)
                return redirect('getdressed')
            except:
                order_form.add_error(None, 'Error orders')
            order_form.save()
    else:
        order_form = OrderEditForm ()
    return render(request,'order_create.html',{'order_form' : order_form})                                   

def teach_created(request):

    if request.method == 'POST':
        teach_form = OrderFormTeach(data=request.POST)
        if teach_form. is_valid():
            try:
                OrderTeach.objects.create(**teach_form.cleaned_data)
                return redirect('teach')
            except:
                teach_form.add_error(None, 'Error orders')
            teach_form.save()
    else:
        teach_form = OrderFormTeach()
    return render(request,'teach_created.html',{'teach_form': teach_form})

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

def register (request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            
            new_user = user_form.save(commit=False)
            # Создаем пользователю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])
            # Сохраняем пользоваетля в базе данных.
            new_user.save()
            # Создание дополнительных данных профиля пользователя.
            Profile.objects.create(user=new_user)
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render (request, 'registration/register.html', {'user_form': user_form})