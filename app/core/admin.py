from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core.models import Profile

User = get_user_model()
# from core.models import Employee, Post
# # Register your models here.


admin.site.register(Profile)

class UserAdmin(BaseUserAdmin):
    """ Custom class for Django Admin user manager """
    ordering = ['id']
    list_display = ('email', 'first_name',
                    'last_name', 'user_type',
                    'is_active', 'slug')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',
                       'first_name', 'last_name', 'user_type')
        }),
    )


admin.site.register(User, UserAdmin)
