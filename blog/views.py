from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<h3 style="margin: auto; text-align:center; font-size:20px;">Hey python you are Incredible</h3>')