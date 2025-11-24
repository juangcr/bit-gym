import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_basic = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    customer_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username
