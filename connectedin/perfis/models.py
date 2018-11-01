from django.db import models

class User(models.Model):
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    dt_birth = models.DateField()
