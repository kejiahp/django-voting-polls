from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.conf import settings
from requests import request
from contestants.models import NewPageantRegistration
from django.conf import settings
from django.views.decorators.http import require_POST
from payments.models import NewVotingWebhookModel
from django.db.models import Q
from hashids import Hashids

hashid = Hashids(salt=settings.HASHID_SALT, min_length=8)


def male_contestants(request):
    male_cont = NewPageantRegistration.objects.filter(
        gender="male", is_evicted=False, is_confirmed=True).order_by("-number_of_votes")
    context = {
        "male_cont": male_cont
    }
    return render(request, "male_cont.html", context)


def female_contestants(request):
    female_cont = NewPageantRegistration.objects.filter(
        gender="female", is_evicted=False, is_confirmed=True).order_by("-number_of_votes")
    context = {
        "female_cont": female_cont
    }
    return render(request, "female_cont.html", context)


def purchaseissues(request):
    return render(request, "form_purchased.html")


def paychecker(pay, req=request):
    if pay.verified == True:
        messages.success(req, "Purchase was verified")
    else:
        messages.error(req, "Purchase was not verified")


def webhookPayments(pay, req=request):
    """ This is to validate payments made with the webhook api """
    if pay.verified == True:
        messages.success(
            req, f"Payment for {pay.type_of_vote}, status: {pay.payment_state}, verified: True")
    else:
        messages.error(
            req, f"Payment for {pay.type_of_vote}, status: {pay.payment_state}, verified: False")


@require_POST
def purchaseissues_valid(request):
    ref = request.POST["refnumber"]
    if NewVotingWebhookModel.objects.filter(ref=ref).exists():
        payment = NewVotingWebhookModel.objects.get(ref=ref)
        webhookPayments(payment, request)
        return redirect('purchase-issues')
    else:
        messages.error(request, "Transaction with reference " +
                       ref+" was not found in our system")
        return redirect('purchase-issues')


def processcomplete(request):
    return render(request, "processcomplete.html")


def cont_finder(request):
    if request.method == "POST":
        searchvalue = request.POST["cont_search"]
        searchvalue = searchvalue.strip()
        candidate = NewPageantRegistration.objects.filter(Q(firstname__icontains=searchvalue) | Q(
            lastname__icontains=searchvalue), is_confirmed=True, gender="male")
        if candidate:
            context = {
                "candidate": candidate
            }
            return render(request, "search_result.html", context)
        else:
            context = {
                "message": f"Sorry couldn't find results for search: {searchvalue}"}
            return render(request, "search_result.html", context)


def cont_finder_female(request):
    if request.method == "POST":
        searchvalue = request.POST["cont_search"]
        searchvalue = searchvalue.strip()
        candidate = NewPageantRegistration.objects.filter(Q(firstname__icontains=searchvalue) | Q(
            lastname__icontains=searchvalue), is_confirmed=True, gender="female")
        if candidate:
            context = {
                "candidate": candidate
            }
            return render(request, "search_result.html", context)
        else:
            context = {
                "message": f"Sorry couldn't find results for search: {searchvalue}"}
            return render(request, "search_result.html", context)
