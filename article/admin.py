from django.contrib import admin
from article.models import Article, ArticleHeading, ArticleFeedback, ArticleEdit, ArticlePost
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = ArticleHeading
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['views', 'searchtags', 'publish']}),
        ('Article Detail', {'fields': ['title', 'author', 'slug', 'content']}),
        ('Date Information', {'fields': ['timeStamp']}),
        ('Image', {'fields': ['image_title', 'image']}),
    ]
    list_display = ('title', 'author', 'timeStamp', 'views', 'publish')
    list_filter = ['timeStamp', 'publish', 'views', 'author']
    search_fields = ['title']
    inlines = [ChoiceInline]
admin.site.register(Article, ArticleAdmin)

class ArticleFeedbackAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'timeStamp')
    list_filter = ['timeStamp', 'article', 'user']
admin.site.register(ArticleFeedback, ArticleFeedbackAdmin)

class ArticleEditAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'timeStamp')
    list_filter = ['timeStamp', 'article', 'user']
admin.site.register(ArticleEdit, ArticleEditAdmin)

class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'timeStamp')
    list_filter = ['timeStamp', 'user']
admin.site.register(ArticlePost, ArticlePostAdmin)