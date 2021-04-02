from django.db import models

# Create your models here.

class BookDetails(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    area_related = models.CharField(max_length=50)

