from django.db import models


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    name = models.CharField(max_length=255, verbose_name='Имя')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField('Название', max_length=255, null=False)
    description = models.CharField('Описание', max_length=255, null=False)
    price = models.IntegerField('Цена', default=0)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    text = models.CharField('Текст', max_length=255)
    author = models.CharField('Автор', max_length=255, null=True)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
