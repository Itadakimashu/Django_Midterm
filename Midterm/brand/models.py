from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True,unique=True)

    def __str__(self):
        return self.name