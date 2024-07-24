from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'holder_username', 
        'branch_name',
        'title', 
        'number'
    )

    def holder_username(self, obj):
        return obj.holder.username

    def branch_name(self, obj):
        return obj.branch.name
    
    holder_username.short_description = 'Holder'
    branch_name.short_description = 'Branch'


admin.site.register(Account, AccountAdmin)
