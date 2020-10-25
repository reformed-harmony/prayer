from django.contrib import admin

from .models import \
    Comment, \
    Group, \
    GroupMembership, \
    PrayerRequest


class SynchronizableAdmin(admin.ModelAdmin):
    """
    Common admin fields for Synchronizable models
    """

    fieldsets = [
        (
            "Synchronizable",
            {
                'fields': (
                    'uuid',
                    'created',
                    'modified',
                    'is_deleted',
                )
            }
        )
    ]
    list_filter = [
        'created',
        'modified',
        'is_deleted',
    ]
    readonly_fields = [
        'uuid',
        'created',
        'modified',
    ]


@admin.register(Group)
class GroupAdmin(SynchronizableAdmin):
    fieldsets = [
        (
            '',
            {
                'fields': (
                    'name',
                    'visibility',
                )
            }
        )
    ] + SynchronizableAdmin.fieldsets
    list_display = [
        'name',
        'visibility',
    ]
    list_filter = [
        'visibility',
    ] + SynchronizableAdmin.list_filter


@admin.register(GroupMembership)
class GroupMembershipAdmin(SynchronizableAdmin):
    fieldsets = [
        (
            '',
            {
                'fields': (
                    'user',
                    'group',
                    'is_admin',
                    'is_approved',
                )
            }
        )
    ] + SynchronizableAdmin.fieldsets
    list_display = [
        'user',
        'group',
        'is_admin',
        'is_approved',
    ]
    list_filter = [
        'user',
        'group',
        'is_admin',
        'is_approved',
    ] + SynchronizableAdmin.list_filter


@admin.register(PrayerRequest)
class PrayerRequestAdmin(SynchronizableAdmin):
    fieldsets = [
        (
            '',
            {
                'fields': (
                    'user',
                    'groups',
                    'title',
                    'description',
                    'is_urgent',
                )
            }
        )
    ] + SynchronizableAdmin.fieldsets
    list_display = [
        'title',
        'user',
        'is_urgent',
    ]
    list_filter = [
        'user',
        'groups',
        'is_urgent',
    ] + SynchronizableAdmin.list_filter


@admin.register(Comment)
class CommentAdmin(SynchronizableAdmin):
    fieldsets = [
        (
            '',
            {
                'fields': (
                    'user',
                    'prayer_request',
                    'text',
                )
            }
        )
    ] + SynchronizableAdmin.fieldsets
    list_display = [
        'user',
        'prayer_request',
    ]
    list_filter = [
        'user',
        'prayer_request',
    ] + SynchronizableAdmin.list_filter
