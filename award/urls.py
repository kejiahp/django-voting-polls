from django.urls import path
from award.views import award_categories,search_category,award_vote_page,award_vote_valid,award_vote_paystack,verify_vote
urlpatterns = [
    path('awardscategory/',award_categories,name="award-categories"),
    path('category-search/',search_category,name="category-search"),
    path('award-vote/<int:id>/',award_vote_page,name='award-vote'),
    path('award-vt-validdation/',award_vote_valid,name='award-valid'),
    path('award-voting/<str:id>',award_vote_paystack,name='award-voting'),
    path('award-vote-verify/<str:ref>/',verify_vote,name='award-vote-verify'),
]