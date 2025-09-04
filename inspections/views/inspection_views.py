from django.shortcuts import render
from rest_framework import generics, permissions

from inspections.models import InspectionModel
from inspections.serializers.inspection_serializer import InspectionSerializer


class InspectionListCreateView(generics.ListCreateAPIView):
    queryset = InspectionModel.objects.all()
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
    serializer_class = InspectionSerializer


class InspectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InspectionModel.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = InspectionSerializer


class InspectionByAssetView(generics.ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = InspectionSerializer

    def get_queryset(self):
        asset_id = self.kwargs['assetId']
        return InspectionModel.objects.filter(asset=asset_id).all()
