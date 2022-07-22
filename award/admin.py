from django.contrib import admin
from award.models import AwardsCategory,AwardsContestant,AwardVotePurchase

admin.site.register(AwardsContestant)
admin.site.register(AwardsCategory)
admin.site.register(AwardVotePurchase)