from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedAndCanWriteUserOrReadOnly(BasePermission):
    """
    Allow users write access only to themselves
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            (
                request.method in SAFE_METHODS or
                request.user.is_staff or
                request.user.id == obj.id
            )
        )
