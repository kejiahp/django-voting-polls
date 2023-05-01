from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from contestants.models import NewPageantRegistration
from payments.models import NewVotingWebhookModel
from voters.models import NewsLetterSubscriber
from django.views.decorators.http import require_POST
from django.conf import settings
from hashids import Hashids

hashid = Hashids(salt=settings.HASHID_SALT, min_length=8)

amt_per_voter = "50"


def home(request):
    return render(request, "home_temp.html")


def about(request):
    return render(request, "about.html")


def sponsors_partners(request):
    return render(request, "PartnersSponsors.html")


def vote_page(request, id):
    contestant = get_object_or_404(NewPageantRegistration, id=id)
    return render(request, "vote.html", {"cont": contestant, "amt": amt_per_voter})


@require_POST
def vote_pg_valid(request):
    email = request.POST["email"]
    number_of_votes = request.POST["numvotes"]
    amount = request.POST["amount"]
    cont_id = request.POST["cont_id"]
    if email != "" and number_of_votes != "" and amount != "" and cont_id != "":
        if amount == amt_per_voter:
            cont = NewPageantRegistration.objects.get(id=cont_id)
            voter = NewVotingWebhookModel(
                email=email, number_of_votes=number_of_votes, contestant_id=cont.id, amount=amount, type_of_vote="pageant-vote")
            voter.save()
            vid = voter.id
            # encoding the id of the VotePurchase
            vid = hashid.encode(vid)
            return redirect(reverse("voting-pay", args=(vid,)))
        messages.error(request, "Invalid Amount")
        return redirect(reverse("vote", args=(cont_id,)))
    messages.error(request, "All fields must be filled")
    return redirect(reverse("vote", args=(cont_id,)))


def vote_flutter(request, id):
    try:
        id = hashid.decode(id)
        id = id[0]
    except:
        raise Http404
    voter_details = get_object_or_404(NewVotingWebhookModel, id=id)
    contestant_details = get_object_or_404(
        NewPageantRegistration, id=voter_details.contestant_id)
    return render(request, "voting.html", {"voter_details": voter_details, "paykey": settings.PAYSTACKPUBKEY, "contestant_details": contestant_details})


@require_POST
def newsletter(request):
    email = request.POST["email"]
    if email:
        sub = NewsLetterSubscriber(email=email)
        sub.save()
        messages.success(
            request, "Thanks for subscribing we will keep you posted for updates")
        return redirect("processcomplete")
    return redirect('home')
