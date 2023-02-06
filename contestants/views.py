from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.conf import settings
from requests import request
from contestants.models import RegistrationPurchase, RegisterContestant
from award.models import AwardVotePurchase
from django.conf import settings
from paystackapi.paystack import Paystack
from django.views.decorators.http import require_POST
from payments.models import AwardVotingWebhookModel
from voters.models import VotePurchase
from django.db.models import Q
from voters.models import VotePurchase
from hashids import Hashids

hashid = Hashids(salt=settings.HASHID_SALT, min_length=8)


def male_contestants(request):
    male_cont = RegisterContestant.objects.filter(
        gender="Male", is_evicted=False, is_confirmed=True).order_by("-number_of_votes")
    context = {
        "male_cont": male_cont
    }
    return render(request, "male_cont.html", context)


def female_contestants(request):
    female_cont = RegisterContestant.objects.filter(
        gender="Female", is_evicted=False, is_confirmed=True).order_by("-number_of_votes")
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
            req, f"Payment for {pay.type_of_vote} is {pay.payment_state}")
    else:
        messages.error(
            req, f"Payment for {pay.type_of_vote} is {pay.payment_state}")


@require_POST
def purchaseissues_valid(request):
    ref = request.POST["refnumber"]
    if RegistrationPurchase.objects.filter(ref=ref).exists():
        payment = RegistrationPurchase.objects.get(ref=ref)
        paychecker(payment, request)
        return redirect('purchase-issues')
    elif VotePurchase.objects.filter(ref=ref).exists():
        payment = VotePurchase.objects.get(ref=ref)
        paychecker(payment, request)
        return redirect('purchase-issues')
    elif AwardVotePurchase.objects.filter(ref=ref).exists():
        payment = AwardVotePurchase.objects.get(ref=ref)
        paychecker(payment, request)
        return redirect('purchase-issues')
    elif AwardVotingWebhookModel.objects.filter(ref=ref).exists():
        payment = AwardVotingWebhookModel.objects.get(ref=ref)
        webhookPayments(payment, request)
        return redirect('purchase-issues')
    else:
        messages.error(request, "Transaction with reference " +
                       ref+" was not found in our system")
        return redirect('purchase-issues')


def apply(request, ref):
    get_object_or_404(RegistrationPurchase, ref=ref,
                      verified=True, completed=False)
    return render(request, "apply.html", {"ref": ref})


def purchaseform(request):
    return render(request, "registration_form.html")


def form_valid(request):
    if request.method == "POST":
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        try:
            if email != "" or phonenumber != "":
                register_email = RegistrationPurchase.objects.create(
                    email=email, phonenumber=phonenumber)
                register_email.save()
                object_id = hashid.encode(register_email.id)

                return redirect(reverse("valid_post", args=(object_id,)))
            else:
                messages.error(request, "All fields must be filled")
                return render(request, "registration_form.html")
        except:
            return redirect('home')


def form_valid_post(request, id):
    try:
        id = hashid.decode(id)
        id = id[0]
    except:
        raise Http404
    register_email = get_object_or_404(
        RegistrationPurchase, id=id, verified=False, completed=False)
    context = {
        "register_email": register_email,
        "paykey": settings.PAYSTACKPUBKEY,
        "amount": 5000
    }
    return render(request, "proceedtopay.html", context)


class RegistrationView(View):
    def get(self):
        return redirect("home")

    def post(self, request):
        refnum = request.POST["refnum"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        instagram = request.POST["instagramhandle"]
        tellus = request.POST["tellus"]
        email = request.POST["email"]
        image1 = request.FILES["image1"]
        image2 = request.FILES["image2"]
        gender = request.POST["gender"]
        phonenumber = request.POST["phonenumber"]
        payment = get_object_or_404(
            RegistrationPurchase, ref=refnum, verified=True, completed=False)
        context = {
            "ref": refnum,
            "autofill": request.POST
        }
        if payment:
            if refnum != "" and firstname != "" and lastname != "" and instagram != "" and tellus != "" and email != "" and image1 != "" and image2 != "" and gender != "" and phonenumber != "":
                if not RegisterContestant.objects.filter(email=email).exists():
                    reg_contestant = RegisterContestant(refnum=refnum, firstname=firstname, lastname=lastname, instagram_handle=instagram,
                                                        tell_us=tellus, email=email, image1=image1, image2=image2, gender=gender, phonenumber=phonenumber)
                    reg_contestant.save()
                    payment.completed = True
                    payment.save()
                    messages.success(request, 'Contestant Sucessfully added!')
                    return redirect(reverse('jointhegroup', args=(refnum,)))
                else:
                    messages.error(
                        request, "A contestant already as this email")
                    return render(request, "apply.html", context)
            else:
                messages.error(request, "All fields must be filled")
                return render(request, "apply.html", context)
        else:
            return redirect('home')


def verify_trans(request, ref_num):
    paystack_secret_key = settings.PAYSTACK_SECRET_KEY
    paystack = Paystack(secret_key=paystack_secret_key)
    response = paystack.transaction.verify(reference=ref_num)
    amount = 500000
    reference_num = response['data']['reference']
    if response["status"] == True and response["message"] == 'Verification successful' and response['data']['status'] == 'success' and response['data']['amount'] == amount:
        if RegistrationPurchase.objects.filter(ref=response['data']['reference']).exists():
            obj = RegistrationPurchase.objects.get(
                ref=response['data']['reference'])
            obj.verified = True
            obj.save()
            messages.success(
                request, "Verification complete, You have successfully purchased the form.")
            return redirect(reverse("apply", args=(reference_num,)))
    else:
        messages.error(
            request, "Verification Unsuccessful, Form not purchased")
        return render(request, "registration_form.html")


def processcomplete(request):
    return render(request, "processcomplete.html")


def jointhegroup(request, ref):
    if RegistrationPurchase.objects.filter(ref=ref, verified=True, completed=True).exists() and RegisterContestant.objects.filter(refnum=ref, is_evicted=False, is_confirmed=False).exists():
        return render(request, "jointhegroup.html")
    else:
        messages.error(
            "Sorry, you are not eligible to join the group. Please contact Customer Care.(Link in footer of the page)")
        return redirect('processcomplete')


def cont_finder(request):
    if request.method == "POST":
        searchvalue = request.POST["cont_search"]
        searchvalue = searchvalue.strip()
        candidate = RegisterContestant.objects.filter(Q(firstname__icontains=searchvalue) | Q(
            lastname__icontains=searchvalue), is_confirmed=True, gender="Male")
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
        candidate = RegisterContestant.objects.filter(Q(firstname__icontains=searchvalue) | Q(
            lastname__icontains=searchvalue), is_confirmed=True, gender="Female")
        if candidate:
            context = {
                "candidate": candidate
            }
            return render(request, "search_result.html", context)
        else:
            context = {
                "message": f"Sorry couldn't find results for search: {searchvalue}"}
            return render(request, "search_result.html", context)
