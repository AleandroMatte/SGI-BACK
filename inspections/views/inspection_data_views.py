from rest_framework import generics
from rest_framework import permissions
from inspections.models import InspectionData
from inspections.serializers.inspection_data_serializer import InspectionDataSerializer


class InspectionDataListCreate(
    generics.ListCreateAPIView
):
    permission_classes = (permissions.AllowAny,)
    serializer_class = InspectionDataSerializer

    def get_queryset(self):
        inspection_fk = self.kwargs["inspection_id"]
        return InspectionData.objects.filter(inspection=inspection_fk).all()
