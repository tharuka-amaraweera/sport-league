from rest_framework import permissions


class TeamCoachOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.team.teamcoach)
        view_permission = bool(obj.team.teamcoach ==
                               request.user or request.user.is_superuser)
        if view_permission:
            return True
        else:
            return False
