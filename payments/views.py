import hashlib
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import urllib
from award.models import AwardsContestant
from . models import AwardVotingWebhookModel, WebhookTestModel
from django.shortcuts import get_object_or_404, render
import hmac
import os

secret1 = os.environ.get('KEJIAHSSECRET') or ""

secret = bytes(secret1, 'utf-8')


def payment_home(request):
    return render(request, "paywebhooktest1.html")


@csrf_exempt
def payment_test(request, pk=None):
    response = json.loads(request.body)
    if response.get('event') == 'charge.success':
        vote = WebhookTestModel(ref=response['data']['reference'])
        vote.save()
    return HttpResponse(status=200)

    # paybytes = urllib.parse.urlencode(request.body).encode('utf8')
    # sign = hmac.new(secret, paybytes, hashlib.sha512).hexdigest()

    # if sign == request.headers["x-paystack-signature"]:
    #     response = json.loads(request.body)
    #     if response.get('event') == 'charge.success':
    #         vote = WebhookTestModel(ref=response['data']['reference'])
    #         vote.save()
    # with open("./webhookData.txt", 'w') as handler:
    #     handler.write(request.body)

    # return HttpResponse(status=200)


@csrf_exempt
def payment_webhook(request, pk=None):
    response = json.loads(request.body)

    if response.get('event') == 'charge.success':
        reference_num = response['data']['reference']
        voter = get_object_or_404(AwardVotingWebhookModel, ref=reference_num)
        voter_paid = voter.total_price
        voter_paid = int(float(voter_paid))*100

        if response['data']['status'] == 'success' and response['data']['amount'] == voter_paid:
            voter.payment_state = "success"
            voter.verified = True
            voter.order_paid = True
            voter.save()
            voters_votes_no = voter.number_of_votes
            cont_voted = get_object_or_404(
                AwardsContestant, id=voter.contestant_id.id)
            current_votes = cont_voted.number_of_votes
            new_votes = current_votes + voters_votes_no
            cont_voted.number_of_votes = new_votes
            cont_voted.save()

        elif response['data']['status'] == 'abandoned' or response['data']['amount'] != voter_paid:
            voter.payment_state = "failed"
            voter.verified = False
            voter.order_paid = False
            voter.save()

    return HttpResponse(status=200)
