from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    Id = models.AutoField(primary_key = True)
    views = models.IntegerField(default=0)
    publish = models.BooleanField()
    searchtags = models.CharField(max_length=1000)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField()
    image_title =  models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='article/images', null=True, blank=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

class ArticleHeading(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    image_title =  models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='article/images', null=True, blank=True)

    def __str__(self):
        return self.title + ' ,' + self.article.title 

class ArticleFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    feedback = models.TextField()
    timeStamp = models.DateTimeField(default=now)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.title + ' by ' + self.user.username


class ArticleEdit(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(default=now)
    old = models.TextField()
    changes = models.TextField()
    def __str__(self):
        return self.article.title + ' by ' + self.user.username


class ArticlePost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    post = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(default=now)
    image1 = models.ImageField(upload_to = "images/", null=True, blank=True) 
    image_title1 = models.CharField(max_length=200, null=True, blank=True)
    image2 = models.ImageField(upload_to = "images/", null=True, blank=True) 
    image_title2 = models.CharField(max_length=200, null=True, blank=True)
    image3 = models.ImageField(upload_to = "images/", null=True, blank=True) 
    image_title3 = models.CharField(max_length=200, null=True, blank=True)
    image4 = models.ImageField(upload_to = "images/", null=True, blank=True) 
    image_title4 = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title + ' by ' + self.user.username
    
