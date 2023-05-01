from django.contrib import admin
from voters.models import NewsLetterSubscriber


class NewsLetterSubscriberAdmin(admin.ModelAdmin):
    search_fields = ['email']


admin.site.register(NewsLetterSubscriber, NewsLetterSubscriberAdmin)
