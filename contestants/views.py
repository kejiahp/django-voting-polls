from multiprocessing import context
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.conf import settings
from contestants.models import RegistrationPurchase,RegisterContestant
from django.conf import settings
from django.urls.exceptions import NoReverseMatch
from paystackapi.transaction import Transaction
from paystackapi.paystack import Paystack
from django.views.decorators.http import require_POST

def male_contestants(request):
    male_cont = RegisterContestant.objects.filter(gender="Male")
    context={
        "male_cont":male_cont
    }
    return render(request, "male_cont.html",context)

def female_contestants(request):
    female_cont = RegisterContestant.objects.filter(gender="Female")
    context = {
        "female_cont":female_cont
    }
    return render(request, "female_cont.html",context)

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
    get_object_or_404(RegistrationPurchase ,ref = ref,verified=True,completed = False)
    return render(request, "apply.html",{"ref":ref})

def purchaseform(request):
    return render(request,"registration_form.html")


def form_valid(request):
    if request.method == "POST":
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        try:
            if email != "" or phonenumber !="":
                register_email = RegistrationPurchase.objects.create(email=email,phonenumber=phonenumber)
                register_email.save()
                context = {
                    "register_email":register_email,
                    "paykey": settings.PAYSTACKPUBKEY,
                    "amount":5000
                }
                return render(request,"proceedtopay.html",context)
            else:
                messages.error(request,"All fields must be filled")
                return render(request, "registration_form.html")
        except:
           return redirect('home')


class RegistrationView(View):
    def get(self,request):
        return redirect("home")

    def post(self, request):
        refnum = request.POST["refnum"]
        firstname= request.POST["firstname"]
        lastname = request.POST["lastname"]
        instagram = request.POST["instagramhandle"]
        tellus = request.POST["tellus"]
        email = request.POST["email"]
        image1 = request.FILES["image1"]
        image2 = request.FILES["image2"]
        gender = request.POST["gender"]
        phonenumber = request.POST["phonenumber"]
        payment = get_object_or_404(RegistrationPurchase, ref = refnum,verified=True,completed = False)
        context = {
            "ref":refnum,
            "autofill":request.POST
        }
        if payment:
            if refnum!="" and firstname!="" and lastname!="" and instagram!="" and tellus!="" and email!="" and image1!="" and image2!="" and gender!="" and phonenumber!="":
                if not RegisterContestant.objects.filter(email=email).exists():
                    reg_contestant = RegisterContestant(refnum=refnum,firstname=firstname,lastname=lastname,instagram_handle=instagram,tell_us=tellus,email=email,image1=image1,image2=image2,gender=gender,phonenumber=phonenumber)
                    reg_contestant.save()
                    payment.completed=True
                    payment.save()
                    messages.success(request,'Contestant Sucessfully added')
                    return redirect('processcomplete')
                else:
                    messages.error(request,"A contestant already as this email")
                    return render(request, "apply.html", context)
            else:
                messages.error(request,"All fields must be filled")
                return render(request, "apply.html", context)
        else:
            return redirect('home')




def verify_trans(request, ref_num):
    paystack_secret_key = settings.PAYSTACK_SECRET_KEY
    paystack = Paystack(secret_key=paystack_secret_key)
    response = paystack.transaction.verify(reference=ref_num)
    amount = 500000
    reference_num = response['data']['reference']
    if response['data']['status'] == 'success' and response['data']['amount'] == amount:
        if RegistrationPurchase.objects.filter(ref = response['data']['reference']).exists():
            obj = RegistrationPurchase.objects.get(ref = response['data']['reference'])
            obj.verified = True
            obj.save()
            messages.success(request, "Verification complete, You have successfully purchased the form.")
            return redirect(reverse("apply",kwargs={"ref":reference_num}))
    else:
        messages.error(request, "Verification Unsuccessful, Form not purchased")
        return render(request,"registration_form.html")

def processcomplete(request):
    return render(request,"processcomplete.html")