from django.db import models

from accounts.models import User


class Parrot(models.Model):
    name = models.CharField(max_length=255)
    link = models.TextField()
    user = models.ForeignKey(User)
