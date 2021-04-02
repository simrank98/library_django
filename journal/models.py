from django.db import models

# Create your models here.

class JournalDetails(models.Model):
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    year_of_publish = models.DateField()
