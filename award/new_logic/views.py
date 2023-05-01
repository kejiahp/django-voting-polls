from django.views import View
from django.shortcuts import render, redirect
from award.new_logic.forms import NewAwardsRegistrationForm
from django.contrib import messages
from award.models import NewAwardsRegistration, AwardsCategory
from django.shortcuts import get_object_or_404


class NewAwardsRegistrationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "AwardsRegistrationPage.html")

    def post(self, request, *args, **kwargs):
        form = NewAwardsRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            if not NewAwardsRegistration.objects.filter(email=form.cleaned_data.get("email")).exists():
                award_category_instance = get_object_or_404(
                    AwardsCategory, name=form.cleaned_data.get("category"))
                form.cleaned_data.pop("category")

                award_contestant = NewAwardsRegistration.objects.create(
                    category=award_category_instance, **form.cleaned_data)
                award_contestant.save()

                return redirect('v2_registration_success')

            messages.error(
                request, "A contestant already as this email")
            return render(request, "AwardsRegistrationPage.html", {"form": form})

        messages.error(request, "All fields must be valid")
        return render(request, "AwardsRegistrationPage.html", {"form": form})


class AwardsCategoryDescription(View):
    def get(self, request):
        return render(request, "AwardsCategoryDescription.html")
