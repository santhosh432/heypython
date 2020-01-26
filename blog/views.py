from django.shortcuts import render, HttpResponse
import random
# Create your views here.


def home(request):
    colors = ['#977', '#997797', '#778799', '#779991', '#859977', '#998a77']
    request.session['color'] = random.choice(colors)
    return render(request, 'blog/home.html')
