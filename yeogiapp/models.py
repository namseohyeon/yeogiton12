from django.db import models

# Create your models here.
class Post(models.Model):
    #제목
    title = models.CharField(max_length=200)
    #본문
    body = models.TextField()
    #날짜
    date = models.DateTimeField(auto_now_add=True)
    #공간사진
    spacePhoto = models.ImageField(blank=True, null=True, upload_to='space_photo')
    #좋아요수
    likeNum = models.IntegerField(default=0)
    #공간 이름
    spaceName = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    #게시글
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    #댓글 내용
    comment = models.TextField()
    #날짜
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment