from django.db import models


class Guest(models.Model):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User: {self.username}'
