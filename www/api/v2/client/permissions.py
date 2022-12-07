from rest_framework.permissions import IsAuthenticated


class IsAdminPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view)
