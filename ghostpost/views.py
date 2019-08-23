from django.shortcuts import render, HttpResponseRedirect, reverse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

from ghostpost.models import Boast, Roast, Author, User 
from ghostpost.forms import BoastForm, RoastForm, AuthorForm

def index(request, *args, **kwargs):
    html = 'index.html'
    posts = {
        'boasts': Boast.objects.all(),
        'roasts': Roast.objects.all() 
    }
    return render(request, html, {'posts': posts})


def boast(request, *args, **kwargs):
    html = 'boast.html'
    items = Boast.objects.all()
    return render(request, html, {'boasts': items})


def roast(request, *args, **kwargs):
    html = 'roast.html'
    items = Roast.objects.all()
    return render(request, html, {'roasts': items})


def author(request, *args, **kwargs):
    html = 'author.html'
    posts = {
        'boasts': Boast.objects.all(),
        'roasts': Roast.objects.all() 
    }
    return render(request, html, {'author': posts})


def add_boast(request, *args, **kwargs):
    html = 'addboast.html'
   
    if request.method == "POST":
        form = BoastForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Boast.objects.create(
                boast=data['boast'],
                author=data['author']
            )
            return  HttpResponseRedirect(reverse('homepage'))
   
    form = BoastForm()
    
    return render(request, html, {'form': form})            


def add_roast(request, *args, **kwargs):
    html = 'addroast.html'
   
    if request.method == "POST":
        form = RoastForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Roast.objects.create(
                roast=data['roast'],
                author=data['author']
            )
            return HttpResponseRedirect(reverse('homepage'))
        
    form = RoastForm()
    return render(request, html, {'form': form})  


def add_author(request, *args, **kwargs):
    html = 'addauthor.html'
   
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return  HttpResponseRedirect(reverse('userinput'))
   
    form = AuthorForm()
    return render(request, html, {'form': form})   