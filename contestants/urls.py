from django.urls import path
from contestants.views import male_contestants,female_contestants,apply,apply_submit

urlpatterns = [
   path('male/',male_contestants,name="male-cont"),
   path('female/',female_contestants,name= 'female_cont'),
   path('apply/',apply,name="apply"),
   path('apply-sum/',apply_submit,name="apply-summary"),
]
