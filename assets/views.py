from rest_framework import generics
from assets.models.asset_model import Asset
from assets.models.asset_type_model import AssetType
from assets.permission_classes.permissions import HasAssetGetPermission
from assets.serializers.asset_serializer import AssetSerializer
from assets.serializers.asset_type_serializers import AssetTypeSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated


class AssetTypeView(generics.ListCreateAPIView):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer


class AssetTypeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer


class AssetView(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = (IsAuthenticated, DjangoModelPermissions, HasAssetGetPermission)


class AssetDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
