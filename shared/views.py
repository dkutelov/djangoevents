from django.core.exceptions import PermissionDenied


class ModifyPermissionMixin:
    groups = None

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if 'Admin' not in user.groups:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)