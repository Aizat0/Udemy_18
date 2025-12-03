from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Тек эле объекттун owner'у өзгөртө алсын, башкалар окуй алат.
    Модельге 'owner' же 'user' деген поле бар деп кабыл алдык — сенин моделдерге тууралап кой.
    """
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS: GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # Эгер модельде owner же user талаасы бар болсо:
        return getattr(obj, "owner", None) == request.user or getattr(obj, "user", None) == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Админ эмес колдонуучуларга окууга уруксат, өзгөртүүгө админ гана.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

