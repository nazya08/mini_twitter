from django.db import models

from guests.models import Guest


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to="posts/covers", blank=True, null=True)
    user = models.ForeignKey(Guest, on_delete=models.CASCADE)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Post: {self.title}, by: {self.user}'


class Comment(models.Model):
    content = models.TextField(null=True, blank=True)
    user = models.ForeignKey(Guest, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment: {self.content}, by: {self.user}'
