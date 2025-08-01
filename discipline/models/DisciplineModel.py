import uuid
from django.db import models

# Create your models here.
class DisciplineModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, auto_created=True, unique=True)
    name = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"{self.name}"