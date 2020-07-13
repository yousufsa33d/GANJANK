from django.contrib import admin
from home.models import Contact,HomepageDate, MainArticle, DoYouKnowItem, TodayItem, TodayPictureArticle

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'timeStamp')
    list_filter = ['timeStamp', 'email']
admin.site.register(Contact, ContactAdmin)

class ChoiceInline1(admin.TabularInline):
    model = MainArticle
    extra = 0

class ChoiceInline2(admin.TabularInline):
    model = DoYouKnowItem
    extra = 0

class ChoiceInline3(admin.TabularInline):
    model = TodayItem
    extra = 0

class ChoiceInline4(admin.TabularInline):
    model = TodayPictureArticle
    extra = 0

class HomepageDateAdmin(admin.ModelAdmin):
    list_display = ['date']
    list_filter = ['date']
    search_fields = ['date']
    inlines = [ChoiceInline1, ChoiceInline2, ChoiceInline3, ChoiceInline4]
admin.site.register(HomepageDate, HomepageDateAdmin)