"""DZ_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DZ import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                path('admin/', admin.site.urls),
                path('products/', views.index),
                path('products/<int:id>/', views.product_item),
                path('review/', views.review_list),
                path('add_product/', views.add_product),
                path('add_review/', views.add_review),
                path('login/', views.login),
                path('logout/', views.logout),
                path('register/', views.register),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
