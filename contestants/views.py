from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from django.conf import settings

def male_contestants(request):
    return render(request, "male_cont.html")

def female_contestants(request):
    return render(request, "female_cont.html")

def apply(request):
    return render(request, "apply.html")

def apply_submit(request):
    return render(request,"apply_submit.html")

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
            "fieldValues":request.POST,
            "paystackTestPubKey":settings.PAYSTACKPUBKEY,
            "amount":5000
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
        user.is_active = False
        user.save()
        messages.success(request, "Account Successfully Created")
        return render(request, "apply_submit.html", context)