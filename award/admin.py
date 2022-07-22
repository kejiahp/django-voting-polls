from django.contrib import admin
from award.models import AwardsCategory,AwardsContestant

admin.site.register(AwardsContestant)
admin.site.register(AwardsCategory)