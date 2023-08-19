from django.db import models

# Create your models here.

class movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return self.name