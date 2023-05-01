from django.urls import path
from voters.views import home, about, vote_page, vote_flutter, vote_pg_valid, newsletter, sponsors_partners

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('vote/<int:id>', vote_page, name="vote"),
    path('vote/voting/<str:id>', vote_flutter, name="voting-pay"),
    path('voter-validate/', vote_pg_valid, name="vote-valid"),
    path('newsletter/', newsletter, name="newsletter"),
    path('sponsors-and-partners/', sponsors_partners,
         name="sponsors_and_partners")
]
