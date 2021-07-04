from django import forms
from .models import Product, Review


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'title  description price category'.split()


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = 'text product'.split()


