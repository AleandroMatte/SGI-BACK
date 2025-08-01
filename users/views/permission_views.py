from rest_framework.generics import ListAPIView
from django.contrib.auth.models import Permission

from users.serializers.permission_serializer import PermissionSerializer


class PermissionListView(ListAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
