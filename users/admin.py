from django.contrib import admin

from users.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
                    'id',
                    'username',
                    'email',
                    'phone')

