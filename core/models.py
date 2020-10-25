from uuid import uuid4

from django.db import models

from accounts.models import User


class Synchronizable(models.Model):
    """
    Base class for models that can be sync'd over a network

    A UUID is used for the primary key, enabling offline creation of new items
    that are later sync'd via the API. Fields are also provided for creation /
    last modification time, and deletion status.
    """

    uuid = models.UUIDField(
        verbose_name="UUID",
        primary_key=True,
        default=uuid4,
        editable=False,
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    # pylint: disable=arguments-differ,unused-argument
    def delete(self, **kwargs):
        """
        Set deleted to True instead of actually deleting the item
        """
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True


class Group(Synchronizable):
    """
    A group of users that share requests
    """

    VISIBILITY_PRIVATE = 'private'  # Users must be approved
    VISIBILITY_UNLISTED = 'unlisted'  # Anyone with the link can join
    VISIBILITY_PUBLIC = 'public'  # group is shown in public lists

    VISIBILITY_CHOICES = (
        (VISIBILITY_PRIVATE, "Private"),
        (VISIBILITY_UNLISTED, "Unlisted"),
        (VISIBILITY_PUBLIC, "Public"),
    )

    name = models.CharField(max_length=100)
    visibility = models.CharField(
        max_length=10,
        choices=VISIBILITY_CHOICES,
    )

    def __str__(self):
        return self.name


class GroupMembership(Synchronizable):
    """
    Subscription to a group
    """

    NOTIFICATIONS_NONE = 'none'  # no notifications are sent for this group
    NOTIFICATIONS_URGENT = 'urgent'  # only urgent notifications are sent
    NOTIFICATIONS_ALL = 'all'  # send notifications for all requests

    NOTIFICATIONS_CHOICES = (
        (NOTIFICATIONS_NONE, "None"),
        (NOTIFICATIONS_URGENT, "Urgent only"),
        (NOTIFICATIONS_ALL, "All"),
    )

    user = models.ForeignKey(
        User,
        related_name='group_memberships',
        on_delete=models.CASCADE,
    )

    group = models.ForeignKey(
        Group,
        related_name='group_memberships',
        on_delete=models.CASCADE,
    )

    is_admin = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    notifications = models.CharField(
        max_length=10,
        choices=NOTIFICATIONS_CHOICES,
    )

    class Meta:
        unique_together = ('user', 'group')


class PrayerRequest(Synchronizable):
    """
    An individual prayer request
    """

    user = models.ForeignKey(
        User,
        related_name='prayer_requests',
        on_delete=models.CASCADE,
    )

    groups = models.ManyToManyField(Group, related_name='prayer_requests')

    title = models.CharField(max_length=200)
    description = models.TextField()

    is_urgent = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(Synchronizable):
    """
    Comment left on a request
    """

    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
    )

    prayer_request = models.ForeignKey(
        PrayerRequest,
        related_name='comments',
        on_delete=models.CASCADE,
    )

    text = models.TextField()
