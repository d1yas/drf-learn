# from rest_framework.permissions import BasePermission, SAFE_METHODS


# class IsAuthorOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.user.is_authenticated:
#             return True
#         else: return False


#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return obj.author == request.user
#         else: return False