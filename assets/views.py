from rest_framework import generics
from rest_framework.permissions import AllowAny
from assets.models.asset_model import Asset
from assets.models.asset_type_model import AssetType
from assets.serializers.asset_serializer import AssetSerializer
from assets.serializers.asset_type_serializers import AssetTypeSerializer


class AssetTypeView(generics.ListCreateAPIView):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()


class AssetTypeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssetType.objects.all()
    serializer_class = AssetTypeSerializer
    permission_classes = (AllowAny,)


class AssetView(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()


class AssetDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()
