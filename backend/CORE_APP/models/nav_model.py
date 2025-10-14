from django.contrib.auth.models import Group
from django.db import models
from .base_model import BaseUIModel
from .icon_model import IconModel

class NavbarModel(BaseUIModel):
    POSITION_CHOICES = [
        ('TOP', 'Top Navbar'),
        ('SIDE', 'Sidebar'),
        ('FOOTER', 'Footer Menu'),
    ]
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    icon = models.ForeignKey(
        IconModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='navbar_items'
    )
    show_icon = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_dropdown = models.BooleanField(default=False)
    is_sticky = models.BooleanField(default=False)
    open_in_new_tab = models.BooleanField(default=False)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, default='TOP')
    visible_to_roles = models.ManyToManyField(Group, blank=True)

    class Meta:
        ordering = ['position', 'order']
        verbose_name = "Navbar Item"
        verbose_name_plural = "Navbar Items"

    def __str__(self):
        return self.title
    
    

    @property
    def has_children(self):
        return self.children.exists()
