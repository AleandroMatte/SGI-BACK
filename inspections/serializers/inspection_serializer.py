from rest_framework import serializers

from inspections.models import InspectionModel


class InspectionSerializer(serializers.ModelSerializer):
    user_email = serializers.SlugRelatedField(read_only=True, many=False, slug_field='email', source='user')
    asset_name = serializers.SlugRelatedField(read_only=True, many=False, slug_field='asset_identifier', source='asset')
    inspection_date = serializers.DateTimeField(format='%d/%m/%Y')

    class Meta:
        fields = "__all__"
        model = InspectionModel
