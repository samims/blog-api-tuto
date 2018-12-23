from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = "You must be the owner of the object"
    my_safe_method= ['GET', 'PUT']
    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False
    # if request.method in my_safe_method:
    #     return True
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
