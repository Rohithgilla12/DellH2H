from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class ProfileInline(admin.StackedInline):
    model = UserDetails
    can_delete = False
    verbose_name_plural = 'UserDetails'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_select_related = ('UserDetails', )
    
# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(UserDetails)