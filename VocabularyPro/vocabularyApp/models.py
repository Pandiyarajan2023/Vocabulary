from django.db import models

# Create your models here.

class vocabulary(models.Model):
    Word = models.CharField(max_length=50)
    Meaning = models.CharField(max_length=30)
    Example = models.CharField(max_length=100)
    Name = models.CharField(max_length=25)