from django.shortcuts import render

def home(request):
    return render(request, "home_temp.html")

def about(request):
    return render(request, "about.html")

def vote_page(request):
    return render(request, "vote.html")

def vote_flutter(request):
    return render(request, "voting.html")