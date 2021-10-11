
from shared_security.authentication import get_permission_data
from rest_framework.permissions import BasePermission


class EditPermission(BasePermission):
    def has_permission(self, request, view):
        permission_data = get_permission_data(
            request, '/user/permission/edit/{user_id}'.format(
                user_id=view.kwargs.get('user_id')
            )
        )
        return "edit" in permission_data.get("permission")
        