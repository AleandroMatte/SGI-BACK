from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from discipline.models import DisciplineModel
from discipline.serializers.DisciplineSerializer import DiscplineSerializer
from discipline.permission_classes.permissions import HasDisciplineGetPermission


class DisciplinesView(
    generics.ListCreateAPIView
):
    serializer_class = DiscplineSerializer
    queryset = DisciplineModel.objects.all()
    permission_classes = (IsAuthenticated, DjangoModelPermissions, HasDisciplineGetPermission)
