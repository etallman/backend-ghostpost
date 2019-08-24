from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from ghostpost.views import index, boast, roast, add_boast, add_roast, add_upvote_boast, add_upvote_roast, add_downvote_boast, add_downvote_roast, remove_downvote_boast, remove_downvote_roast, remove_upvote_boast, remove_upvote_roast

from ghostpost.models import Boast, Roast, AnonUser

admin.site.register(AnonUser)
admin.site.register(Boast)
admin.site.register(Roast)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    # path('message/', message),
    path('roast/', roast),
    path('boast/', boast),
    path('addboast/', add_boast, name='add_boast'),
    path('addroast/', add_roast, name='add_roast'),
    path('removeupvote/<int:boast_id>/', remove_upvote_boast),
    path('removeupvote/<int:roast_id>/', remove_upvote_roast),
    path('removedownvote/<int:boast_id>/', remove_downvote_boast),
    path('removedownvote/<int:roast_id>/', remove_downvote_roast),
    path('addupvote/<int:boast_id>/', add_upvote_boast),
    path('addupvote/<int:roast_id>/', add_upvote_roast),
    path('adddownvote/<int:boast_id>/', add_downvote_boast),
    path('adddownvote/<int:roast_id>/', add_downvote_roast)

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)