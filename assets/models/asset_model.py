import uuid
from django.db import  models

from assets.models.asset_type_model import AssetType


class Asset(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, auto_created=True, unique=True)
    asset_identifier = models.CharField(null=False, max_length=200)
    asset_lat = models.CharField(null=False, max_length=15)
    asset_long = models.CharField(null=False, max_length=15)
    asset_type_fk = models.ForeignKey(AssetType, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)