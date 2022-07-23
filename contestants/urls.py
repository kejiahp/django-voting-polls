from django.urls import path
from contestants.views import male_contestants,female_contestants,apply,RegistrationView,purchaseform,form_valid,verify_trans,purchaseissues,purchaseissues_valid,processcomplete,form_valid_post,jointhegroup,cont_finder,cont_finder_female

urlpatterns = [
   path('male/',male_contestants,name="male-cont"),
   path('female/',female_contestants,name= 'female_cont'),
   path('apply/<str:ref>/',apply,name="apply"),
   path('apply-validate/',RegistrationView.as_view(),name="apply-validate"),
   path('purchaseform/',purchaseform,name="buyform"),
   path('purchasevalid/',form_valid,name="purchase-valid"),
   path('verify_trans/<str:ref_num>/',verify_trans,name="verify_trans"),
   path('purchaseissues/',purchaseissues,name='purchase-issues'),
   path("purchaseissues-valid/",purchaseissues_valid,name="purchaseissues-valid"),
   path("processcomplete/",processcomplete,name='processcomplete'),
   path("valid-post/<str:id>",form_valid_post,name="valid_post"),
   path('jointhegroup/<str:ref>',jointhegroup,name="jointhegroup"),
   path('search-contestant/',cont_finder,name='search-contest'),
   path('search-contestant-female/',cont_finder_female,name='search-contest-female'),
]