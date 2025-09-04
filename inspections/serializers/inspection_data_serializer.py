from rest_framework import serializers
from rest_framework import status

from inspections.models import InspectionData


class InspectionDataSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        if attrs["inspection_field_data_is_file"] and not attrs.get("inspection_field_file"):
            raise serializers.ValidationError(
                "inspection_field_data_is_file indicates that a file should be sent at key 'inspection_field_file'",
                status.HTTP_400_BAD_REQUEST
            )
        return super().validate(attrs)

    class Meta:
        fields = "__all__"
        model = InspectionData
