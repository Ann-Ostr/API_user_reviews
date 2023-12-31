from rest_framework import permissions


class IsSuperUser(permissions.IsAdminUser):
    """Права доступа для суперпользователя."""
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsAdminOrReadOnly(permissions.BasePermission):
    """Права доступа для админа."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_superuser)


class IsGodsOrReadOnly(permissions.BasePermission):
    """Разрешение на редактирование автором или модератором/админом."""
    message = 'Редактирование доступно только авторам.'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_admin
                or request.user.is_moderator)
