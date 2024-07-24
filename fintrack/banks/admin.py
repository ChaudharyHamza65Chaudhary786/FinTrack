from django.contrib import admin

from . models import Bank, Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'bank'
    )

    list_filter = (
        'bank',
    )


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
