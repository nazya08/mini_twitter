from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Comment, Guest
from posts.forms import PostForm, CommentForm


def post_list(request, username=None):
    # username = request.GET.get('username')
    if username:
        posts = Post.objects.filter(user__username=username)
    else:
        posts = Post.objects.all()
    context = {'posts': posts, 'title': 'List of posts'}
    return render(request, 'posts/all_about_posts.html', context)


def comment_list(request):
    comments = Comment.objects.all()
    context = {'comments': comments, 'title': 'List of comments'}
    return render(request, 'posts/all_about_comments.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)

    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'posts/post_detail.html', context)


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'posts/create_comment.html', {'form': form})
