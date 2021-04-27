from rest_framework import permissions

class IsMineOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.role == '10':
                return True
            elif request.method in permissions.SAFE_METHODS:
                return True
            elif request.user.id == obj.id:
                return True
            return False
        else:
            return False