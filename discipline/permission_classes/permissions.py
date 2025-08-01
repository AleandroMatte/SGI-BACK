from rest_framework import permissions


class HasDisciplineGetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('discipline.view_disciplinemodel')
