from rest_framework import serializers

from discipline.models import DisciplineModel


class DiscplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplineModel
        fields = '__all__'
