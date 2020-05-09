from rest_framework.permissions import BasePermission


class IsNotAdminsUser(BasePermission):

    def has_permission(self, request, view):
        print(request.user.is_staff)
        return bool(not request.user.is_staff)
