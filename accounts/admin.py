from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Override BaseUserAdmin to add the extra fields
    """

    fieldsets = list(BaseUserAdmin.fieldsets) + [
        (
            "Extra",
            {
                'fields': (
                    'image',
                    'timezone',
                )
            }
        )
    ]
