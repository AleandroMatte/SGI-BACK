import uuid
from django.db import  models

from discipline.models import DisciplineModel


class AssetType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, auto_created=True, unique=True)
    asset_type_name = models.CharField(null=False, max_length=300)
    discipline_fk = models.ForeignKey(DisciplineModel, on_delete=models.PROTECT, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"{self.asset_type_name} - {self.discipline_fk.__str__()}"
