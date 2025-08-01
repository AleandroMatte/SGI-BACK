from rest_framework import permissions


class HasAssetGetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('assets.view_asset')
