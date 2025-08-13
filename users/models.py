from django.contrib.auth.models import AbstractUser
from django.db import models


class SGAUserModel(AbstractUser):
    birth_date = models.DateTimeField(null=False)
    profile_picture = models.ImageField(upload_to="user_profiles/images/", null=True)
    position = models.CharField(max_length=200, null=False)
