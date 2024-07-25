from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'description',
        'category',
        'date',
        'amount',
        'is_reverted',
        'transaction_from_account',
    )
    list_filter = ('date', 'is_reverted')
