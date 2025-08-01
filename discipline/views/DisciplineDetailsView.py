from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from discipline.models import DisciplineModel
from discipline.serializers.DisciplineSerializer import DiscplineSerializer
from discipline.permission_classes.permissions import HasDisciplineGetPermission


class DisciplineDetailsView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = DiscplineSerializer
    queryset = DisciplineModel.objects.all()
    permission_classes = (IsAuthenticated, DjangoModelPermissions, HasDisciplineGetPermission)
