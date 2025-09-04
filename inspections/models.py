import uuid
from django.db import models

from assets.models.asset_model import Asset
from users.models import SGAUserModel


class InspectionModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, auto_created=True, unique=True)
    inspection_date = models.DateTimeField(auto_now_add=True, null=False)
    user = models.ForeignKey(SGAUserModel, on_delete=models.DO_NOTHING, null=False)
    asset = models.ForeignKey(Asset, on_delete=models.DO_NOTHING, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"{self.id} - {self.inspection_date}"


class InspectionData(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, auto_created=True, unique=True)
    inspection = models.ForeignKey(InspectionModel, on_delete=models.DO_NOTHING, null=False)
    inspection_field = models.CharField(max_length=500, null=False)
    inspection_field_data = models.CharField(max_length=500, null=True)
    inspection_field_data_is_file = models.BooleanField(default=False, null=False)
    inspection_field_file = models.FileField(upload_to="assets/inspections/images", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
