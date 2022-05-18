from django.urls import path
from voters.views import home,about,vote_page,vote_flutter,vote_pg_valid,verify_vote

urlpatterns = [
    path('', home ,name="home"),
    path('about/',about,name="about"),
    path('vote/<int:id>',vote_page,name="vote"),
    path('vote/voting/<int:id>',vote_flutter,name="voting-pay"),
    path('voter-validate/',vote_pg_valid,name="vote-valid"),
    path('verify_vote/<str:ref>',verify_vote,name="verify-vote"),
]
