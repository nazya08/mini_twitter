from django.contrib import admin
from guests.models import Guest
from posts.models import Post, Comment


admin.site.register(Guest)
admin.site.register(Post)
admin.site.register(Comment)
