from rest_framework import generics
from django.contrib.auth import models
from rest_framework.authentication import TokenAuthentication
from users.serializers.group_serializer import GroupSerializer


class GroupDetailsViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = ()


class GroupViews(generics.ListCreateAPIView):
    queryset = models.Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = ()
