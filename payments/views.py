import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from award.models import NewAwardsRegistration
from contestants.models import NewPageantRegistration
from . models import NewVotingWebhookModel
from django.shortcuts import get_object_or_404, render


def payment_home(request):
    return render(request, "paywebhooktest1.html")


def vote_pending(request):
    return render(request, "vote_pending.html")


@csrf_exempt
def payment_webhook(request, pk=None):
    response = json.loads(request.body)

    if response.get('event') == 'charge.success':
        reference_num = response['data']['reference']
        voter = get_object_or_404(NewVotingWebhookModel, ref=reference_num)
        voter_paid = voter.total_price
        voter_paid = int(float(voter_paid))*100

        if response['data']['status'] == 'success' and response['data']['amount'] == voter_paid:
            voters_votes_no = voter.number_of_votes

            if voter.type_of_vote == "pageant-vote":
                voter.payment_state = "success"
                voter.verified = True
                voter.order_paid = True
                voter.save()
                cont_voted = get_object_or_404(
                    NewPageantRegistration, id=int(voter.contestant_id))
                current_votes = cont_voted.number_of_votes
                new_votes = current_votes + voters_votes_no
                cont_voted.number_of_votes = new_votes
                cont_voted.save()

            elif voter.type_of_vote == "awards-vote":
                voter.payment_state = "success"
                voter.verified = True
                voter.order_paid = True
                voter.save()
                cont_voted = get_object_or_404(
                    NewAwardsRegistration, id=int(voter.contestant_id))
                current_votes = cont_voted.number_of_votes
                new_votes = current_votes + voters_votes_no
                cont_voted.number_of_votes = new_votes
                cont_voted.save()

            else:
                voter.payment_state = "success"
                voter.verified = False
                voter.order_paid = True
                voter.save()

        elif response['data']['status'] == 'abandoned' or response['data']['amount'] != voter_paid:
            voter.payment_state = "failed"
            voter.verified = False
            voter.order_paid = False
            voter.save()

    return HttpResponse(status=200)
