from atexit import register
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.conf import settings
from contestants.models import RegistrationPurchase
from django.conf import settings

def male_contestants(request):
    return render(request, "male_cont.html")

def female_contestants(request):
    return render(request, "female_cont.html")

def apply(request):
    return render(request, "apply.html")

def purchaseform(request):
    return render(request,"registration_form.html")

def purchaseform_valid(request):
    if request.method == "POST":
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        #ENSURING NO CONTESTANT IS REGISTERS USING ANOTHER CONTESTANTS EMAIL OR PHONENUMBER
        if not RegistrationPurchase.objects.filter(email=email,verified=True).exists():
            if not RegistrationPurchase.objects.filter(phonenumber=phonenumber,verified=True).exists():
                register_email = RegistrationPurchase.objects.create(email=email,phonenumber=phonenumber)
                register_email.save()
                print(register_email)
                context = {
                    "display":'block',
                    "register_email":register_email,
                    "paykey": settings.PAYSTACKPUBKEY,
                    "amount":5000
                }
                return render(request,"registration_form.html",context)
            messages.error(request,"A contestant already has this number")
            return render(request,"registration_form.html")
        messages.error(request,"A contestant already has this email")
        return render(request,"registration_form.html")

def verify_payment(request,ref):
    pass



class RegistrationView(View):
    def get(self,request):
        return render(request, "apply.html")

    def post(self, request):
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        context = {
            "fieldValues":request.POST
        }

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken. Try again")
            return render(request, "apply.html", context)
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already taken. Try again")
            return render(request, "apply.html", context)
        if password1 != password2:
            messages.error(request, "Confirm Password and Password do not match")
            return render(request, "apply.html", context)
        if len(password1) < 6:
            messages.error(request,"Password Lenght must be greater than 6")
            return render(request, "apply.html", context)
        if not username.islower():
            username = username.lower()
        #creating an object of the user model
        user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname)
        user.set_password(password1)
        user.is_active = True
        user.save()

        messages.success(request, "Account Successfully Created")
        return render(request, "apply.html")