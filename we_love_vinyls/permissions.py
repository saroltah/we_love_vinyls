from rest_framework import permissions

class IsMemberOrReadOnly(permissions.BasePermission):

    def __init__(self, user_field='member'):
        self.user_field = user_field

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, self.user_field) == request.user

class IsOrganizerOrReadOnly(IsMemberOrReadOnly):
    def __init__(self):
        super().__init__(user_field='organizer')

class IsAdvertiserOrReadOnly(IsMemberOrReadOnly):
    def __init__(self):
        super().__init__(user_field='advertiser')