from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField()
    email = models.EmailField()
    contact_no = models.CharField()
    bio = models.TextField()
