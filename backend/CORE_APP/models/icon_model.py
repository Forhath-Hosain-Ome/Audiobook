from django.db import models
class IconModel(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Name or identifier for the icon")
    image = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.name
