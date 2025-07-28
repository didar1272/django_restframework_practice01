from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    """
    Custom permission to only allow staff users to edit products.
    """
    perms_map = {
        'GET': ['%(app_label)s.add_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # def has_permission(self, request, view):
    #     if request.user and request.user.is_staff:
    #         if request.user.has_perm('products.view_product'):
    #             return True
    #         if request.user.has_perm('products.add_product'):
    #             return True
    #         if request.user.has_perm('products.update_product'):
    #             return True
    #         if request.user.has_perm('products.delete_product'):
    #             return True
    #     return False