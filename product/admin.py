from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_select_related = ('profile', )

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Profile)