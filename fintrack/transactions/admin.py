from django.contrib import admin

from . models import SubCategory, Category, Transaction

admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Transaction)
