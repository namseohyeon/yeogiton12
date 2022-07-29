from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'spacePhoto']

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : "게시글 제목을 입력해주세요",
            'rows':20
        }

        self.fields['body'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : "게시글 본문을 입력해주세요",
            'rows':20
        }

        self.fields['spacePhoto'].widget.attrs = {
            'class' : 'form-control'
        }

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']  

    def __init__(self, *args, **kwargs):
        super(CommentModelForm, self).__init__(*args, **kwargs)
        
        self.fields['comment'].widget.attrs = {
            'class' : 'form-control',
            'placeholder' : "댓글을 입력해주세요",
            'rows': 5
        }
 