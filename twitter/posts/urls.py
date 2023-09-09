from django.urls import path

from .views import post_list, comment_list, post_detail, add_post, add_comment


urlpatterns = [
    path('all/', post_list, name="post_list"),
    path('user/<str:username>/', post_list, name="post_list_with_username"),
    path('<int:post_id>/', post_detail, name="post_detail"),
    path('comments/', comment_list, name="comment_list"),
    path('add-post', add_post, name="add_post"),
    path('add-comment', add_comment, name="add_comment")
]
