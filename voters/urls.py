from django.urls import path
from voters.views import home,about,vote_page,vote_flutter

urlpatterns = [
    path('', home ,name="home"),
    path('about/',about,name="about"),
    path('vote/',vote_page,name="vote"),
    path('vote/voting/',vote_flutter,name="voting-pay")
]
