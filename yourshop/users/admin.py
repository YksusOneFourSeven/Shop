from .models import Account
from django.contrib import admin

class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'email']

admin.site.register(Account, AccountAdmin)