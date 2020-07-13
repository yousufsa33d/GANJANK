from django.db import models
from django.utils.timezone import now
from article.models import Article
# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    message = models.TextField()
    timeStamp = models.DateTimeField(default=now)
    def __str__(self):
        return 'Message from '+ self.name
    
class HomepageDate(models.Model):
    sno = models.AutoField(primary_key = True)
    date = models.DateField()
    def __str__(self):
        return str(self.date)

class MainArticle(models.Model):
    sno = models.AutoField(primary_key = True)
    homepageDate = models.ForeignKey(HomepageDate, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return self.article.title

class DoYouKnowItem(models.Model):
    sno = models.AutoField(primary_key = True)
    homepageDate = models.ForeignKey(HomepageDate, on_delete=models.CASCADE)
    doYouKnowItem = models.CharField(max_length=1000)
    def __str__(self):
        return self.doYouKnowItem[:10]

class TodayItem(models.Model):
    sno = models.AutoField(primary_key = True)
    homepageDate = models.ForeignKey(HomepageDate, on_delete=models.CASCADE)
    todayItem = models.CharField(max_length=1000)
    def __str__(self):
        return self.todayItem[:10]

class TodayPictureArticle(models.Model):
    sno = models.AutoField(primary_key = True)
    homepageDate = models.ForeignKey(HomepageDate, on_delete=models.CASCADE)
    pictureArticle = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return self.pictureArticle.title
