"""ganjank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article import views


urlpatterns = [
    path('', views.articleHome, name="articleHome"),
    path('getfeedback', views.getfeedback, name="getfeedback"),
    path('article_edit', views.articleEdit, name="ArticleEdit"),
    path('article_post', views.articlePost, name="ArticlePost"),
    path('modal_article', views.modalArticle, name="ArticlePost"),
    path('<str:slug>', views.article, name="articleShow")
]
