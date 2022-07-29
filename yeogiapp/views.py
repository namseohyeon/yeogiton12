from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm
from django.core.paginator import Paginator
from django.db.models import Count

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
            unfinished = form.save(commit=False)
            unfinished.user = request.user
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

def postlike(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=post_id)
        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)
            usercount = post.like_users.all().count()
            post.likeNum = usercount
            post.save()
        else:
            post.like_users.add(request.user)
            usercount = post.like_users.all().count()
            post.likeNum = usercount
            post.save()
        return redirect('postdetail', post_id)
    return redirect('login')

def commentcreate(request, post_id):
    filled_form = CommentModelForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.user = request.user
        finished_form.save()
    return redirect('postdetail', post_id)

def commentdelete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Post, pk=comment.post.id)
    comment.delete()
    return redirect('postdetail', post.id)

def Login(request):
    return render(request,'Login.html')