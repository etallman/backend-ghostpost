from django.shortcuts import render, HttpResponseRedirect, reverse

from ghostpost.models import Boast, Roast, Vote, AnonUser
from ghostpost.forms import BoastForm, RoastForm

from django.views.generic import DetailView, View

from django.contrib.auth.models import User


def index(request, *args, **kwargs):
    html = 'index.html'
    boast_post = Boast.objects.all()
    roast_post = Roast.objects.all() 
    return render(request, html, {'boast_post': boast_post, 'roast_post': roast_post})

def anonymous_or_real(request):
	# do we have an existing user?
	if request.user.is_authenticated():
		return request.user
	else:
		# if not, create an anonymous user and log them in
		username = IntToLetters(randint(0, maxint))
		u = User(username=username, first_name='Anonymous', last_name='User')
		u.set_unusable_password()
		u.save()
		
		u.username = u.id
		u.save()
		
		# comment out the next two lines if you aren't using profiles
		p = UserProfile(user=u, anonymous=True)
		p.save()
		authenticate(user=u)
		login(request, u)
		return u

class AuthenticationBackendAnonymous:
	'''
		This is for automatically signing in the user after signup etc.
	'''
	def authenticate(self, user=None):
		# make sure they have a profile and that they are anonymous
		# if you're not using profiles you can just return user
		if not user.get_profile() or not user.get_profile().anonymous:
			user = None
		return user
	
	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
class BoastSingleView(DetailView):
    template_name = 'boast.html'
    model=Boast
# def boast(request, *args, **kwargs):
#     html = 'boast.html'
#     boasts = Boast.objects.all()
#     return render(request, html, {'boasts': boasts})

class RoastSingleView(DetailView):
    template_name = 'roast.html'
    model=Roast
# def roast(request, *args, **kwargs):
#     html = 'roast.html'
#     roasts = Roast.objects.all()
#     return render(request, html, {'roasts': roasts})

class RoastFormView(View):
    form_class = RoastForm
    initial = {'key': 'value'}
    template_name = 'form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Roast.objects.create(
                roast=data['roast'],
            )
            return HttpResponseRedirect('index')

        return render(request, self.template_name, {'form': form})

class BoastFormView(View):
    form_class = BoastForm
    initial = {'key': 'value'}
    template_name = 'addboast.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Boast.objects.create(
                boast=data['boast'] 
            )
            return HttpResponseRedirect('index')

        return render(request, self.template_name, {'form': form})

# def add_boast(request, *args, **kwargs):
#     html = 'addboast.html'
#     if request.method == "POST":
#         form = BoastForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Boast.objects.create(
#                 boast=data['boast'],
#             )
#             return  HttpResponseRedirect(reverse('homepage'))
#     form = BoastForm()
    
#     return render(request, html, {'form': form})            


# def add_roast(request, *args, **kwargs):
#     html = 'addroast.html'
   
#     if request.method == "POST":
#         form = RoastForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Roast.objects.create(
#                 roast=data['roast']
#             )
#             return HttpResponseRedirect(reverse('homepage'))
        
#     form = RoastForm()
#     return render(request, html, {'form': form})  

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