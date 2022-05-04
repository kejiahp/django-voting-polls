from django.shortcuts import render

def male_contestants(request):
    return render(request, "male_cont.html")

def female_contestants(request):
    return render(request, "female_cont.html")

def apply(request):
    return render(request, "apply.html")

def apply_submit(request):
    return render(request,"apply_submit.html")