from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Allows access only for authorised users or administrators.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user in obj.users.all()
