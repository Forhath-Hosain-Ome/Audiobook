from django.db import models
from uuid import uuid4

class BaseModel(models.Model):
    uuid_pk = models.UUIDField(default=uuid4, editable=False, unique=True)
    is_completed = models.BooleanField(default=False)
    is_damaged = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True