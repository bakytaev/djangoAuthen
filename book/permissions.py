from rest_framework.permissions import BasePermission, SAFE_METHODS


class SomePermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.username == 'test':
            return True
        elif request.method in SAFE_METHODS:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True
