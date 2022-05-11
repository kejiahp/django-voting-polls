from django.urls import path
from contestants.views import male_contestants,female_contestants,apply,RegistrationView,purchaseform,form_valid,verify_trans,proceed


urlpatterns = [
   path('male/',male_contestants,name="male-cont"),
   path('female/',female_contestants,name= 'female_cont'),
   path('apply/',apply,name="apply"),
   path('apply-validate/',RegistrationView.as_view(),name="apply-validate"),
   path('purchaseform/',purchaseform,name="buyform"),
   path('purchasevalid/',form_valid,name="purchase-valid"),
   path('purchaseform/proceed/',proceed,name="proceed"),
   path('verify_trans/<str:ref_num>/',verify_trans,name="verify_trans"),
]
# verify_trans/wHGyqqwsStWPib49j9PTFluWekGvp5LIh-yQvG2agI_RGKXCe1pCdJNazjcuz9jSKJU