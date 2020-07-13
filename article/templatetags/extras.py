from django import template
from article.models import Article

register = template.Library()

@register.filter(name='get_val')
def get_val(dict, key):
    return dict.get(key)

@register.filter(name='add_article_link')
def add_article_link(content, contentArticle):
    articles = Article.objects.filter(publish=True).exclude(Id=contentArticle.Id)
    articleSpaceTitles = {}
    articleSpaceSlugs = {}
    articleTitles = []
    articleSlugs = []
    changesSlugs = []
    changesTitles = []
    keys = []
    for article in articles:
        spaces = 0
        for char in article.title:
            if char == ' ':
                spaces += 1
        if spaces not in articleSpaceTitles.keys():
            articleSpaceTitles[spaces] = [article.title]
            articleSpaceSlugs[spaces] = [article.slug]
        else:
            articleSpaceTitles[spaces].append(article.title)
            articleSpaceSlugs[spaces].append(article.slug)
    for key in articleSpaceTitles.keys():
        keys.append(key)
    keys.sort()
    keys.reverse()        
    for key in keys:
        for (title, slug) in zip(articleSpaceTitles[key], articleSpaceSlugs[key]):
            if content.find(title) != -1:
                changesSlugs.append(slug)
                changesTitles.append(title)
                content = content.replace(title, slug)
    for (title, slug) in zip(changesTitles, changesSlugs):
        change = f'<a type="button" data-toggle="modal" data-target="#articleModal" class="modal-link" data-article="{slug}">{title}</a>'
        content = content.replace(slug, change)
    return content

@register.filter(name='add_link')
def add_link(content, contentArticle):
    articles = Article.objects.filter(publish=True).exclude(Id=contentArticle.Id)
    articleSpaceTitles = {}
    articleSpaceSlugs = {}
    articleTitles = []
    articleSlugs = []
    changesSlugs = []
    changesTitles = []
    keys = []
    for article in articles:
        spaces = 0
        for char in article.title:
            if char == ' ':
                spaces += 1
        if spaces not in articleSpaceTitles.keys():
            articleSpaceTitles[spaces] = [article.title]
            articleSpaceSlugs[spaces] = [article.slug]
        else:
            articleSpaceTitles[spaces].append(article.title)
            articleSpaceSlugs[spaces].append(article.slug)
    for key in articleSpaceTitles.keys():
        keys.append(key)
    keys.sort()
    keys.reverse()     
    for key in keys:
        for (title, slug) in zip(articleSpaceTitles[key], articleSpaceSlugs[key]):
            if content.find(title) != -1:
                changesSlugs.append(slug)
                changesTitles.append(title)
                content = content.replace(title, slug)
    for (title, slug) in zip(changesTitles, changesSlugs):
        change = f'<a href="/article/{slug}">{title}</a>'
        content = content.replace(slug, change)
    return content