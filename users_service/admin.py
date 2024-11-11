from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

#admin.site.register(User)
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom Admin for user model to display email,username,role in admin panel
    """
    list_display = ('email','username','role','is_staff')
    search_fields = ('email','username')
    ordering = ('email',)
