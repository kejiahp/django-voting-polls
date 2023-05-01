from django.urls import path
from contestants.views import male_contestants, female_contestants, purchaseissues, purchaseissues_valid, processcomplete, cont_finder, cont_finder_female
from contestants.new_logic.views import NewPageantryRegistrationView, v2_registration_sucessful, agree_to_terms, awards_terms, pagaentry_terms

urlpatterns = [
    path('male/', male_contestants, name="male-cont"),
    path('female/', female_contestants, name='female_cont'),
    path('purchaseissues/', purchaseissues, name='purchase-issues'),
    path("purchaseissues-valid/", purchaseissues_valid,
         name="purchaseissues-valid"),
    path("processcomplete/", processcomplete, name='processcomplete'),
    path('search-contestant/', cont_finder, name='search-contest'),
    path('search-contestant-female/', cont_finder_female,
         name='search-contest-female'),

    # NEW ROUTES
    path("v2-apply-validator/", NewPageantryRegistrationView.as_view(),
         name="v2_apply_validator"),
    path("v2-registration-success", v2_registration_sucessful,
         name="v2_registration_success"),
    path("agree-terms-and-conditions", agree_to_terms,
         name="agree_terms_and_conditions"),
    path("awards-terms-and-conditions", awards_terms,
         name="awards_terms_and_conditions"),
    path("pagaentry-terms-and-conditions", pagaentry_terms,
         name="pagaentry_terms_and_conditions")
]
