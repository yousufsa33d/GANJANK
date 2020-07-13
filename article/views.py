from django.shortcuts import render, HttpResponse, redirect, Http404
from article.models import Article, ArticleHeading, ArticleFeedback, ArticleEdit, ArticlePost
from django.contrib import messages
from article.templatetags import extras
import json

# Create your views here.
def articleHome(request):
    if request.GET.get('sort'):
        sort = request.GET['sort']
        articles = Article.objects.filter(title__startswith=sort, publish=True)
        return render(request, 'article/sort.html', {'sort':sort, 'articles': articles})
    else:
        raise Http404('not found')
def article(request, slug):
    article = Article.objects.filter(slug=slug, publish=True).first()
    if article:
        headings = ArticleHeading.objects.filter(article=article, parent=None)
        subheadings = ArticleHeading.objects.filter(article=article).exclude(parent=None)
        subheadingDict = {}
        for subheading in subheadings:
            if subheading.parent.id not in subheadingDict.keys():
                subheadingDict[subheading.parent.id] = [subheading]
            else:
                subheadingDict[subheading.parent.id].append(subheading)
        article.views += 1
        article.save()
        context = {'article':article, 'headings':headings, 'subheadings': subheadingDict}
        if request.GET.get('action') == 'edit':
            return render(request, 'article/articleEdit.html', context)
        else:
            return render(request, 'article/article.html', context)
    else:
        raise Http404('Article not found')

def articleEdit(request):
    try:
        changes = request.POST['changes']
        old = request.POST['old']
        articleId = request.POST['articleId']
        user = request.user
        article = Article.objects.get(Id=articleId, publish=True)
        articleEdit = ArticleEdit(article=article, user=user, old=old, changes=changes)
        articleEdit.save()
        messages.success(request, "edited")
        return HttpResponse('Done')
    except:
        return HttpResponse('something went wrong')

def getfeedback(request):
    if request.method == 'POST':
        feedback = request.POST['feedback']
        articleId = request.POST['articleId']
        article = Article.objects.get(Id=articleId, publish=True)
        articleFeedback = ArticleFeedback(feedback = feedback, article = article, user=request.user)
        articleFeedback.save()
        messages.success(request, 'فیڈ بیک شت۔')
        return redirect(f'/article/{article.slug}')
    else:
        return HttpResponse('404 - Not Found')

def articlePost(request):
    if request.method == 'POST':
        try:
            post = request.POST['post']
            user = request.user
            title = request.POST['title']
            articlePost = ArticlePost(title=title, user=user, post=post)
            articlePost.image_title1 = request.POST['image_title1']
            articlePost.image_title2 = request.POST['image_title2']
            articlePost.image_title3 = request.POST['image_title3']
            articlePost.image_title4 = request.POST['image_title4']
            if request.FILES.get('image1') != None:
                articlePost.image2 = request.FILES['image1']
            if request.FILES.get('image2') != None:
                articlePost.image2 = request.FILES['image2']
            if request.FILES.get('image3') != None:
                articlePost.image3 = request.FILES['image3']
            if request.FILES.get('image4') != None:
                articlePost.image4 = request.FILES['image4']
            articlePost.save()
            messages.success(request, 'article posted')
            return redirect("home")
        except:
            messages.error(request, 'somrthing went wrong try again')
            return redirect('article_post')  
    else:
        return render(request, 'article/articlePost.html')

def modalArticle(request):
    article = Article.objects.filter(slug=request.GET['article'], publish=True).first()
    if article:
        headings = ArticleHeading.objects.filter(article=article, parent=None)
        subheadings = ArticleHeading.objects.filter(article=article).exclude(parent=None)
        subheadingDict = {}
        for subheading in subheadings:
            if subheading.parent.id not in subheadingDict.keys():
                subheadingDict[subheading.parent.id] = [subheading]
            else:
                subheadingDict[subheading.parent.id].append(subheading)
        article.views += 1
        article.save()
        context = {'article':article, 'headings':headings, 'subheadings': subheadingDict}
        articleData = str(render(request, 'article/modalArticle.html', context).content.decode('utf-8'))
        data = json.dumps({'articleData': articleData, 'articleTitle': article.title})
        return HttpResponse(data)
    else:
        return HttpResponse("Article not found")