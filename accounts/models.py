import hashlib

from django.contrib.auth.models import AbstractUser
from django.db import models
from pytz import common_timezones


class User(AbstractUser):
    """
    Custom user model

    Users can customize their profile image and timezone.
    """

    image = models.ImageField(
        upload_to='user-images',
        blank=True,
    )

    def image_url(self):
        """
        Return the image URL that should be displayed (Gravatar fallback)
        """
        if self.image:
            return self.image.url
        return 'https://www.gravatar.com/avatar/{}?s=512&d=identicon'.format(
            hashlib.md5(self.email.encode('utf-8')).hexdigest(),
        )

    timezone = models.CharField(
        max_length=40,
        choices=[(t, t) for t in common_timezones],
        default='UTC',
    )

    def __str__(self):
        """
        Display a user's name as neatly as possible
        """
        if self.first_name and self.last_name:
            return "{} {}".format(
                self.first_name,
                self.last_name,
            )
        return self.username
