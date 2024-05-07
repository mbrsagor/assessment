from django.contrib import admin
from .models import User


class UserAdminManager(admin.ModelAdmin):
    list_display = ['id', 'uuid', 'email', 'full_name', 'phone', 'is_active', 'is_staff', 'is_superuser']
    list_display_links = ['id', 'uuid', 'email']
    list_filter = ['email', 'phone']
    list_editable = ['full_name', 'phone']


admin.site.register(User, UserAdminManager)
