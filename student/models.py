from django.db import models

# Create your models here.
class StudentsDetails(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=5)
    department = models.CharField(max_length=40)
    