from rest_framework import generics

from .models import User
from .permissions import IsAuthenticatedAndCanWriteUserOrReadOnly
from .serializers import UserSerializer


class ListUsersView(generics.ListAPIView):
    """
    List user objects
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class RetrieveOrUpdateUserView(generics.RetrieveUpdateAPIView):
    """
    Read or update user objects

    Regular users may only update their own profile.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedAndCanWriteUserOrReadOnly]
