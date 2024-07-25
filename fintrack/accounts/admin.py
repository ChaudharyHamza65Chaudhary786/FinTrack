from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'number',
        'category',
        'current_balance',
        'branch',
        'holder',
    )
    list_filter = ('category',)
