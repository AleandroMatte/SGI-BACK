from rest_framework import serializers
from assets.models.asset_type_model import AssetType


class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = '__all__'
