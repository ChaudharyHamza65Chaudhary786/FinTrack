from django.contrib import admin

from . models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'category',
        'transaction_from_account',
        'description'
    )

    list_filter = (
        'category',
        'transaction_from_account',
        'is_reverted'
    )
