from django.conf import settings
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from award.models import AwardsCategory, NewAwardsRegistration
from django.views.decorators.http import require_POST
from django.contrib import messages
from hashids import Hashids

from payments.models import NewVotingWebhookModel

hashid = Hashids(salt=settings.HASHID_SALT, min_length=8)


def award(request):
    return render(request, 'award.html')


def award_categories(request):
    categories = AwardsCategory.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'award_category.html', context)


def search_category(request):
    if request.method == 'POST':
        search_result = request.POST["category-search"]
        categories = AwardsCategory.objects.filter(
            name__icontains=search_result)

        if categories:
            context = {
                "categories": categories
            }
            return render(request, "category_search.html", context)
        else:
            context = {
                "message": f"Sorry couldn't find results for search: {search_result}"}
            return render(request, "category_search.html", context)


# Validation Process for the Awards Voting
amt_per_voter = "50"


def award_vote_page(request, id):
    contestant = get_object_or_404(NewAwardsRegistration, id=id)
    return render(request, "award_vote.html", {"cont": contestant, "amt": amt_per_voter})


@require_POST
def award_vote_valid(request):
    email = request.POST["email"]
    number_of_votes = request.POST["numvotes"]
    amount = request.POST["amount"]
    cont_id = request.POST["cont_id"]
    if email != "" and number_of_votes != "" and amount != "" and cont_id != "":
        if amount == amt_per_voter:
            cont = NewAwardsRegistration.objects.get(id=cont_id)
            voter = NewVotingWebhookModel(
                email=email, number_of_votes=number_of_votes, contestant_id=cont.id, amount=amount, type_of_vote="awards-vote")
            voter.save()
            vid = voter.id
            vid = hashid.encode(vid)
            return redirect(reverse("award-voting", args=(vid,)))
        messages.error(request, "Invalid Amount")
        return redirect(reverse("award-vote", args=(cont_id,)))
    messages.error(request, "All fields must be filled")
    return redirect(reverse("award-vote", args=(cont_id,)))


def award_vote_paystack(request, id):
    try:
        id = hashid.decode(id)
        id = id[0]
    except:
        raise Http404
    voter_details = get_object_or_404(NewVotingWebhookModel, id=id)
    contestant_details = get_object_or_404(
        NewAwardsRegistration, id=voter_details.contestant_id)
    return render(request, "award_voting.html", {"voter_details": voter_details, "paykey": settings.PAYSTACKPUBKEY, "contestant_details": contestant_details})
