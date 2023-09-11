from django import forms
from django.core.exceptions import ValidationError

from posts.models import Post, Comment


def validate_title(value):
    if value[0].isdigit():
        raise forms.ValidationError("Post's title should not start with number")


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validate_title])

    class Meta:
        model = Post
        fields = ['title', 'content', 'cover_image', 'user']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].empty_label = "User is not chosen"
        self.fields['post'].empty_label = "Post is not chosen"

    class Meta:
        model = Comment
        fields = ['content', 'user', 'post']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'post': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) > 50:
            raise ValidationError('Length must be less than 50')

        return content
