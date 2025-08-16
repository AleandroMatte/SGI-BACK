from rest_framework import serializers

from assets.models.asset_model import Asset


class AssetTypeRelationSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.asset_type_name}"


class AssetSerializer(serializers.ModelSerializer):
    asset_type = AssetTypeRelationSerializer(many=False, read_only=True, source="asset_type_fk")
    created_at = serializers.DateTimeField(format='%d/%m/%Y')

    class Meta:
        model = Asset
        fields = '__all__'
