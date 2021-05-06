from django.db import models

# Create your models here.
class Eksperymenty(models.Model):
    exp_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200, default='NONE')

    def __str__(self):
        return self.full_name
