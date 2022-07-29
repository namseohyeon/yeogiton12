from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')
    #paginator = Paginator(posts, 5)
    #pagnum = request.GET.get('page')
    #posts = paginator.get_page(pagnum)

    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    #request method가 POST일 경우 : 입력값 저장
    if request.method == 'POST' or request.method=='FILES':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    #request method가 GET일 경우 : form 입력 html 띄우기
    else:
        form = PostModelForm()
    return render(request, 'post_form.html', {'form':form})

def postdelete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('home')

def postdetail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentModelForm()
    return render(request, 'post_detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

