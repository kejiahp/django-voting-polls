from django.urls import path
from award.views import award_categories, search_category, award_vote_page, award_vote_valid, award_vote_paystack, award
from award.new_logic.views import NewAwardsRegistrationView, AwardsCategoryDescription

urlpatterns = [
    path('', award, name='award-landing'),
    path('awardscategory/', award_categories, name="award-categories"),
    path('category-search/', search_category, name="category-search"),
    path('award-vote/<int:id>/', award_vote_page, name='award-vote'),
    path('award-vt-validdation/', award_vote_valid, name='award-valid'),
    path('award-voting/<str:id>', award_vote_paystack, name='award-voting'),

    # NEW VIEWS
    path("v2-award-validator/", NewAwardsRegistrationView.as_view(),
         name="v2_award_validator"),
    path("awards-category-description", AwardsCategoryDescription.as_view(),
         name="awards_category_description"),
]
