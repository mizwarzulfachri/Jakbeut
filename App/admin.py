from re import search
from django.contrib import admin
from App.models import User, Ceramah

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    listDisplay = ['UserName', 'UserEmail', 'UserPhone', 'UserAddress', 'JoinedDate']
    search_fields = ['UserName', 'UserAddress', 'JoinedDate']
    list_fields = ['JoinedDate']
    list_per_page = 5

admin.site.register(User)
admin.site.register(Ceramah)