from django.shortcuts import render
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
