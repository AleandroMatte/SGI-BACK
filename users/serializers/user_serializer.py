from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(max_length=200, write_only=True)
    profile_picture = serializers.ImageField(required=False)

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        user = User.objects.create_user(**validated_data)
        user.groups.set([group.id for group in groups_data])
        return user

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "username", "password", "birth_date", "position", "profile_picture", "groups")
