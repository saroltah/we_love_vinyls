from rest_framework import permissions

class IsMemberOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.member == request.user

class IsOrganizerOrReadOnly(IsMemberOrReadOnly):
    member_field = 'organizer'