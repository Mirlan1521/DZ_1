from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput, NumberInput, Select

from .models import Product, Review


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'title  description price category'.split()
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название продукта'
                }
            ),
            'description': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите описание продукта'
                }
            ),
            'price': NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'category': Select(
                attrs={
                    'class': 'form-control',

                }
            )
        }


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = 'text product'.split()
        widgets = {
            'text': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите текст'
                }
            ),
            'author': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите ник'
                }
            )

        }


class UserRegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Пароль',
                                          'class': 'form-control'}
                               ))
    password1 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': ' Повторите Пароль',
                                           'class': 'form-control'}
                                ))

    def clean_email(self):
        users = User.objects.filter(username=self.cleaned_data['email'])
        if users.count() > 0:
            raise ValidationError('Эта почта уже используется!')




