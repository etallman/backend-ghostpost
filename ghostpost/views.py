from django.shortcuts import render, HttpResponseRedirect, reverse

from ghostpost.models import Boast, Roast, AnonUser
from ghostpost.forms import BoastForm, RoastForm

def index(request, *args, **kwargs):
    html = 'index.html'
    boast_post = Boast.objects.all()
    roast_post = Roast.objects.all() 
    return render(request, html, {'boast_post': boast_post, 'roast_post': roast_post})

def boast(request, *args, **kwargs):
    html = 'boast.html'
    boasts = Boast.objects.all()
    return render(request, html, {'boasts': boasts})

def roast(request, *args, **kwargs):
    html = 'roast.html'
    roasts = Roast.objects.all()
    return render(request, html, {'roasts': roasts})


def add_boast(request, *args, **kwargs):
    html = 'addboast.html'
    if request.method == "POST":
        form = BoastForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Boast.objects.create(
                boast=data['boast'],
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
                roast=data['roast']
            )
            return HttpResponseRedirect(reverse('homepage'))
        
    form = RoastForm()
    return render(request, html, {'form': form})  

def add_upvote_boast(request, boast_id, *args, **kwargs):
    try:
        boast = Boast.objects.get(id=boast_id)
    except Boast.DoesNotExist():
        pass
    boast.upvote.add(request)
    return HttpResponseRedirect(reverse('homepage'))


def add_downvote_boast(request, boast_id, *args, **kwargs):
    try:
        boast = Boast.objects.get(id=boast_id)
    except Boast.DoesNotExist():
        pass
    boast.downvote.add(request)
    return HttpResponseRedirect(reverse('homepage'))


def remove_upvote_boast(request, boast_id, *args, **kwargs):
    try:
        boast = Boast.objects.get(id=boast_id)
    except Boast.DoesNotExist():
        pass
    boast.upvote.remove(request)
    return HttpResponseRedirect(reverse('homepage'))


def remove_downvote_boast(request, boast_id, *args, **kwargs):
    try:
        boast = Boast.objects.get(id=boast_id)
    except Boast.DoesNotExist():
        pass
    boast.downvote.remove(request)
    return HttpResponseRedirect(reverse('homepage'))


def add_upvote_roast(request, roast_id, *args, **kwargs):
    try:
        roast = Roast.objects.get(id=roast_id)
    except Roast.DoesNotExist():
        pass
    roast.upvote.add(request)
    return HttpResponseRedirect(reverse('homepage'))


def add_downvote_roast(request, roast_id, *args, **kwargs):
    try:
        roast = Roast.objects.get(id=roast_id)
    except Roast.DoesNotExist():
        pass
    roast.downvote.add(request)
    return HttpResponseRedirect(reverse('homepage'))


def remove_upvote_roast(request, roast_id, *args, **kwargs):
    try:
        roast = Roast.objects.get(id=roast_id)
    except Roast.DoesNotExist():
        pass
    roast.upvote.remove(request)
    return HttpResponseRedirect(reverse('homepage'))


def remove_downvote_roast(request, roast_id, *args, **kwargs):
    try:
        roast = Roast.objects.get(id=roast_id)
    except Roast.DoesNotExist():
        pass
    roast.downvote.remove(request)
    return HttpResponseRedirect(reverse('homepage'))