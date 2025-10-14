from django.db import models
from .base_model import BaseUIModel
from .icon_model import IconModel
class FooterModel(BaseUIModel):
    SECTION_CHOICES = [
        ('MAIN', 'Main Footer'),
        ('BOTTOM', 'Bottom Bar'),
    ]
    title = models.CharField(max_length=100, help_text="Title of the footer section, e.g., 'Company' or 'Support'")
    section_type = models.CharField(max_length=20, choices=SECTION_CHOICES, default='MAIN')
    content = models.TextField(blank=True, null=True, help_text="Optional text content, such as copyright notice or address")
    icon = models.ForeignKey(
        IconModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='footer_items'
    )
    url = models.CharField(max_length=255, blank=True, null=True)

    order = models.PositiveIntegerField(default=0)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        help_text="Parent section for grouped links"
    )
    open_in_new_tab = models.BooleanField(default=False)
    is_social_link = models.BooleanField(default=False)

    class Meta:
        ordering = ['section_type', 'order']
        verbose_name = "Footer Item"
        verbose_name_plural = "Footer Items"

    def __str__(self):
        return f"{self.title} ({self.section_type})"

    @property
    def has_children(self):
        return self.children.exists()
