from django.shortcuts import render
from django.shortcuts import render,redirect

def home(request):
    return render(request, "home_temp.html")

def about(request):
    return render(request, "about.html")

def male_contestants(request):
    return render(request, "male_cont.html")

def female_contestants(request):
    return render(request, "female_cont.html")