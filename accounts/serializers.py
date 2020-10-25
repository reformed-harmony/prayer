from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User objects
    """

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'image',
            'image_url',
            'timezone',
        ]
        extra_kwargs = {
            'image': {'write_only': True},
        }
