from django.contrib import admin

from .models import Bank, Branch


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'address', 'phone_number', 'bank')
    list_filter = ('bank',)
    search_fields = ('name',)
