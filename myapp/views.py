from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trial(request):
    return HttpResponse("<h1> Project is on Air </h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="Sunil Kumar"
    return render(request,"myapp/profile.html",{'name':name})