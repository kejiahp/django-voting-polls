from django.contrib import admin
from blog.models import Blog

# Register your models here.

@admin.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('title',)}
    search_fields = ['title']
    list_filter = ['author']