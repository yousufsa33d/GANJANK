from django.shortcuts import render, HttpResponse, redirect, Http404
from home.models import Contact, HomepageDate, MainArticle, DoYouKnowItem, TodayItem, TodayPictureArticle
from article.models import Article
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_auth
from django.contrib.auth import login as login_auth
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import re

# Create your views here.
def home(request):
    articles = Article.objects.filter(publish=True)
    no_of_articles = articles.count()
    try:
        today = date.today()
        homepageDate = HomepageDate.objects.get(date=today)
        mainArticle = MainArticle.objects.filter(homepageDate=homepageDate).first()
        doYouKnows = DoYouKnowItem.objects.filter(homepageDate=homepageDate)
        todayItems = TodayItem.objects.filter(homepageDate=homepageDate)
        todayPictureArticle = TodayPictureArticle.objects.filter(homepageDate=homepageDate).first()
        context = {'no_of_articles': no_of_articles,
                    'mainArticle': mainArticle.article,
                    'doYouKnows': doYouKnows,
                    'todayItems': todayItems,
                    'todayPictureArticle': todayPictureArticle.pictureArticle
        }
        return render(request, 'home/home.html', context)
    except:
        articleViews = []
        for article in articles:
            articleViews.append(article.views)
        articleViews.sort()
        articleViews.reverse()
        mainArticle = Article.objects.filter(views=articleViews[0]).first()
        # mainArticle = Article.objects.get(slug='gwadar')
        context = {'no_of_articles': no_of_articles,
                    'mainArticle': mainArticle
        }
        return render(request, 'home/home.html', context)
    # today = date.today()
    # invoice_for_today = Invoice.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        message = request.POST['message']
        if len(name)<2 or len(email)<2 or len(message)<5:
            messages.error(request, ' فارم ءَ شر پُر بکن۔ ')
        else:
            messages.success(request, ' منتوار: تئی مسج مارادست کپت۔ ')
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
    return render(request, 'home/contact.html')

#Sign Up API
def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['confirmpassword']

            if name == '':
                messages.error(request, "Enter a name")
                return redirect('signup')

            if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' ,email)) == None:
                messages.error(request, "enter a valid email address")
                return redirect('signup')

            if User.objects.filter(email=email).exists():
                messages.error(request, "email already exists")
                return redirect('signup')

            if len(username) > 100 or len(username) < 5:
                messages.error(request, "username must be greater than 4 charracter and less than 100 character")
                return redirect('signup')

            if username.find(' ') != -1:
                messages.error(request, "enter a valid username")
                return redirect('signup')

            if User.objects.filter(username=username).exists():
                messages.error(request, "username already exists")
                return redirect('signup')

            if len(password) <= 8:
                messages.error(request, "password must be greater than 8 character")
                return redirect('signup')

            
            if password != password2:
                messages.error(request, "password does not match")
                return redirect('signup')

            user = User.objects.create_user(username, email, password)
            user.first_name = name
            user.save()
            login_auth(request, user)
            messages.success(request, 'اکاوٰنٹ کامیبی گما بنت۔')
            return redirect('home')
        except:
            messages.error(request, 'something went wrong Try again')
            return redirect('signup')
    else:
        return render(request, 'home/signup.html')

def login(request):
    if request.method == 'POST':
        try:
            username_email = request.POST['username_email']
            password = request.POST['password']
            
            user = authenticate(request, username=username_email, password=password)
            if user is not None:
                login_auth(request, user)
                messages.success(request, 'successfully logged in')
                return redirect('home')
            else:
                user_email = User.objects.filter(email=username_email)
                if user_email.exists():
                    username = user_email[0]
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login_auth(request, user)
                        messages.success(request, 'successfully logged in')
                        return redirect('/login')
                messages.error(request, 'invalid login crediatianals')
                return redirect('/login')
        except:
            messages.error(request, 'Something went wrong try again')
            return redirect('/login')
    else:
       return render(request, 'home/login.html')

def logout(request):
    logout_auth(request)
    messages.success(request, 'logout successfully')
    return redirect('home')

def profile(request):
    try:
        user = User.objects.filter(username=request.user).first()
        context = {'user': user}
        return render(request, 'home/profile.html', context)
    except:
        return HttpResponse('404 - Not Found')

def search(request):
    try:
        query = request.GET['query']
        if len(query) < 5:
            context = {'noresult': True}
            return render(request, 'home/search.html', context)
        article = Article.objects.filter(searchtags__icontains=query, publish=True)
        if article.count() == 0:
            context = {'articles': article, 'noresult': True}
            return render(request, 'home/search.html', context)
        if article.count() == 1:
            return redirect(f'/article/{article[0].slug}')
        else:
            context = {'articles': article}
            return render(request, 'home/search.html', context)
    except:
        raise Http404('404 - not found')

@csrf_exempt
def checkemail(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            if User.objects.filter(email=email).exists():
                return HttpResponse('false')
            else:
                return HttpResponse('true')
        except:
            return HttpResponse('something went wrong')
    else:
        raise Http404('something went wrong!')
@csrf_exempt
def checkusername(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            if User.objects.filter(username=username).exists():
                return HttpResponse('false')
            else:
                return HttpResponse('true')
        except:
            return HttpResponse('something went wrong')
    else:
        raise Http404('something went wrong!')
