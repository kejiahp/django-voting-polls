from django.urls import path
from blog.views import bloglist,blogdetails

urlpatterns = [
    path('',bloglist,name="blog-posts"),
    path('blog-details/<int:id>',blogdetails,name="blog-details")
]
