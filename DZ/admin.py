from django.contrib import admin
from DZ.models import Category, Product, Review


class ProductInline(admin.StackedInline):
    model = Product
    fields = 'title description'.split()
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


class ProductCategoryReview(admin.ModelAdmin):
    list_display = 'id title description  price '.split()
    search_fields = 'title'.split()
    list_filter = 'category'.split()
    list_editable = 'description price'.split()


class ReviewAdmin(admin.ModelAdmin):
    list_display = 'id text  author product '.split()


# Register your models here.


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductCategoryReview)
admin.site.register(Review, ReviewAdmin)
