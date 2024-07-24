from django.contrib import admin

from . models import Bank, Branch


class BranchAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'bank'
    )

    list_filter = (
        'bank',
    )


admin.site.register(Bank)
admin.site.register(Branch, BranchAdmin)
