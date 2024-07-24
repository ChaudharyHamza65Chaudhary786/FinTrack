from django.contrib import admin

from . models import User


@admin.register(User)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'username',
    )
