from rest_framework import serializers
from django.contrib.auth import models



class GroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Permission.objects.all())
    class Meta:
        model = models.Group
        fields = ('id', 'name', 'permissions')