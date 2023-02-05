from django.conf import settings
from django.db import models


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(unique=True, max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
