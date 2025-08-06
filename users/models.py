from django.contrib.auth.models import AbstractUser
from django.db import models


class SGADepartaments(models.Model):
    departament_name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.departament_name


class SGAUserModel(AbstractUser):
    birth_date = models.DateTimeField(null=False)
    profile_picture = models.ImageField(upload_to="user_profiles/images/", null=True)
    departament_id = models.ForeignKey(SGADepartaments, on_delete=models.DO_NOTHING)
    position = models.CharField(max_length=200, null=False)
