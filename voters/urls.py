from django.urls import path
from voters.views import home,about,male_contestants,female_contestants

urlpatterns = [
    path('', home ,name="home"),
    path('about/',about,name="about"),
    path('contestantsmale/',male_contestants,name="male-cont"),
    path('contestantsfemale/',female_contestants,name= 'female_cont'),
]
