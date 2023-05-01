from django.shortcuts import render, redirect
from django.contrib import messages
from contestants.models import NewPageantRegistration
from django.views import View
from contestants.new_logic.forms import NewPageantRegistrationForm


# NEW VIEWS
def v2_registration_sucessful(request):
    return render(request, "RegistrationSuccessful.html")


def agree_to_terms(request):
    return render(request, "AgreeToTerms.html")


def awards_terms(request):
    return render(request, "AwardsTerms.html")


def pagaentry_terms(request):
    return render(request, "PagaentryTerms.html")


class NewPageantryRegistrationView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "apply.html")

    def post(self, request, *args, **kwargs):
        form = NewPageantRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data.get('is_in_agency') == "False":
                form.cleaned_data.pop("agency_name")
                form.cleaned_data.pop("agency_modeling_image")
                form.cleaned_data.pop("modeling_experience")

                if not NewPageantRegistration.objects.filter(email=form.cleaned_data.get('email')).exists():
                    pagaent_contestant = NewPageantRegistration.objects.create(
                        **form.cleaned_data)
                    pagaent_contestant.save()
                    return redirect('v2_registration_success')

                messages.error(
                    request, "A contestant already as this email")
                return render(request, "apply.html", {"form": form})
            else:
                if not NewPageantRegistration.objects.filter(email=form.cleaned_data.get('email')).exists():
                    pagaent_contestant = NewPageantRegistration.objects.create(
                        **form.cleaned_data)
                    pagaent_contestant.save()
                    return redirect('v2_registration_success')

                messages.error(
                    request, "A contestant already as this email")
                return render(request, "apply.html", {"form": form})

        messages.error(request, "All fields must be valid")
        return render(request, "apply.html", {"form": form})
