from django.urls import path
from contestants.views import male_contestants,female_contestants,apply,RegistrationView,purchaseform,purchaseform_valid,verify_payment


urlpatterns = [
   path('male/',male_contestants,name="male-cont"),
   path('female/',female_contestants,name= 'female_cont'),
   path('apply/',apply,name="apply"),
   path('apply-validate/',RegistrationView.as_view(),name="apply-validate"),
   path('purchaseform/',purchaseform,name="buyform"),
   path('purchasevalid/',purchaseform_valid,name="purchase-valid"),
   path('verify-payment/<str:ref>/',verify_payment,name="verify-pay"),
]
