import os
from django.utils.text import slugify
from django.db import models
from django.conf import settings
from uuid import uuid4
from django.contrib.auth import get_user_model
User = get_user_model()

class BaseModel(models.Model):
    uuid_pk = models.UUIDField(default=uuid4, editable=False, unique=True)
    is_completed : bool = models.BooleanField(default=False)
    is_damaged : bool = models.BooleanField(default=False)
    created_at : bool = models.DateTimeField(auto_now_add=True)
    updated_at : bool = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BaseUIModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    logo = models.ImageField(upload_to='logo/')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="%(class)s_created"
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null=True, blank=True, related_name="%(class)s_updated"
    )
    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_deleted"
    )
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    color = models.CharField(max_length=20, default='000000')
    font_size = models.PositiveIntegerField(default=14)
    font_family = models.CharField(max_length=50, default='Arial')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        abstract = True
        ordering = ['-updated_at', '-created_at']
        verbose_name = "Base UI Model"
        verbose_name_plural = "Base UI Models"

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def navbar_icon_upload_to(instance, filename):
        base, ext = os.path.splitext(filename)
        slug = slugify(instance.title)
        return f'navbar_icons/{slug}{ext}'

    def __str__(self):
        return getattr(self, 'name', f"{self.__class__.__name__} #{self.pk}")