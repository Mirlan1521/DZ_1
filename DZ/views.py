import secrets

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import ProductCreateForm, ReviewCreateForm, UserRegisterForm
from .models import Category, Review, Product


def index(request):
    products = Product.objects.all()
    data = {
        'title': "Все продукты",
        'product': products
    }
    return render(request, 'index.html', context=data)


def product_item(request, id):
    reviews = Review.objects.filter(product_id=id)
    products = Product.objects.get(id=id)
    data = {
        'products': products,
        'reviews': reviews
    }
    return render(request, 'products.html', context=data)


def review_list(request):
    text = request.GET.get('search_text', '')
    reviews = Review.objects.filter(text__contains=text)
    product = request.GET.get('products', '')
    if product != '':
        reviews = reviews.filter(product_id=int(product))
    return render(request, 'review.html', context={
        'reviews': reviews,
        'products': Product.objects.all()
    })


def add_product(request):
    if request.method == 'GET':
        print('GET')
        form = ProductCreateForm()
        data = {
            'form': form
        }
        return render(request, 'add.html', context=data)
    elif request.method == 'POST':
        print('POST')
        print(request.POST)
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/')
        else:
            return render(request, 'add.html',
                          context={'form': form})


@login_required(login_url='/login/')
def add_review(request):
    if request.method == 'GET':
        form = ReviewCreateForm()
        data = {
            'form': form
        }
        return render(request, 'add_review.html', context=data)
    elif request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products/')
        else:
            return render(request, 'add_review.html',
                          context={'form': form})


from django.contrib import auth


def login(request):
    data = {}
    next = (request.GET.get('next'))
    if next:
        data['message'] = 'Авторизуйтесь чтобы добавить отзыв'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/products/')
        else:
            data['message'] = 'Введите правильные данные!!!'
    return render(request, 'login.html', context=data)


def logout(request):
    auth.logout(request)
    return redirect('/products/')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=request.POST['email'],
                password=request.POST['password'],
                is_active=True)
            # code = secrets.token_urlsafe(16)
            send_mail(
                subject='Test subject',
                message='Test massage',
                from_email=settings.EMAIL_HOST,
                recipient_list=[request.POST['email']]
            )
        else:
            return render(request, 'register.html', context={'form': form})
    data = {
        'form': UserRegisterForm()
    }
    return render(request, 'register.html', context=data)
