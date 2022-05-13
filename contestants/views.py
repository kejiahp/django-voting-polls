import email
from weakref import ref
from wsgiref.util import request_uri
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.conf import settings
from contestants.models import RegistrationPurchase
from django.conf import settings
from django.urls.exceptions import NoReverseMatch
from paystackapi.transaction import Transaction
from paystackapi.paystack import Paystack
from django.views.decorators.http import require_POST

def male_contestants(request):
    return render(request, "male_cont.html")

def female_contestants(request):
    return render(request, "female_cont.html")

def purchaseissues(request):
    return render(request, "form_purchased.html")

@require_POST
def purchaseissues_valid(request):
    ref = request.POST["refnumber"]
    payment = get_object_or_404(RegistrationPurchase, ref = ref)
    if payment.verified == True:
        messages.success(request,"Purchase was verified")
        return render(request,"form_purchased.html")
    messages.error(request, "Purchase was not verified")
    return render(request, "form_purchased.html")

def apply(request, ref):
    register_object = get_object_or_404(RegistrationPurchase ,ref = ref,verified=True,completed = False)
    email = register_object.email
    return render(request, "apply.html",{"email":email,"ref":ref})

def purchaseform(request):
    return render(request,"registration_form.html")

def proceed(request):
    try:
        return render(request, "proceedtopay.html")
    except NoReverseMatch as exc:
        return redirect('home')

def form_valid(request):
    if request.method == "POST":
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        #ENSURING NO CONTESTANT IS REGISTERS USING ANOTHER CONTESTANTS EMAIL OR PHONENUMBER
        try:
            if not RegistrationPurchase.objects.filter(email=email,verified=True).exists():
                if not RegistrationPurchase.objects.filter(phonenumber=phonenumber,verified=True).exists():
                    register_email = RegistrationPurchase.objects.create(email=email,phonenumber=phonenumber)
                    register_email.save()
                    context = {
                        "register_email":register_email,
                        "paykey": settings.PAYSTACKPUBKEY,
                        "amount":5000
                    }
                    return render(request,"proceedtopay.html",context)
                messages.error(request,"A contestant already has this number")
                return render(request,"registration_form.html")
            messages.error(request,"A contestant already has this email")
            return render(request,"registration_form.html")
        except:
           return redirect('home') 


class RegistrationView(View):
    def get(self,request):
        return render(request, "apply.html")

    def post(self, request):
        pass

def verify_trans(request, ref_num):
    paystack_secret_key = settings.PAYSTACK_SECRET_KEY
    paystack = Paystack(secret_key=paystack_secret_key)
    response = paystack.transaction.verify(reference=ref_num)
    amount = 500000
    reference_num = response['data']['reference']
    if response['data']['status'] == 'success' & response['data']['amount'] == amount:
        if RegistrationPurchase.objects.filter(ref = response['data']['reference']).exists():
            obj = RegistrationPurchase.objects.get(ref = response['data']['reference'])
            obj.verified = True
            messages.success(request, "Verification complete, You have successfully purchased the form.")
            return redirect(reverse("apply",kwargs={"ref":reference_num}))
    else:
        messages.error(request, "Verification Unsuccessful, Form not purchased")
        return render(request,"registration_form.html")

