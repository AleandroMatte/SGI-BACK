import uuid
from django.db import models

from django.core.exceptions import ValidationError
from assets.models.asset_type_model import AssetType
from django.utils.translation import gettext_lazy as _


def validate_lat_long(value: str):
    # @Author Aleandro Matteoni
    # Since the frontend LatLng may be incompatible with longer values for coordinates
    # check if formatting is right
    if "." not in value or value.count(".") > 1:
        raise ValidationError(
            _("%(value)s is not a valid coordinate"),
            params={"value": value},
        )
    # check if the coordinates have a valid amount of digits before the '.'
    if len(value.split(".")[0]) < 2 or       len(value.split(".")[0]) > 4:
        raise ValidationError(
            _("%(value)s a coordinate must have at least 2 characters before the point and at max 4."),
            params={"value": value},
        )
    # check if it has exactly 5 decimal places
    if not 4 < len(value.split(".")[1]) < 6:
        raise ValidationError(
            _("%(value)s a coordinate precision must be no smaller and no larger than 5."),
            params={"value": value},
        )


class Asset(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, auto_created=True, unique=True)
    asset_image = models.ImageField(upload_to="assets/images/", null=True)
    asset_identifier = models.CharField(null=False, max_length=200)
    asset_lat = models.CharField(null=False, max_length=9, validators=[validate_lat_long])
    asset_long = models.CharField(null=False, max_length=9, validators=[validate_lat_long])
    asset_type_fk = models.ForeignKey(AssetType, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"{self.id} - {self.asset_identifier}"
