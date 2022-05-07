from django.urls import path
from contestants.views import male_contestants,female_contestants,apply,apply_submit,RegistrationView
from django.views.decorators.csrf import csrf_protect,csrf_exempt

urlpatterns = [
   path('male/',male_contestants,name="male-cont"),
   path('female/',female_contestants,name= 'female_cont'),
   path('apply/',apply,name="apply"),
   path('apply-sum/',apply_submit,name="apply-summary"),
   path('apply-validate/',RegistrationView.as_view(),name="apply-validate"),
]
